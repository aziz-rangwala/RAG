# RAG

# PDF Chat Application

A RAG-based web application that allows users to chat with their PDF documents using LangChain and Ollama LLM.

## Features

- 📄 PDF document upload
- 💬 Interactive chat interface
- 🤖 RAG (Retrieval Augmented Generation) based responses
- 🔍 Context-aware conversations
- 🚀 Built with Streamlit for a clean UI
- 🆓 Uses free, open-source LLM (Ollama/Llama2)

## Prerequisites

- Python 3.8+
- [Ollama](https://ollama.ai/) installed on your system
- Virtual environment (recommended)

## Installation

1. Clone the repository

```
git clone https://github.com/yourusername/pdf-chat-app.git
cd pdf-chat-app
```

2. Create and activate virtual environment

```
python -m venv venv
source venv/bin/activate
```

3. Install dependencies

```
pip install -r requirements.txt
```

4. Install Ollama and pull the Llama2 model

```bash
# Install Ollama from https://ollama.ai/
ollama pull llama2
```

5. Run the app

```
streamlit run app.py
```

## Usage

1. Start the Streamlit application:

```bash
streamlit run app.py
```

2. Open your web browser and navigate to `http://localhost:8501`

3. Upload a PDF document using the sidebar

4. Click "Process PDF" and wait for the processing to complete

5. Start chatting with your document!

## Project Structure

```
project/
├── app.py              # Main Streamlit application
├── utils.py            # Utility functions for PDF processing and RAG
├── requirements.txt    # Python dependencies
├── README.md          # Project documentation
├── .gitignore         # Git ignore file
└── venv/              # Virtual environment (not tracked in git)
```



    