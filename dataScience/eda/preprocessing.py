import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

DATA_PATH = r"A:\Projects\AI-Powered-Cyber-Threat-Detection-Dashboard\dataScience\dataset\data.xlsx"

def load_data():
    print(f"📂 Loading dataset from: {DATA_PATH}")
    df = pd.read_excel(DATA_PATH)
    print("✅ Dataset loaded:", df.shape)
    return df

def clean_data(df):
    print("🧹 Cleaning data...")
    df = df.drop_duplicates()
    drop_cols = [col for col in df.columns if "Unnamed" in col or "Flow ID" in col]
    df = df.drop(columns=drop_cols, errors="ignore")
    for col in df.select_dtypes(include=[np.number]).columns:
        df[col] = df[col].replace([np.inf, -np.inf], np.nan)
        df[col] = df[col].fillna(df[col].median())
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].fillna(df[col].mode()[0])
    print("✅ After cleaning:", df.shape)
    return df

def encode_labels(df):
    print("🔑 Encoding labels...")
    le = LabelEncoder()
    if "Label" in df.columns:
        df["Label"] = le.fit_transform(df["Label"])
    return df
def save_data(df):
    PROCESSED_DATA_PATH = r"A:\Projects\AI-Powered-Cyber-Threat-Detection-Dashboard\dataScience\dataset\processed_data.xlsx"
    df.to_excel(PROCESSED_DATA_PATH, index=False)
    print(f"💾 Saved processed dataset at: {PROCESSED_DATA_PATH} ({df.shape})")


if __name__ == "__main__":
    df = load_data()
    df = clean_data(df)
    df = encode_labels(df)
    save_data(df)
