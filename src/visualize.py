import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def plot_category_distribution(csv_path, output_path="outputs/category_distribution.png"):
    df = pd.read_csv(csv_path)

    plt.figure(figsize=(10, 6))
    sns.countplot(data=df, x='label', order=df['label'].value_counts().index, palette='Set2')
    plt.title("Comment Category Distribution")
    plt.xlabel("Category")
    plt.ylabel("Count")
    plt.xticks(rotation=30)
    plt.tight_layout()

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path)
    print(f"✅ Category distribution plot saved to {output_path}")
