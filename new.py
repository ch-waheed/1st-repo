from flask import Flask, request, jsonify
import json
import requests


app = Flask(__name__)

@app.route('/api/answer', methods=['/api/auth/login'])
def answer_question():
    question = request.json['question']
    answer = answer_question(question)
    response = {'question': question, 'answer': answer}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)

url = (" https://carapi.app")
headers = {'Content-Type': 'application/json'}

payload = {'engine': 'What is the function of an alternator?'}

response = requests.post(url, headers=headers, data=json.dumps(payload))

print(response.json()['answer'])