from flask import Flask, render_template, request
from model.emotion_model import predict_emotion

app = Flask(__name__)

# Route untuk halaman utama (input feedback)
@app.route('/')
def index():
    return render_template('index.html')

# Route untuk menerima feedback dan memproses emosi
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        feedback = request.form['feedback']
        # Prediksi emosi menggunakan model
        emotion = predict_emotion(feedback)
        return render_template('index.html', feedback=feedback, emotion=emotion)

if __name__ == '__main__':
    app.run(debug=True)
