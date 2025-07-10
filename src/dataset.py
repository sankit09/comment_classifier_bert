import torch
from torch.utils.data import Dataset

class CommentDataset(Dataset):
    def __init__(self, comments, labels, tokenizer, label2id, max_len=128):
        self.comments = comments
        self.labels = labels
        self.tokenizer = tokenizer
        self.label2id = label2id
        self.max_len = max_len

    def __len__(self):
        return len(self.comments)

    def __getitem__(self, idx):
        text = str(self.comments[idx])
        label = self.label2id[self.labels[idx]]

        encodings = self.tokenizer(
            text,
            add_special_tokens=True,
            max_length=self.max_len,
            padding='max_length',
            truncation=True,
            return_tensors='pt'
        )

        return {
            'input_ids': encodings['input_ids'].squeeze(0),
            'attention_mask': encodings['attention_mask'].squeeze(0),
            'label': torch.tensor(label, dtype=torch.long)
        }
