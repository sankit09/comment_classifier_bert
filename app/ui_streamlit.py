import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from transformers import BertTokenizer
from src.predict import load_model, predict_comment
from src.response_templates import generate_response
from src.config import id2label
from src.preprocessing import clean_comment

# Load model and tokenizer once
@st.cache_resource
def load_assets():
    model = load_model("models/bert_classifier.pt", num_classes=len(id2label))
    tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
    return model, tokenizer

model, tokenizer = load_assets()

st.set_page_config(page_title="Comment Categorizer", layout="centered")
st.title("💬 Comment Categorization & Reply Assistant")

# Section 1: Manual Comment Input
st.subheader("🧪 Try it out:")
user_input = st.text_area("Enter a comment")

if st.button("Predict Category"):
    if user_input:
        cleaned = clean_comment(user_input)
        label = predict_comment(cleaned, model, tokenizer)
        response = generate_response(label)
        st.success(f"**Predicted Category:** {label}")
        st.info(f"**Suggested Response:** {response}")
    else:
        st.warning("Please enter a comment first.")

# Section 2: CSV Upload
st.subheader("📁 Bulk Upload Comments (CSV)")

uploaded_file = st.file_uploader("Upload a CSV file with a `comment` column", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file, quotechar='"')


    if "comment" not in df.columns:
        st.error("CSV must contain a 'comment' column.")
    else:
        df["cleaned_comment"] = df["comment"].apply(clean_comment)
        df["predicted_label"] = df["cleaned_comment"].apply(lambda x: predict_comment(x, model, tokenizer))
        df["auto_response"] = df["predicted_label"].apply(generate_response)

        st.success("✅ Comments categorized successfully!")

        st.subheader("📊 Category Distribution")
        chart_data = df["predicted_label"].value_counts().reset_index()
        chart_data.columns = ["Category", "Count"]
        st.bar_chart(chart_data.set_index("Category"))

        st.subheader("📄 Categorized Comments")
        st.dataframe(df[["comment", "predicted_label", "auto_response"]])

        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button("📥 Download Result CSV", data=csv, file_name="categorized_comments.csv", mime='text/csv')
