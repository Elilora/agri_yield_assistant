from rag.retriever import get_relevant_docs
from rag.generator import generate_answer
from utils.logger import get_logger

logger = get_logger(__name__)

def rag_pipeline(query, top_k=5):
    """RAG Pipeline"""

    #retrieve docs
    docs = get_relevant_docs(query, top_k=top_k)
    logger.info(f"Retrieved {len(docs)} documents")

    #merge context
    context = "\n\n".join([d["text"] for d in docs])
    logger.info(f"Context: {context}")
    
    # generate answer
    answer = generate_answer(query, context)
    logger.info(f"Answer: {answer}")

    return {"query": query,"answer": answer,"sources": docs}

# Test pipeline
if __name__ == "__main__":
    query = "What is the yield of Wheat in North region?"
    result = rag_pipeline(query)
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