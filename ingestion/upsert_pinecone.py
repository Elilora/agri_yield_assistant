import asyncio
from utils.logger import get_logger
from embeddings.embedder import embed_text
from ingestion.csv_to_docs import load_csv_and_convert
from vectorstore.pinecone_client import initialise_pinecone, upsert_data_to_pinecone

logger = get_logger(__name__)

BATCH_SIZE = 16
EMBED_CONCURRENCY = 4


async def embed_one(item, semaphore):
    async with semaphore:
        try:
            embedding = await asyncio.to_thread(embed_text, item["text"])
            return {
                "id": item["id"],
                "values": embedding,
                "metadata": item.get("metadata", {})
            }
        except Exception as e:
            logger.error(f"Embedding failed for {item['id']}: {e}")
            return None


async def ingest_async(csv_path):
    logger.info("Loading CSV...")
    docs = load_csv_and_convert(csv_path)
    logger.info(f"Loaded {len(docs)} documents")

    index = initialise_pinecone()
    semaphore = asyncio.Semaphore(EMBED_CONCURRENCY)

    batch_tasks = []
    batch_vectors = []

    for item in docs:
        batch_tasks.append(embed_one(item, semaphore))

        if len(batch_tasks) == BATCH_SIZE:
            results = await asyncio.gather(*batch_tasks)
            batch_tasks.clear()

            for v in filter(None, results):
                batch_vectors.append(v)

            logger.info(f"Upserting batch of {len(batch_vectors)} vectors")
            upsert_data_to_pinecone(index,batch_vectors)
            batch_vectors.clear()

    # 🔹 Handle leftovers
    if batch_tasks:
        results = await asyncio.gather(*batch_tasks)
        for v in filter(None, results):
            batch_vectors.append(v)

    if batch_vectors:
        logger.info(f"Final upsert of {len(batch_vectors)} vectors")
        upsert_data_to_pinecone(index, batch_vectors)


if __name__ == "__main__":
    asyncio.run(ingest_async("data/crop_yield.csv"))
