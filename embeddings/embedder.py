import cohere
from util.config import embedding_model, COHERE_API_KEY


# cohere client initialised
cohere_client = cohere.Client(api_key = COHERE_API_KEY)

def embed_text(text):
    """Embed text using Cohere"""
    response = cohere_client.embed(texts=[text], model=embedding_model)
    return response.embeddings[0]

