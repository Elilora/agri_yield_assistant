
import time
from ingestion.csv_to_docs import load_csv_and_convert
from embeddings.embedder import embed_text
from vectorstore.pinecone_client import initialise_pinecone, upsert_data_to_pinecone

def ingest(csv_path):
    print("Loading CSV...")
    docs = load_csv_and_convert(csv_path)

    pinecone_index = initialise_pinecone()

    batch = []

    try:
        # Process each row in the dataset
        for item in docs:
            print(f"Embedding {item['id']}...")
            embedding = embed_text(item["text"])

            # Check if document already exists in Pinecone
            existing = pinecone_index.fetch(ids=[item["id"]])

            if item["id"] in existing.vectors:
                print(f"Duplicate document skipped: {item['id']}")
                continue  # Skip duplicate

            # Create document for Pinecone
            vector = {
                "id": item["id"],
                "values": embedding,
                "metadata": item["metadata"]}

            batch.append(vector)
            time.sleep(1.0) # Rate limit handling

        print("Uploading to Pinecone...")
        upsert_data_to_pinecone(batch)

        print("Ingestion complete!")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    ingest("data/crop_yield.csv")



