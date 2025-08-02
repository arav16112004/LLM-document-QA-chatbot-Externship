#!/usr/bin/env python3

from IPython.display import display, Markdown

import os
# Disable Chroma telemetry 
os.environ["ANONYMIZED_TELEMETRY"] = "false"

from llama_index.core import SimpleDirectoryReader
from llama_index.core.node_parser import SentenceSplitter
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import VectorStoreIndex, StorageContext
from llama_index.vector_stores.chroma import ChromaVectorStore

from chromadb.config import Settings
import chromadb

# Initialize Chroma client with telemetry disabled
settings = Settings(anonymized_telemetry=False)
chroma_client = chromadb.Client(settings=settings)

# Create or get existing collection
chroma_collection = chroma_client.create_collection(
    name="semantic_search_demo",
    get_or_create=True
)


# Chunking 

documents = SimpleDirectoryReader("my_directory").load_data()
splitter = SentenceSplitter(chunk_size=1000, chunk_overlap=10)
chunks = splitter.get_nodes_from_documents(documents)


#embeddings
embed_model = HuggingFaceEmbedding(model_name="sentence-transformers/all-MiniLM-L6-v2")
for chunk in chunks:
    chunk.embedding = embed_model.get_text_embedding(chunk.text)
print("Embeddings Generated Successfully!")


# 3. Storing embeddings and creating index
vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
storage_context = StorageContext.from_defaults(vector_store=vector_store)

index = VectorStoreIndex.from_documents(
    documents,
    storage_context=storage_context,
    embed_model=embed_model
)
print("Vector store created successfully!")


# AI

from llama_index.llms.google_genai import GoogleGenAI
from llama_index.core.llms import ChatMessage

GOOGLE_API_KEY = "AIzaSyCj6NEAxuosAQ1fxK5jAG66NNBzciE4UNM" 
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY


llm = GoogleGenAI(
    model="gemini-2.5-flash"

)

query_engine = index.as_query_engine(
    llm=llm,
    similarity_top_k=2  # Retrieve top 2 most similar chunks
)

def run_query(query_text):
    # Get response
    response = query_engine.query(query_text)
    print(f"\nAI Response:", response.response)
    return response


print(f"\nHi, How may i help you today\n")
while True:
    query1= input(f"\nYour query: ")
    if "bye" in query1:
        print("okay, goodbye")
        break
    run_query(query1)
    




