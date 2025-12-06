import sys
from agents.tools import retrieve_crop_info
from rag.generator import generate_answer

def main():
    print("Welcome to Agri Yield Assistant!")
    print("Ask a question about crop yields (or type 'exit' to quit).")
    
    while True:
        query = input("\nYour Question: ")
        if query.lower() in ['exit', 'quit']:
            print("Goodbye!")
            break
            
        print("\nRetrieving information...")
        try:
            context = retrieve_crop_info(query)
            # print(f"DEBUG Context: {context[:200]}...") # Uncomment for debugging
            
            print("Generating answer...")
            answer = generate_answer(query, context)
            
            print(f"\nAnswer:\n{answer}")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
