# 🌾 AgriSmart – Crop Yield Intelligence Platform
Agri Yield Assistant is an end-to-end data science, machine learning, and retrieval-augmented generation (RAG) application designed to analyse agricultural data, predict crop yields, and answer questions about crop performance using an AI agent grounded in structured agricultural data.

The application integrates traditional machine learning with modern LLM-powered retrieval to deliver both quantitative predictions and explainable, data-backed insights.

## Key Components
1. Machine Learning for Crop Yield Prediction - Trains predictive models using historical agricultural and environmental data.
2. Vector Search with Pinecone - Stores embedded agricultural records for efficient semantic retrieval.
3. LLM-Powered RAG Agent - Answers user questions by retrieving relevant data from the vector store and generating grounded responses.
4. 📊 Exploratory Data Analysis (EDA) (Planned) - Analysis of agricultural datasets to understand data distributions correlations, seasonal patterns, and key factors influencing crop yield.
4. Web Application(Planned)- Interactive interface for yield predictions and AI-powered agricultural insights.


## Project Goals
1. Understand how factors like rainfall, soil type, temperature, and irrigation affect crop yield
2. Build a machine learning model to predict crop yield
3. Store agricultural records in a vector database
4. Enable natural‑language Q&A over the dataset using a RAG agent
5. Build a web interface for farmers, researchers, and analysts


## Setup Instructions
1. Create virtual environment
```bash
    python -m venv .venv
    source .venv/bin/activate
```
2. Install dependencies
```bash
    pip install -r requirements.txt
```
3. Environment variables - Create a .env file:
```python
    PINECONE_API_KEY=your_key
    COHERE_API_KEY=your_key
```
4. Data Ingestion
```bash
    python -m ingestion.upsert_pinecone
```
This will:
Read CSV
Convert rows to documents
Embed text
Store vectors in Pinecone
5. Run the RAG Agent - Ask questions interactively via CLI.
```bash
    python main.py
```

