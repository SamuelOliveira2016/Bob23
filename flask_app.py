from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import bob  # Importing bob.py

app = Flask(__name__)
CORS(app)

db =bob.chave_openai

@app.route('/', methods=['POST'])
@cross_origin()
def chat():
    print("Received request:", request.json)
    data = request.json
    if data and 'text' in data:
        received_text = data['text']
        #response = bob.process_query(received_text)  # Using the function from bob.py
        processed_data = {"response": f"Echo: {received_text}"}
    else:
        processed_data = {"response": "Echo: None"}
    return jsonify(processed_data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)  # Runs the server on port 5000 with debug mode on
