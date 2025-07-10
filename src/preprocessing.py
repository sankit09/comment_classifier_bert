import re
import pandas as pd

def clean_comment(text: str) -> str:
    text = text.lower()
    text = re.sub(r"http\S+|www\S+", "", text)                 # Remove URLs
    text = re.sub(r"@[A-Za-z0-9_]+", "", text)                 # Remove @mentions
    text = re.sub(r"[^\w\s]", "", text)                        # Remove punctuation
    text = re.sub(r"\s+", " ", text).strip()                   # Remove extra whitespace
    return text

def load_and_clean_csv(csv_path: str) -> pd.DataFrame:
    df = pd.read_csv(csv_path)
    df["cleaned_comment"] = df["comment"].apply(clean_comment)
    return df
