from llama_index.core import SimpleDirectoryReader

# Load PDF or text document
documents = SimpleDirectoryReader("my_directory").load_data()


from llama_index.core.node_parser import SentenceSplitter


splitter_fixed = SentenceSplitter(chunk_size=300, chunk_overlap=50) 
chunks_fixed = splitter_fixed.get_nodes_from_documents(documents)
print(f"Total Fixed-Length Chunks Created: {(chunks_fixed[0].get_content())}")

print(f"Total Fixed-Length Chunks Created: {(chunks_fixed[1].get_content())}")




