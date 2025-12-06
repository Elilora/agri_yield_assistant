from util.config import pinecone_index, embedding_dimension PINECONE_API_KEY 
from pinecone import Pinecone, ServerlessSpec


def initialise_pinecone():
    """Initialise Pinecone index 
       Creates index if it doesn't exist (which in this case did not exist)  
       Returns Pinecone index"""

    # pinecone client using config
    pinecone = Pinecone(api_key=PINECONE_API_KEY)
                                
   
    # FIX HERE: list of index names extracted from objects
    existing_indexes = [idx["name"] for idx in   pinecone.list_indexes()]

    # create index if it doesn't exist, dim is 768 for multilingual-22-12  
    if pinecone_index not in existing_indexes:
        pinecone.create_index(pinecone_index, dimension=embedding_dimension,metric="cosine",
        spec=ServerlessSpec(cloud="aws", region="us-east-1"))
        # Wait for index creation to propagate
        time.sleep(5)
    else:
        print(f"Index '{pinecone_index}' already exists")
    return pinecone.Index(pinecone_index)


def upsert_data_to_pinecone(vectors):
    """Upsert data to Pinecone index"""

    # pinecone index initialised
    pinecone_index = initialise_pinecone()
    
    if vectors:
        # upsert data to pinecone index
        pinecone_index.upsert(vectors=vectors)
    else:
        print("No data to upsert")
           