# dataScience/data_visual/visual.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Path to dataset
DATA_PATH = r"A:\Projects\AI-Powered-Cyber-Threat-Detection-Dashboard\dataScience\dataset\processed_data.xlsx"

def load_data():
    """Load the dataset for visualization"""
    print(f"📂 Loading dataset from: {DATA_PATH}")
    df = pd.read_excel(DATA_PATH)
    print("✅ Dataset loaded:", df.shape)
    return df

def plot_class_distribution(df, target_col="Label"):
    """Plot bar chart of class distribution"""
    if target_col in df.columns:
        plt.figure(figsize=(6,4))
        sns.countplot(x=df[target_col])
        plt.title("Class Distribution")
        plt.xlabel("Class")
        plt.ylabel("Count")
        plt.show()
    else:
        print("⚠️ Target column not found for class distribution plot.")

def plot_correlation_heatmap(df):
    """Plot heatmap of correlations among numeric features"""
    plt.figure(figsize=(10,6))
    sns.heatmap(df.corr(), cmap="coolwarm", annot=False, cbar=True)
    plt.title("Correlation Heatmap")
    plt.show()

def plot_feature_distributions(df, n_cols=5):
    """Plot histograms for numeric features"""
    numeric_cols = df.select_dtypes(include="number").columns
    df[numeric_cols].hist(figsize=(16, 12), bins=30, layout=(-1, n_cols))
    plt.suptitle("Feature Distributions", size=18)
    plt.show()

if __name__ == "__main__":
    df = load_data()
    plot_class_distribution(df, target_col="Label")
    plot_correlation_heatmap(df)
    plot_feature_distributions(df)
