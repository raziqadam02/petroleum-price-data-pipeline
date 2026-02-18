from src.extract import extract_parquet
from src.logger import setup_logger

setup_logger()

df = extract_parquet("data/raw/fuelprice.parquet")
print(df.head())