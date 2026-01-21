
from rag.rag_pipeline import RAGAgent

def main():
    agent = RAGAgent(top_k=5)

    print("Welcome to Agri Yield Assistant!")
    print("Ask a question about crop yields (or type 'exit' to quit).")
    
    while True:
        query = input("\nYour Question: ")
        if query.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break

        print("\nRetrieving information and generating answer...")
        try:
            result = agent.retrieve_and_generate(query)
            print(f"\nAnswer:\n{result['answer']}")
            # show sources
            for doc in result['sources']:
               print(f"- {doc['id']}: {doc['text'][:100]}...")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
