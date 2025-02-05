import os
import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def process_pdfs(pdfs):
    text = ""
    for pdf in pdfs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text() or ""
    return text

def create_vector_store(text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    embeddings = OpenAIEmbeddings()
    return FAISS.from_texts(chunks, embeddings)

def main():
    st.title("PDF Chatbot 🦜")
    
    # Initialize session state
    if "history" not in st.session_state:
        st.session_state.history = []
    if "vector_store" not in st.session_state:
        st.session_state.vector_store = None

    # PDF Upload
    pdfs = st.sidebar.file_uploader(
        "Upload PDFs", 
        type="pdf", 
        accept_multiple_files=True,
        help="Select multiple PDF files to analyze"
    )

    # Process PDFs when uploaded
    if pdfs and not st.session_state.vector_store:
        with st.spinner("Analyzing PDFs..."):
            text = process_pdfs(pdfs)
            st.session_state.vector_store = create_vector_store(text)

    # Chat interface
    user_input = st.chat_input("Ask about your PDFs:")
    
    if user_input:
        if not st.session_state.vector_store:
            st.error("Please upload PDFs first!")
            return
            
        # Add user question to history
        st.session_state.history.append(("user", user_input))
        
        with st.spinner("Thinking..."):
            qa = RetrievalQA.from_chain_type(
                llm=OpenAI(temperature=0.3),
                chain_type="stuff",
                retriever=st.session_state.vector_store.as_retriever()
            )
            response = qa.run(user_input)
            
        # Add bot response to history
        st.session_state.history.append(("assistant", response))
    
    # Display chat history
    for role, message in st.session_state.history:
        with st.chat_message(role):
            st.markdown(message)

if __name__ == "__main__":
    main()
    