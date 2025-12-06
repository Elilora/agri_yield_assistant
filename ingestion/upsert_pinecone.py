
import time
from util.logger import get_logger
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

    try:
        # Process each row in the dataset
        for item in docs:
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

            # Rate limit handling
            time.sleep(1.0) 

        logger.info("Uploading to Pinecone...")
        upsert_data_to_pinecone(batch)

        logger.info("Ingestion complete!")
    except Exception as e:
        logger.error(f"Error: {e}")


if __name__ == "__main__":
    ingest("data/crop_yield.csv")



