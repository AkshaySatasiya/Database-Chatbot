import os
import pandas as pd
import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.agents import create_sql_agent, AgentType
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langchain.sql_database import SQLDatabase
from langchain.llms import OpenAI
from langchain.callbacks import get_openai_callback
from langchain.agents import Tool
import time
import openai
from langchain.agents import Tool

# Set your OpenAI API key
os.environ["OPENAI_API_KEY"] = "YOUR_OPENAI_API_KEY"

# Database connection
db_user = "postgres"
db_password = "PASSWORD"
db_host = "localhost"
db_name = "schoolDB"
db_port = 5432
SQLALCHEMY_DATABASE_URL = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
db = SQLDatabase.from_uri(SQLALCHEMY_DATABASE_URL)

# LLM and SQL agent setup
llm = ChatOpenAI(model_name="gpt-3.5-turbo-0125",temperature=0.1)
toolkit = SQLDatabaseToolkit(db=db, llm=llm)

SQL_PREFIX = """You are an agent designed to interact with a SQL database.
First analyze the input and choose which function or tool you have to use.
Given an input question, create a syntactically correct {dialect} query to run, then look at the results of the query and return the answer.
Unless the user specifies a specific number of examples they wish to obtain, always limit your query to at most {top_k} results.
You can order the results by a relevant column to return the most interesting examples in the database.
Never query for all the columns from a specific table, only ask for the relevant columns given the question.
You have access to tools for interacting with the database.
Only use the below tools. Only use the information returned by the below tools to construct your final answer.
You MUST double check your query before executing it. If you get an error while executing a query, rewrite the query and try again.

DO NOT make any DML statements (INSERT, UPDATE, DELETE, DROP etc.) to the database.

If the question does not seem related to the database, just return "I don't know" as the answer.
"""

SQL_FUNCTIONS_SUFFIX = """I should look at the input ans select which function to call, always double check input and select appropriate function.\n If the input is related to database then i should look at the tables in the database to see what I can query.  Then I should query the schema of the most relevant tables."""



def greeting_input(input=""):
    return "User input is greeting, reply approprietly"

# Define tools for greeting 
greeting_tool = Tool(
    name="greeting_input",
    func= greeting_input,
    description="Always use this tool before caling any athor tool. Use this tool when you have to answer any greeting input. Always use this tool before executing any other function"
)
tool = [greeting_tool]


agent_executor = create_sql_agent(
    llm=llm,
    extra_tools=tool,
    toolkit=toolkit, 
    verbose=True, 
    agent_type=AgentType.OPENAI_FUNCTIONS,
    prefix=SQL_PREFIX,
    suffix=SQL_FUNCTIONS_SUFFIX
    )

prompt_template = """
Your role is to communicate effectively with the user, ensuring responses are appropriate to the query type and manageably sized.
Your task is to assist users with their queries. When a query is related to the 'sql_bot' database, refine it for clarity and accuracy, and provide detailed responses in a tabular format.\nFor queries that are not related to the database, respond in a conversational and friendly manner.\nYour responses should be informative and tailored to the type of query. \n
Sapecific instructions:
-> For database-related queries: Provide detailed answers in a tabular format. If a query could return a large amount of data, limit the response to a subset (like the top 10 entries) and inform the user about this limitation.
-> For non-database-related queries: Engage in a helpful and friendly manner, providing answers or assistance as a conversational chatbot would.
"""



# @traceable(name="Function call")
def count_tokens(chain, query):
    with get_openai_callback() as cb:
        # Combine the prompt template with the user's query
        full_query = prompt_template + "\nUser query: " + query
        # Process the combined query
        try:
            result = chain.run(full_query)
            # st.text(f'Spent a total of {cb} tokens')
        except Exception as e:
            result = "I don't have suffiecient resource to process your query !"
            return e
    return result

# Streamlit app
def main():
    st.title("Universal Chatbot: SQL Database")

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Accept user input
    user_query = st.chat_input("Enter your query:")

    if user_query:
        # Displaying the User Message
        with st.chat_message("user"):
            st.markdown(user_query)

        # Process the user's query using the SQL agent
        start_time = time.time()
        response = count_tokens(agent_executor, user_query)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(elapsed_time)

        # Displaying and Storing the Assistant Message
        with st.chat_message("assistant"):
            st.markdown(response)
            st.markdown(elapsed_time)

        # Storing Messages
        st.session_state.messages.append({"role": "user", "content": user_query})
        st.session_state.messages.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    main()