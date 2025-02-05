# PDF Chatbot 🦜
A Streamlit-based PDF chatbot that allows users to upload and interact with PDF documents. It uses OpenAI embeddings and FAISS for efficient document retrieval and intelligent question answering.

# Features
Upload and process multiple PDFs.
Extract and analyze text from PDFs.
Vectorize text using OpenAI embeddings.
Store embeddings in FAISS for fast retrieval.
Interactive chatbot interface to ask questions about the PDFs.

## Requirements
Python 3.11 or higher
Streamlit
PyPDF2
LangChain
FAISS
OpenAI API key


# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate

# Install Dependencies

pip install -r requirements.txt
