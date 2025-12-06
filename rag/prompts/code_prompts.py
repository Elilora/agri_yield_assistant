
def generation_prompt(context, query):
    generation_prompt = f"""You are an agricultural assistant. Use the following context to answer the user's question.
                    If context lacks the answer, say: "I don't have enough information in the documents."
    
                    Context:
                    {context}
                    
                    Question: 
                    {query}
                        
                    Answer:"""
    return generation_prompt