# models.py
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

class LLMModel:
    def __init__(self, main_model, sub_model, device):
        self.tokenizer = AutoTokenizer.from_pretrained(main_model, device_map=device, trust_remote_code=True)
        self.model = AutoModelForCausalLM.from_pretrained(main_model, device_map=device, trust_remote_code=True, torch_dtype=torch.float16)
        self.model.eval()
        # whether main_model equals sub_model
        if main_model == sub_model:
            self.sub_model = self.model
            self.sub_tokenizer = self.tokenizer
        else:
            self.sub_tokenizer = AutoTokenizer.from_pretrained(sub_model, device_map=device, trust_remote_code=True)
            self.sub_model = AutoModelForCausalLM.from_pretrained(sub_model, device_map=device, trust_remote_code=True, torch_dtype=torch.float16)
            self.sub_model.eval()

    def answer_question(self, question, context):
        # Coding the question and context
        inputs = self.tokenizer.encode_plus(context, question, add_special_tokens=True, return_tensors='pt').to(self.model.device)
        # generate answer
        #reply_ids = self.model.generate(inputs['input_ids'], attention_mask=inputs['attention_mask'], max_tokens=32000, pad_token_id=self.tokenizer.eos_token_id)
        reply_ids = self.model.generate(**inputs, max_new_tokens=30000-inputs['input_ids'].shape[-1], pad_token_id=self.tokenizer.eos_token_id)
        # Decode the generated answer
        return self.tokenizer.decode(reply_ids[0], skip_special_tokens=True)