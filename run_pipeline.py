import pandas as pd
from transformers import BertTokenizer
from src.config import id2label
from src.predict import load_model, predict_batch
from src.response_templates import generate_response
from src.preprocessing import clean_comment
from src.visualize import plot_category_distribution

def main(input_csv="data/raw_comments.csv", output_csv="outputs/categorized_comments.csv"):
    print("🔍 Loading data...")
    df = pd.read_csv(input_csv)
    df["cleaned_comment"] = df["comment"].apply(clean_comment)

    print("📦 Loading model and tokenizer...")
    tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
    model = load_model("models/bert_classifier.pt", num_classes=len(id2label))

    print("🤖 Predicting categories...")
    df["predicted_label"] = [predict_comment(c, model, tokenizer) for c in df["cleaned_comment"]]

    print("✍️ Generating auto-responses...")
    df["auto_response"] = df["predicted_label"].apply(generate_response)

    print(f"💾 Saving categorized comments to: {output_csv}")
    df.to_csv(output_csv, index=False)

    print("📊 Plotting distribution chart...")
    plot_category_distribution(output_csv)

    print("✅ Pipeline complete!")

# Required: import predict_comment from predict manually
from src.predict import predict_comment

if __name__ == "__main__":
    main()
