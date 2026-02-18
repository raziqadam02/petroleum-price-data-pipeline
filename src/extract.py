import pandas as pd
import logging

def extract_parquet(path: str) -> pd.DataFrame:
    logging.info(f"Reading parquet file...")
    df = pd.read_parquet(path)
    logging.info(f"Loaded {len(df)} records")
    return df