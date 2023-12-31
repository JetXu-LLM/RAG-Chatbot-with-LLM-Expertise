# api.py
from flask import Flask, request, jsonify
from ragchatbot.models import LLMModel

app = Flask(__name__)
llm_model = LLMModel(model_name='mistralai/Mixtral-8x7B-Instruct-v0.1')

@app.route('/answer', methods=['POST'])
def get_answer():
    data = request.get_json()
    question = data['question']
    context = data['context']
    answer = llm_model.answer_question(question, context)
    return jsonify(answer=answer)

def start_api_server(config):
    app.run(host=config['host'], port=config['port'])
