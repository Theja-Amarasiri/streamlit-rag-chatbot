# Multi Document RAG Chatbot
This project contains a fast, modern Retrieval Augmented Generation chatbot built with LangChain, Groq, FAISS, and Streamlit. Upload multiple documents (PDF, DOCX, TXT, MD) and ask natural language questions. The chatbot retrieves the most relevant chunks and generates accurate answers using Groq’s LLMs.
Features
1.	Multi Document Upload Upload multiple PDFs, Word docs, text files, or markdown files. All documents are chunked, embedded, and stored in a unified vector store.
2.	Smart Retrieval Using FAISS + HuggingFace embeddings for efficient semantic search.
3.	Chat Interface Developing a clean and user-friendly UI with created with Streamlit.
4.	Modular Architecture demonstration Optimizing document loading, chunking, vector storage, and RAG pipeline are cleanly separated.
# Architecture Overview
User Uploads Docs ↓ Document Loaders (PDF, DOCX, TXT, MD) ↓ Recursive Text Splitter ↓ HuggingFace Embeddings ↓ FAISS Vector Store ↓ Retriever (k=2) ↓ Groq LLM ↓ Final Answer
Tech Stack Used In This Project
•	Python 3.10+
•	Streamlit (UI)
•	LangChain (RAG pipeline)
•	FAISS (vector search)
•	HuggingFace Embeddings
•	Groq API (LLM inference)
•	PyPDF, docx2txt, unstructured (document parsing)

# Quick Installation (Windows)
python -m venv .venv  
.venv\Scripts\activate  
pip install -r requirements.txt  
streamlit run app.py  
# Supported File Types
•	.pdf
•	.docx
•	.txt
•	.md
# Getting a Groq API Key
1.	Visit the Groq Console: https://console.groq.com
2.	Sign in or create a free account.
3.	Navigate to the API Keys section in the sidebar.
4.	Click Create API Key.
5.	Copy the generated key.
6.	Create a .env file using your new API key. (An example format to create this is available in .env.example. :)
# User Interface using Streamlit
 <img width="900" height="445" alt="image" src="https://github.com/user-attachments/assets/90f2b12a-0710-480d-bb73-395634b3b314" />

# Author
Theja Nadeeja Amarasiri  
Computer Science (AI) Undergraduate  
Swinburne University of Technology

