import streamlit as st
from dotenv import load_dotenv

from document_loader import load_documents
from vector_store import build_vector_store
from rag_pipeline import build_rag_pipeline

load_dotenv()

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

if "retriever" not in st.session_state:
    st.session_state.retriever = None

if "last_upload" not in st.session_state:
    st.session_state.last_upload = None

# Sidebar
with st.sidebar:
    st.header("Upload Documents Here!")
    uploaded_files = st.file_uploader(
        "Choose files",
        type=["pdf", "docx", "txt", "md"],
        accept_multiple_files=True
    )

    if uploaded_files != st.session_state.last_upload:
        st.session_state.last_upload = uploaded_files
        st.session_state.messages = []

        if uploaded_files:
           docs = load_documents(uploaded_files)
           st.session_state.retriever = build_vector_store(docs)
           st.success(f"{len(uploaded_files)} document(s) uploaded!")

        for f in uploaded_files:
            st.write(f"- {f.name}")

# Main UI
st.title("RAG Doc‑Helper :)")
st.write("Ask anything about your documents!")

# Chat input
user_input = st.chat_input("Ask something about your documents")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    if st.session_state.retriever:
        rag = build_rag_pipeline(st.session_state.retriever)
        answer = rag(user_input)
    else:
        answer = "Please upload documents first."

    st.session_state.messages.append({"role": "assistant", "content": answer})

# Display chat history
for msg in st.session_state.messages: 
    with st.chat_message(msg["role"]): 
        st.write(msg["content"])
