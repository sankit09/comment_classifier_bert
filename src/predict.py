import torch
from transformers import BertTokenizer
from src.model import BERTClassifier
from src.config import label2id, id2label
from src.preprocessing import clean_comment

def load_model(model_path="models/bert_classifier.pt", num_classes=8):
    model = BERTClassifier(num_classes=num_classes)
    model.load_state_dict(torch.load(model_path, map_location=torch.device("cpu")))
    model.eval()
    return model

def predict_comment(text, model, tokenizer, max_len=128):
    cleaned = clean_comment(text)

    enc = tokenizer(
        cleaned,
        add_special_tokens=True,
        return_tensors='pt',
        padding='max_length',
        truncation=True,
        max_length=max_len
    )

    input_ids = enc["input_ids"]
    attention_mask = enc["attention_mask"]

    with torch.no_grad():
        outputs = model(input_ids=input_ids, attention_mask=attention_mask)
        prediction = torch.argmax(outputs, dim=1).item()

    return id2label[prediction]
