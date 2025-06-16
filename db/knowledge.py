import chromadb
from chromadb.utils import embedding_functions
import os

# Setup ChromaDB client and collection
chroma_client = chromadb.Client()
chroma_collection = chroma_client.get_or_create_collection(name="chapters")

# Add to DB
def store_chapter(chapter_id, content):
    chroma_collection.add(
        documents=[content],
        ids=[chapter_id],
        metadatas=[{"chapter": chapter_id}]
    )
    print(f"✅ Stored chapter '{chapter_id}' in ChromaDB.")

# Search from DB
def search_chapter(query_text, top_k=1):
    results = chroma_collection.query(
        query_texts=[query_text],
        n_results=top_k
    )
    return results
