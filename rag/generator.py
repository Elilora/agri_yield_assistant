import cohere
from utils.config import COHERE_API_KEY
from rag.prompts.code_prompts import generation_prompt

# Initialize Cohere client
cohere_client = cohere.Client(api_key=COHERE_API_KEY)

def generate_answer(query, context):
    """
    Generate an answer to the query using the provided context.
    
    Args:
        query (str): The user's question.
        context (str): The retrieved context relevant to the question.
        
    Returns:
        str: The generated answer.
    """
    
    prompt=generation_prompt(context, query)

    response = cohere_client.generate(model='command',prompt=prompt,max_tokens=300,temperature=0.7,)
    
    return response.generations[0].text.strip()



#With Langchain
  """from langchain_cohere import ChatCohere
from langchain_core.prompts import ChatPromptTemplate

llm = ChatCohere()

prompt = ChatPromptTemplate.from_template(\"""
You are an agricultural analytics assistant.
Answer using ONLY the provided context.

Question: {question}

Context:
{context}

If context is insufficient, say "I don't have enough information."
\""")
"""
