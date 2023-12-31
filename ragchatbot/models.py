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

    def answer_question(self, question, context, device):
        # 对问题和上下文进行编码
        inputs = self.tokenizer.encode_plus(question, context, add_special_tokens=True, return_tensors='pt').to(device)
        # 生成回答
        reply_ids = self.model.generate(inputs['input_ids'], attention_mask=inputs['attention_mask'], max_new_tokens=2000, do_sample=True, temperature=0.2, top_k=50, top_p=0.95, pad_token_id=self.tokenizer.eos_token_id)
        # 解码生成的回答
        return self.tokenizer.decode(reply_ids[0], skip_special_tokens=True)