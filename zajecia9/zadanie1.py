from flask import Flask, request, jsonify, render_template_string, redirect, url_for
from transformers import pipeline

app = Flask(__name__)


summarizer = pipeline("summarization", model="t5-small")
streszczenie = None

@app.route('/new', methods=['POST'])
def new():
    global streszczenie
    data = request.get_json()
    text = "summarize: " + data["data"]
    streszczenie = summarizer(text, max_length=60, min_length=20, do_sample=False)
    return jsonify(data), 201

@app.route('/', methods=['GET'])
def output():
    if streszczenie:
        return jsonify(streszczenie[0]['summary_text']), 200
    else:
        return jsonify("brak"), 404

if __name__ == '__main__':
    app.run(debug=True)