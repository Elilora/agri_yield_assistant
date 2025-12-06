import os
from dotenv import load_dotenv
from vectorstore.pinecone_client import initialise_pinecone
from embeddings.embedder import embed_text

load_dotenv(dotenv_path=".env.local")

class PineconeRetriever:
    def __init__(self, index_name="agri-assistant"):
        self.index = initialise_pinecone()

    def get_relevant_docs(self, query, top_k=3):
        """
        Retrieve relevant documents from Pinecone based on the query.
        """
        # Generate embedding for the query
        query_embedding = embed_text(query)

        # Query Pinecone
        results = self.index.query(
            vector=query_embedding,
            top_k=top_k,
            include_metadata=True
        )

        # Extract relevant information
        docs = []
        for match in results['matches']:
            docs.append({
                "id": match['id'],
                "score": match['score'],
                "metadata": match['metadata']
            })
        
        return docs

if __name__ == "__main__":
    # Test the retriever
    retriever = PineconeRetriever()
    results = retriever.get_relevant_docs("What is the yield of Wheat in North region?")
    for doc in results:
        print(doc)
