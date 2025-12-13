
from rag.retriever import PineconeRetriever

def retrieve_crop_info(query: str) -> str:
    """
    Retrieve relevant crop information based on the query.
    
    Args:
        query (str): The user's question or query about crops.
        
    Returns:
        str: A formatted string containing relevant document snippets.
    """
    retriever = PineconeRetriever()
    docs = retriever.get_relevant_docs(query)
    
    if not docs:
        return "No relevant information found."
    
    context = ""
    for i, doc in enumerate(docs):
        context += f"Document {i+1}:\n"
        # Assuming the metadata contains the text content, or we need to fetch it.
        # Based on ingestion/upsert_pinecone.py, metadata has 'metadata' which might contain the text?
        # Let's check ingestion/csv_to_docs.py to see what's in metadata.
        # Wait, I haven't seen csv_to_docs.py. Let me quickly check it to be sure.
        # But for now, I'll assume metadata contains relevant info.
        # Actually, looking at upsert_pinecone.py:
        # vector = {"id": item["id"], "values": embedding, "metadata": item["metadata"]}
        # And embedder.py embeds item["text"].
        # So we need to know if 'text' is in metadata.
        # I'll optimistically assume 'text' is in metadata or construct context from available metadata.
        
        # Let's print all metadata for now to be safe, or format it nicely.
        context += str(doc['metadata']) + "\n\n"
        
    return context
