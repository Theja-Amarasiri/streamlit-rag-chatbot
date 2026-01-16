from langchain_community.document_loaders import PyPDFLoader, Docx2txtLoader, TextLoader

def load_documents(uploaded_files):
    all_docs = []

    for file in uploaded_files:
        file_type = file.name.split(".")[-1].lower()

        # Save temporarily
        temp_path = f"temp_{file.name}"
        with open(temp_path, "wb") as f:
            f.write(file.read())

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

    return all_docs
