import pandas as pd
from pathlib import Path

RAW = Path("data/raw/leads.csv")
OUT = Path("data/processed/data.csv")

def ingest():
    df = pd.read_csv(RAW)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUT, index=False)

if __name__ == "__main__":
    ingest()

