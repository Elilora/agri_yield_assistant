from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

def embed_text(text):
    return model.encode(text).tolist()


"""import cohere
from utils.config import embedding_model, COHERE_API_KEY


# cohere client initialised
cohere_client = cohere.Client(api_key = COHERE_API_KEY)

def embed_text(text):
    \"""Embed text using Cohere\"""
    response = cohere_client.embed(texts=[text], model=embedding_model)
    return response.embeddings[0]"""
