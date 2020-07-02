import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('vader_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('HTMLPage2.html')

@app.route('/predict',methods=['POST'])
def predict():
    sentence = request.form.values()
    score = model.polarity_scores(sentence)

    return render_template('HTMLPage2.html', prediction_text='The overall scores of the sentence is {}'.format(str(score['compound'])))

if __name__ == "__main__":
    app.run(debug=True)