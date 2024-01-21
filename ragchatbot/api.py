# api.py
from flask import Flask, request, jsonify, render_template
from ragchatbot.models import LLMModel

app = Flask(__name__)

def create_app(config):
    app.model = LLMModel(main_model=config['main_model'], sub_model=config['sub_model'], device=config['device'])
    return app

@app.route('/')
def index():
    # Render a simple HTML form for inputting the question.
    return render_template('index.html')

@app.route('/answer', methods=['POST'])
def answer():
    print("answer api start")
    content = request.json
    question = content['question']
    context = content['context']
    print(question)
    print(context)
    response = app.model.answer_question(question, context)
    return jsonify({'answer': response})

def start_api_server(config):
    global app
    app = create_app(config)
    app.run(host=config['host'], port=config['port'])
