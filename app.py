from flask import Flask, render_template, request
import pandas as pd
import os
from model import perform_kmeans

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    file = request.files['file']
    clusters = int(request.form['clusters'])
    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        plot_path = perform_kmeans(filepath, clusters)
        return render_template('result.html', image_path=plot_path)
    return "No file uploaded."

if __name__ == "__main__":
    app.run(debug=True)
