# Lamini Model Tuning with Meta-Llama

This project demonstrates how to fine-tune a language model using the Lamini API, specifically leveraging the Meta-Llama-3-8B-Instruct model. The project focuses on customizing the model's responses to specific inputs by providing a dataset for tuning.

## Project Structure
```
project-directory/ 
│ ├── app.py 
├── requirements.txt 
├── .env 
├── README.md 
├── LICENSE 
└── .gitignore
```


## Getting Started

### Prerequisites

Ensure you have the following installed:
- Python 3.8 or higher
- Pip (Python package installer)
- Google Colab (for running the code, or you can run it locally)

### Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/groq-langsmith-chatbot.git
cd groq-langsmith-chatbot
```

2. Install the required Python packages:

```bash 
pip install -r requirements.txt
```

3. Set up your environment variables in the `.env` file or via Google Colab:

```bash
from google.colab import userdata
groq_api_key = userdata.get('groq_api_key')
langsmith = userdata.get('LANGSMITH_API_KEY')
print(langsmith)

import os
os.environ["LANGCHAIN_API_KEY"] = langsmith
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "CourseLanggraph"
```
Replace the placeholder with your actual API keys.

1. Running the Application
2. Ensure your .env file is properly configured with your Groq and LangSmith API keys.

```bash
Run the Python script:
```

- Alternatively, you can run the project in Google Colab:
- Set up the environment variables in Google Colab as described above.
- Run the cells in the notebook sequentially.
- The chatbot will prompt you to enter user input. You can interact with the chatbot in the console.

## Example Usage

- Enter your message when prompted by the chatbot.
- The chatbot processes your input, maintains the conversation's state, and generates a response.
- Type "quit" or "q" to exit the conversation.

## Integration Details

- `Groq API`: Utilized for generating the chatbot's responses using the Gemma2-9b-It model.
- `LangSmith`: Manages the tracing and logging of the conversation flow.
- `LangGraph`: Handles the state management and graph-based flow control for the conversation.

## Files

- `app.py`: The main Python script that handles the chatbot's logic, integration with Groq API, LangSmith, and LangGraph.
- `requirements.txt`: Lists all the Python dependencies needed to run the application.
- `.env`: Contains the API keys for Groq and LangSmith. This file should not be included in version control.
- `README.md`: This file, providing an overview of the project.
- `LICENSE`: The project's license, specifying how others may use the code.
- `.gitignore`: Specifies files and directories that should be ignored by Git, such as the .env file and any other sensitive information.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## .gitignore
The following files are ignored in the version control:
```bash
.env
__pycache__/
*.pyc
*.pyo
*.pyd
```
## Contributing
Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## Acknowledgments
- Thanks to Groq for providing powerful APIs and models for advanced NLP tasks.
- Thanks to LangSmith for enabling detailed tracing and logging.
- Thanks to LangGraph for simplifying state management in conversational AI.

