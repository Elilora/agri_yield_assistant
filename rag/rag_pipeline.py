from rag.retriever import get_relevant_docs
from rag.generator import generate_answer
from utils.logger import get_logger

logger = get_logger(__name__)

class RAGAgent:
    def __init__(self, top_k=5):
        self.top_k = top_k
    
    def retrieve_and_generate(self, query):
        """Run the full RAG pipeline"""
        # Retrieve docs
        docs = get_relevant_docs(query, top_k=self.top_k)
        logger.info(f"Retrieved {len(docs)} documents")

        # Merge context
        context = "\n\n".join([d["text"] for d in docs])
        logger.info(f"Context: {context}")

        # Generate answer
        answer = generate_answer(query, context)
        logger.info(f"Answer: {answer}")

        return {"query": query, "answer": answer, "sources": docs}
    


# Test pipeline
if __name__ == "__main__":
    query = "What is the yield of Wheat in North region?"
    result = RAGAgent().retrieve_and_generate(query)
    print(result)


# with langchain
"""
from langchain_core.runnables import RunnableMap, RunnablePassthrough
from rag.retriever import get_retriever
from rag.generator import llm, prompt

def rag_pipeline():
    retriever = get_retriever()

    return (
        {"context": retriever, "question": RunnablePassthrough()}
        | prompt| llm)

"""


