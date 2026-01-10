
import time
from utils.logger import get_logger
from embeddings.embedder import embed_text
from ingestion.csv_to_docs import load_csv_and_convert
from vectorstore.pinecone_client import initialise_pinecone, upsert_data_to_pinecone

# logger
logger = get_logger(__name__)

def ingest(csv_path):
    logger.info("Loading CSV...")
    docs = load_csv_and_convert(csv_path)

    pinecone_index = initialise_pinecone()
    
    batch = []
    Batch_size = 10


    for item in docs:
        try:
            logger.info(f"Embedding {item['id']}...")
            embedding = embed_text(item["text"])

            # Check if document already exists in Pinecone
            existing = pinecone_index.fetch(ids=[item["id"]])

            # Skip duplicate
            if item["id"] in existing.vectors:
                logger.info(f"Duplicate document skipped: {item['id']}")
                continue  

            # Create document for Pinecone
            vector = {
                "id": item["id"],
                "values": embedding,
                "metadata": item["metadata"]}

            batch.append(vector)

            # Upsert every N vectors
            if len(batch) >= Batch_size:
                logger.info(f"Upserting batch of {len(batch)} vectors...")
                upsert_data_to_pinecone(batch)
                batch.clear()

            time.sleep(2.0)  

        except Exception as e:
            logger.error(f"Skipping {item['id']} due to error: {e}")
            continue

    # Final flush
    if batch:
        logger.info(f"Final upsert of {len(batch)} vectors...")
        upsert_data_to_pinecone(batch)


if __name__ == "__main__":
    ingest("data/crop_yield.csv")



