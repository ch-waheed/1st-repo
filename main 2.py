from flask import Flask, request
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/question', methods=['POST'])
def process_question():
    # Retrieve the question from the request
    question = request.json['question']

    # Process the question and generate an answer
    answer = process_question_function(question)

    # Return the answer as JSON
    return {'answer': answer}

def process_question_function(question):
    # Implement your logic to process the question and generate an answer
    # You can use any NLP library or techniques that fit your requirements
    # Here's a simple example that checks for specific keywords in the question
    if 'engine' in question:
        answer = "The engine parts you may need include spark plugs, filters, and belts."
    elif 'brake' in question:
        answer = "For brakes, you might require brake pads, rotors, and brake fluid."
    elif 'tire' in question:
        answer = "Tire-related parts include tires, inner tubes, and valve stems."
    else:
        answer = "I'm sorry, I don't have information about that specific car part."

    return answer

if __name__ == '__main__':       
    app.run(debug=True)
               