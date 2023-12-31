# models.py
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

class LLMModel:
    def __init__(self, model_name):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

    def answer_question(self, question, context):
        inputs = self.tokenizer.encode(question + context, return_tensors='pt')
        reply_ids = self.model.generate(inputs)
        return self.tokenizer.decode(reply_ids[0], skip_special_tokens=True)
