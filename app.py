from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Implement your prediction logic here
    # Get the uploaded resume file and use your machine learning model to predict job fit

    # For now, just return a sample prediction (0 or 1)
    prediction = 1

    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
