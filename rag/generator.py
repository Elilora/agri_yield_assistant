import os
import cohere
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env.local")

# Initialize Cohere client
cohere_client = cohere.Client(api_key=os.getenv("COHERE_API_KEY"))

def generate_answer(query: str, context: str) -> str:
    """
    Generate an answer to the query using the provided context.
    
    Args:
        query (str): The user's question.
        context (str): The retrieved context relevant to the question.
        
    Returns:
        str: The generated answer.
    """
    
    prompt = f"""You are an agricultural assistant. Use the following context to answer the user's question.
    If the answer is not in the context, say you don't know.
    
    Context:
    {context}
    
    Question: 
    {query}
    
    Answer:"""
    
    response = cohere_client.generate(
        model='command',
        prompt=prompt,
        max_tokens=300,
        temperature=0.7,
    )
    
    return response.generations[0].text.strip()
