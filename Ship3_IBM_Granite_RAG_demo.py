#!/usr/bin/env python3
"""
Ship 3 — IBM Granite Standard RAG — Demo Script
First run: builds chroma_db. Subsequent runs: loads existing store.
"""
import os
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_chroma import Chroma

print("Ship 3 — IBM Granite Standard RAG")
print("─" * 50)

embeddings = OllamaEmbeddings(model="nomic-embed-text")
llm = ChatOllama(model="granite4.1:3b", temperature=0.7)
print("✅ Embeddings ready: nomic-embed-text")
print("✅ LLM ready: granite4.1:3b")

PERSIST_DIR = "./chroma_db"
SOURCE = "/Users/evelyn/Repos/Mirror-Project/MIRROR_LOG.md"

if os.path.exists(PERSIST_DIR) and os.listdir(PERSIST_DIR):
    vector_store = Chroma(
        persist_directory=PERSIST_DIR,
        embedding_function=embeddings,
    )
    print(f"✅ Vector store loaded: {vector_store._collection.count()} documents")
else:
    print("📦 Building vector store from Mirror archive...")
    loader = TextLoader(SOURCE)
    documents = loader.load()
    splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50, separator="\n")
    texts = splitter.split_documents(documents)
    vector_store = Chroma.from_documents(
        documents=texts,
        embedding=embeddings,
        persist_directory=PERSIST_DIR,
    )
    print(f"✅ Vector store created: {len(texts)} chunks")

retriever = vector_store.as_retriever(search_kwargs={"k": 4})

queries = [
    "What is the Mirror of My Becoming?",
    "When did Evelyn start building the Mirror project?",
]

print()
for query in queries:
    print(f"Query: {query}")
    print("─" * 50)
    results = retriever.invoke(query)
    context = "\n\n".join(doc.page_content for doc in results)
    response = llm.invoke(f"Based on the following context, answer the question: {query}\n\nContext: {context}")
    print("Answer:")
    print(response.content)
    print()

print("─" * 50)
print("Demo complete.")
