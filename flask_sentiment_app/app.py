from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load pipeline
with open('sentiment_pipeline.pkl', 'rb') as f:
    pipeline = pickle.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    ulasan = request.form['text']
    prediksi = pipeline.predict([ulasan])[0]
    hasil = 'Positif 😊' if prediksi == 'positive' else 'Negatif 😞'
    return render_template('result.html', prediction=hasil)

if __name__ == '__main__':
    app.run(debug=True)
