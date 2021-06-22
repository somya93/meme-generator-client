from flask import Flask, render_template, request
import requests


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/result', methods=["POST"])
def result():
    url = "http://localhost:3000/generatememe"
    imageURL = request.form.get("imageURL")
    print(imageURL)
    json_data = {"uri": imageURL}

    headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
    response = requests.post(url, json=json_data, headers=headers)
    return response.json()


if __name__ == '__main__':
    app.run(debug=True)
