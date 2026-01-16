import os
from dotenv import load_dotenv

# Load environment variables 
load_dotenv(dotenv_path=".env.local")

# Expose variables
COHERE_API_KEY = os.getenv("COHERE_API_KEY")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")

# embedding model 
embedding_model = "all-MiniLM-L6-v2"
#"multilingual-22-12"

# pinecone index name
pinecone_index = "agri-assistant-384"

# embedding dimension
embedding_dimension= 384
