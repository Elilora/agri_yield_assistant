from rag.pipeline import RAGAgent

rag_agent = RAGAgent()

def rag_tool(query):
    """
    Tool for answering knowledge-based questions using RAG
    """
    return rag_agent.retrieve_and_generate(query)
