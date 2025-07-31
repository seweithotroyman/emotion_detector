import torch
from transformers import BertTokenizer, BertForSequenceClassification

# Inisialisasi model dan tokenizer BERT (misalnya menggunakan pre-trained model)
model_name = 'bert-base-uncased'
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertForSequenceClassification.from_pretrained(model_name, num_labels=8)

# Fungsi untuk melakukan prediksi emosi
def predict_emotion(feedback):
    # Tokenisasi input feedback
    inputs = tokenizer(feedback, return_tensors='pt', padding=True, truncation=True, max_length=512)
    
    # Model prediksi
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
        predicted_class = torch.argmax(logits, dim=1).item()

    # Daftar emosi sesuai dengan label dari model
    emotion_labels = ['joy', 'sadness', 'fear', 'anger', 'surprise', 'anticipation', 'trust', 'disgust']
    
    return emotion_labels[predicted_class]
