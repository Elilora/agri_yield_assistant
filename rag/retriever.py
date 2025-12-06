
from vectorstore.pinecone_client import initialise_pinecone
from embeddings.embedder import embed_text


def get_relevant_docs(query, top_k=5):
        """
        Retrieve relevant documents from Pinecone based on the query.
        """
        
        # pinecone index initialised
        index = initialise_pinecone()

        # generate embedding for the query
        query_embedding = embed_text(query)
         
        # Query Pinecone
        results = index.query(vector=query_embedding, top_k=top_k,include_metadata=True)

        # Extract relevant information
        retrieved_docs = []
        for match in results['matches']:
            docs.append({
                "id": match['id'],
                "score": match['score'],
                "text": match['metadata'].get("text"),
                "metadata": match['metadata']})
        
        return retrieved_docs

# Test block
if __name__ == "__main__":
    results = get_relevant_docs("What is the yield of Wheat in North region?")
    for doc in results:
        print(doc)



# LANGCHAIN IMPLEMENTATION
"""
from langchain_pinecone import PineconeVectorStore
from util.config import PINECONE_INDEX_NAME, embedding_model


vectorstore = PineconeVectorStore(index_name=PINECONE_INDEX_NAME,embedding=embedding_model)

def get_retriever(top_k=5):
    \"""
    Retrieve relevant documents from Pinecone based on the query.
    \"""
    return vectorstore.as_retriever(search_kwargs={"k": top_k})
"""