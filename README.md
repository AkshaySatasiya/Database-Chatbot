# SQL Chatbot Assistant with Custom Greeting Tool 🤖

## Introduction 📜

The SQL Chatbot Assistant with Custom Greeting Tool is a Streamlit application designed to facilitate seamless interaction between users and a PostgreSQL database using natural language processing capabilities provided by OpenAI and the LangChain framework. This innovative application not only allows for efficient querying of SQL databases but also introduces a unique greeting tool, enhancing user experience with personalized interactions.

## Installation 💾

To set up the SQL Chatbot Assistant on your local machine, follow these steps:

1. Ensure Python 3.9+ is installed.
2. Clone the repository to your local machine.
3. Install required packages using pip:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up a PostgreSQL database and update the connection details accordingly in the script.

## Configuration ⚙️

Before running the application, configure the following environment variables:

- `OPENAI_API_KEY`: Your OpenAI API key for accessing GPT models.
- Database connection details (`db_user`, `db_password`, `db_host`, `db_port`, `db_name`) in the script.

## Usage 🚀

To start the application, run the following command in your terminal:

```bash
streamlit run app.py
```

Navigate to the provided local URL in your web browser to interact with the chatbot.

## Features ✨

- **Natural Language Query Processing**: Leverage OpenAI's GPT model for interpreting and processing natural language queries.
- **Custom Greeting Tool**: A specialized tool designed to handle greetings, enhancing user interactions with the chatbot.
- **SQL Database Integration**: Direct integration with PostgreSQL databases for executing queries based on user input.
- **Streamlit Interface**: A user-friendly web interface for interacting with the chatbot.
- **Error Handling and Logging**: Includes mechanisms to handle errors and log them for troubleshooting.

## Dependencies 📦

- Python 3.9+
- Streamlit
- pandas
- openai
- langchain
- PostgreSQL

Refer to `requirements.txt` for a detailed list of required packages.

## Documentation 📖

For more detailed information on the LangChain library, OpenAI GPT models, and Streamlit, please refer to their official documentation:

- [LangChain Documentation](https://langchain.com)
- [OpenAI API Documentation](https://openai.com/api)
- [Streamlit Documentation](https://docs.streamlit.io)

## Examples 🌟

- **Querying for the top 10 students by performance**: "Show me the top 10 students in our database based on their overall performance."
- **Finding specific course details**: "I need information on the Machine Learning course offered this semester."
- **Handling greetings**: "Hello, can you help me find the most popular course right now?"

These examples demonstrate the versatility of the chatbot in handling both specific database queries and general conversational inputs.

## Troubleshooting 🔧

If you encounter any issues, first ensure all environment variables are correctly set and that your PostgreSQL database is accessible. For more specific problems, consult the application logs and refer to the [Troubleshooting section](#troubleshooting) in this document.

## Contributors 🤝

To contribute to this project, please fork the repository, make your changes, and submit a pull request. For major changes or enhancements, please open an issue first to discuss what you would like to change.

## License 📄

This project is licensed under the MIT License - see the LICENSE file for details.
