import os
import cohere
from dotenv import load_dotenv


load_dotenv(dotenv_path=".env.local")

# cohere client initialised
cohere_client = cohere.Client(api_key = os.getenv("COHERE_API_KEY"))

# embedding model initialised
embedding_model = "multilingual-22-12"

def embed_text(text):
    """Embed text using Cohere"""
    response = cohere_client.embed(texts=[text], model=embedding_model)
    return response.embeddings[0]

