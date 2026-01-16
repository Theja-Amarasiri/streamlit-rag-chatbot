import os
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

def build_rag_pipeline(retriever):
    llm = ChatGroq(
        model="groq/compound",
        temperature=0,
        api_key=os.getenv("GROQ_API_KEY")
    )

    prompt = ChatPromptTemplate.from_template(
        "Use only the context to answer. If not found, say 'I don't know.'\n\n"
        "Context:\n{context}\n\nQuestion:\n{question}"
    )

    def rag(question):
        docs = retriever.invoke(question)
        context = "\n\n".join([d.page_content for d in docs])

        # Prevent Groq 413 errors
        MAX_CONTEXT_CHARS = 8000
        context = context[:MAX_CONTEXT_CHARS]

        chain = prompt | llm
        response = chain.invoke({"context": context, "question": question})
        return response.content

    return rag
