import pandas as pd

def row_to_text(row):
    """Convert a single CSV row to a text document."""
    return f""" Region: {row['Region']}
                Soil Type: {row['Soil_Type']}
                Crop: {row['Crop']}
                Rainfall: {row['Rainfall_mm']} mm
                Temperature: {row['Temperature_Celsius']}°C
                Fertilizer Used: {row['Fertilizer_Used']}
                Irrigation Used: {row['Irrigation_Used']}
                Weather Condition: {row['Weather_Condition']}
                Days to Harvest: {row['Days_to_Harvest']}
                Yield: {row['Yield_tons_per_hectare']} tons/ha """.strip()


def row_to_metadata(row):
    
    """Clean metadata for Pinecone."""
    return {
        "region": row["Region"],
        "soil_type": row["Soil_Type"],
        "crop": row["Crop"],
        "rainfall_mm": float(row["Rainfall_mm"]),
        "temperature_c": float(row["Temperature_Celsius"]),
        "fertilizer_used": bool(row["Fertilizer_Used"]),
        "irrigation_used": bool(row["Irrigation_Used"]),
        "weather_condition": row["Weather_Condition"],
        "days_to_harvest": int(row["Days_to_Harvest"]),
        "yield_tph": float(row["Yield_tons_per_hectare"])}


def load_csv_and_convert(path):
    df = pd.read_csv(path)
    docs = []
    
    for i, row in df.iterrows():
        doc_id = f"row_{i}"
        text = row_to_text(row)
        metadata = row_to_metadata(row)
        docs.append({
            "id": doc_id,
            "text": text,
            "metadata": metadata})
    
    return docs
