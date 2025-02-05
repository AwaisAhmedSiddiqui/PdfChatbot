PDF Chatbot 🦜
A Streamlit-based PDF chatbot that allows users to upload PDF files and ask questions related to their content. This chatbot utilizes LangChain and OpenAI embeddings to analyze PDF text and provide intelligent responses. Built with Python, it uses FAISS for efficient document retrieval.

Features
Upload and process multiple PDFs
Extract text from PDF pages
Split the text into chunks for embedding
Use OpenAI's embeddings to vectorize text
Store embeddings in FAISS vector store
Interactive chatbot interface to ask questions about the PDFs
Real-time responses based on uploaded documents
Requirements
Python 3.11 or higher
Streamlit
LangChain
PyPDF2
OpenAI API key
FAISS
Installation
Follow these steps to set up the project locally:

1. Clone the Repository
Clone the repository to your local machine.

bash
Copy
Edit
git clone https://github.com/your-username/pdf-chatbot.git
cd pdf-chatbot
2. Create and Activate a Virtual Environment
It's recommended to use a virtual environment to keep your dependencies isolated.

bash
Copy
Edit
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
3. Install Dependencies
Install the required packages using pip.

bash
Copy
Edit
pip install -r requirements.txt
4. Set Up Environment Variables
Create a .env file in the project root and add your OpenAI API key and HuggingFaceHub API token.

bash
Copy
Edit
# .env file

OPENAI_API_KEY=your-openai-api-key
HuggingFaceHub_API_TOKEN=your-huggingface-api-token
You can obtain an OpenAI API key by signing up on OpenAI's website.

**5. Run the Application**
Run the Streamlit app to start the chatbot interface.

bash
Copy
Edit
streamlit run app.py
The app will open in your default web browser. You can upload your PDF files and start interacting with the chatbot.

Usage
**Upload PDFs**
Use the file uploader in the sidebar to upload multiple PDF files. These PDFs will be analyzed and processed.
Ask Questions
Once the PDFs are uploaded, you can type questions in the chatbot interface to interact with the PDF contents.
The chatbot will provide answers based on the text extracted from the PDFs.
