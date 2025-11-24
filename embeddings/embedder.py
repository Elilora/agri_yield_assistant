import os
import cohere

# cohere client initialised
cohere_client = cohere.client(api_key = os.getenv("COHERE_API_KEY"))

# embedding model initialised
emedding_model = "multilingual-22-12"

def embed_text(text):
    """Embed text using Cohere"""
    response = cohere_client.embed(text=[text], model=emedding_model)
    return response.embeddings[0]
    
