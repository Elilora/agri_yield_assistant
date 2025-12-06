import os
from dotenv import load_dotenv
from pinecone import Pinecone

load_dotenv(dotenv_path=".env.local")

pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
indexes = pc.list_indexes()
print(f"Type: {type(indexes)}")
print(f"Content: {indexes}")
for i in indexes:
    print(f"Item: {i}, Name: {i.name}")
