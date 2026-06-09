import os
from langchain_community.document_loaders import PyPDFLoader, Docx2txtLoader, TextLoader

def load_documents(uploaded_files):
    all_docs = []

    for file in uploaded_files:
        file_type = file.name.split(".")[-1].lower()
        temp_path = f"temp_{file.name}"
        
        # Save temporarily
        with open(temp_path, "wb") as f:
            f.write(file.read())

        try:
            # Choose loader
            if file_type == "pdf":
                loader = PyPDFLoader(temp_path)
            elif file_type == "docx":
                loader = Docx2txtLoader(temp_path)
            elif file_type in ["txt", "md"]:
                loader = TextLoader(temp_path)
            else:
                continue

            docs = loader.load()
            all_docs.extend(docs)
            
        finally:
            # Clean up the file so it doesn't leak storage
            if os.path.exists(temp_path):
                os.remove(temp_path)

    return all_docs