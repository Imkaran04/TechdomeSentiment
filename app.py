from flask import Flask, render_template, request, jsonify
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification
import torch

app = Flask(__name__)

MODEL_PATH = "./model"
tokenizer = DistilBertTokenizer.from_pretrained(MODEL_PATH)
model = DistilBertForSequenceClassification.from_pretrained(MODEL_PATH)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=256)
        with torch.no_grad():
            logits = model(**inputs).logits
        probs = torch.nn.functional.softmax(logits, dim=-1)
        prediction = torch.argmax(probs, dim=-1).item()
        sentiments = ["Negative", "Neutral", "Positive"]
        return render_template('index.html', prediction=sentiments[prediction])
    return render_template('index.html', prediction=None)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0') 
