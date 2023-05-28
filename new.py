from flask import Flask, request, jsonify
import json


app = Flask(__name__)

@app.route('/api/answer', methods=['POST'])
def answer_question():
    question = request.json['question']
    answer = answer_question(question)
    response = {'question': question, 'answer': answer}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)