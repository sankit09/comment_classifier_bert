# 💬 Comment Categorization & Reply Assistant (BERT-Based NLP Tool)

This is a BERT-powered NLP tool that classifies user comments into meaningful categories like praise, constructive criticism, hate, threat, and more. It also generates empathetic, category-specific auto-responses to assist brands and creators in efficiently engaging with their audience.

---

## 🎯 Project Objective

Automatically:
- Detect the **intent or emotion** in a comment
- **Classify** it into one of 8 actionable categories
- **Generate suitable responses** for each category
- **Visualize** category distribution
- Support **single and batch comment inputs**

---

## 📁 Project Structure

```bash
comment_classifier_bert/
├── app/
│   └── ui_streamlit.py         # Streamlit user interface
├── models/
│   └── bert_classifier.pt      # Trained model weights
├── src/
│   ├── dataset.py              # Dataset and DataLoader class
│   ├── model.py                # BERTClassifier architecture
│   ├── predict.py              # Inference and label mapping
│   └── train.py                # Model training logic
├── sample_comments.csv         # Sample input for testing
├── requirements.txt            # Python dependencies
└── README.md                   # Project overview (this file)



Here’s your content formatted in **clean markdown (`README.md`) style**:

---

````markdown
# 🧠 Target Comment Categories

This tool classifies comments into the following **8 categories**:

| Label ID | Category               | Example Comment                                           |
|----------|------------------------|-----------------------------------------------------------|
| 0        | Praise                 | "Amazing visuals and perfect sound design!"              |
| 1        | Support                | "Keep going, you're doing great!"                        |
| 2        | Constructive Criticism | "The animation was okay but the voiceover felt off."     |
| 3        | Hate/Abuse             | "This is trash. Do better."                              |
| 4        | Threat                 | "I'll report this garbage."                              |
| 5        | Emotional              | "This reminded me of my childhood."                      |
| 6        | Irrelevant/Spam        | "Follow me for quick giveaways!"                         |
| 7        | Question/Suggestion    | "Can you make one on space exploration next?"            |

---

# 🛠 Tech Stack

- **Language**: Python 3.11  
- **Model**: `bert-base-uncased`  
- **Libraries**:
  - `transformers` (Hugging Face)
  - `pandas`, `numpy`, `scikit-learn`
  - `torch` (PyTorch)
  - `Streamlit` (UI)
  - `matplotlib`, `seaborn`

---

# 🚀 How to Run

### 1. Clone and Install Dependencies

```bash
git clone https://github.com/yourusername/comment_classifier_bert.git
cd comment_classifier_bert
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
````

### 2. Train the Model (Optional if `bert_classifier.pt` exists)

```bash
PYTHONPATH=. python src/train.py
```

This trains the BERT model and saves weights to `models/bert_classifier.pt`.

### 3. Run the Streamlit App

```bash
PYTHONPATH=. streamlit run app/ui_streamlit.py
```

Then open [http://localhost:8501](http://localhost:8501) in your browser.

---

# 📊 Features

✅ Classify both single and batch comments
✅ Suggest personalized auto-responses
✅ Visualize category distribution in bar chart
✅ Upload `.csv` file or use manual input
✅ Download categorized comments as CSV
✅ Modular, production-ready codebase
✅ Trained on 1,000 labeled comment samples

---

# 🧪 Sample Input (`sample_comments.csv`)

```csv
comment
"Amazing visuals and perfect sound design!"
"I didn't like the ending, but the animation was great."
"This is complete trash. Do better."
"Can you make one on space exploration next?"
"Follow me for quick giveaways!"
```

---

# 💡 Example Output

| comment                                        | predicted\_label       | auto\_response                                                                 |
| ---------------------------------------------- | ---------------------- | ------------------------------------------------------------------------------ |
| Amazing visuals and perfect sound design!      | Praise                 | Thanks so much for your kind words! 🙌                                         |
| I didn't like the ending, but the animation... | Constructive Criticism | Thank you for the honest feedback! We'll work to improve. 💡                   |
| This is complete trash. Do better.             | Hate/Abuse             | We’re here to foster respectful conversations. Your feedback has been noted.   |
| Can you make one on space exploration next?    | Question/Suggestion    | Great question/suggestion! We’ll pass it to the team. 🗨️                      |
| Follow me for quick giveaways!                 | Irrelevant/Spam        | Thanks for your interest! However, we ask users to avoid off-topic promotions. |

---

# 📈 Performance (on 1,000+ samples)

| Metric          | Value  |
| --------------- | ------ |
| Train Loss      | \~0.45 |
| Validation Acc. | 99%    |
| Epochs          | 4      |
| Optimizer       | AdamW  |

---

# 📌 To Improve Further

* Add confidence scores for predictions
* Enable feedback collection on auto-responses
* Extend to multilingual comment support
* Deploy via Hugging Face or Streamlit Cloud

---

# 👤 Author

**Ankit Srivastava**
Data Scientist & AI Engineer


```
