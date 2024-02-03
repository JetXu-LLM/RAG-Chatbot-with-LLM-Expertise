# api.py
from flask import Flask, request, jsonify, render_template
from ragchatbot.models import LLMModel
from ragchatbot.config import Config

app = Flask(__name__)

def create_app():
    app.model = LLMModel(main_model=Config.get('main_model'), sub_model=Config.get('sub_model'), device=Config.get('device'))
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
    max_tokens = Config.get('max_tokens', 8000)
    print(question)
    print(context)
    response = app.model.answer_question(question, context, max_tokens)
    return jsonify({'answer': response})

def start_api_server():
    global app
    app = create_app()
    app.run(host=Config.get('host'), port=Config.get('port'))
