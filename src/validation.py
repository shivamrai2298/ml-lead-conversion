import pandas as pd

def validate(df):
    assert set(["converted"]).issubset(df.columns)
    assert df["converted"].isin([0,1]).all()

if __name__ == "__main__":
    df = pd.read_csv("data/processed/data.csv")
    validate(df)

