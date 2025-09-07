import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler

# Path to dataset
DATA_PATH = r"A:\Projects\AI-Powered-Cyber-Threat-Detection-Dashboard\dataScience\dataset\processed_data.xlsx"

def load_data():
    """Load the preprocessed dataset from dataset folder"""
    print(f"📂 Loading dataset from: {DATA_PATH}")
    df = pd.read_excel(DATA_PATH)
    print("✅ Dataset loaded:", df.shape)
    return df

def select_features(df, target_col="Label"):
    """
    Separate features (X) and target (y).
    By default, 'Label' column is treated as the target.
    """
    print("🎯 Selecting features and target...")
    if target_col in df.columns:
        X = df.drop(columns=[target_col])
        y = df[target_col]
    else:
        X, y = df, None
    print(f"✅ Features: {X.shape}, Target: {None if y is None else y.shape}")
    return X, y

def scale_features(X, method="standard"):
    """
    Scale numeric features for ML models.
    - method="standard" : StandardScaler (mean=0, std=1)
    - method="minmax"   : MinMaxScaler (range 0–1)
    """
    print(f"⚖️ Scaling features using {method} scaler...")
    numeric_cols = X.select_dtypes(include=[np.number]).columns
    X_scaled = X.copy()

    if method == "standard":
        scaler = StandardScaler()
        X_scaled[numeric_cols] = scaler.fit_transform(X[numeric_cols])
    elif method == "minmax":
        scaler = MinMaxScaler()
        X_scaled[numeric_cols] = scaler.fit_transform(X[numeric_cols])
    else:
        raise ValueError("❌ Invalid method. Use 'standard' or 'minmax'.")

    print("✅ Scaling completed.")
    return X_scaled

def save_features(X, y=None):
    """Save processed features (and target if available) back to XLSX"""
    df_out = X.copy()
    if y is not None:
        df_out["Label"] = y  # add back target column

    df_out.to_excel(DATA_PATH, index=False)
    print(f"💾 Saved feature dataset at: {DATA_PATH} ({df_out.shape})")

if __name__ == "__main__":
    df = load_data()
    X, y = select_features(df)
    X = scale_features(X, method="standard")  # change to "minmax" if needed
    save_features(X, y)
