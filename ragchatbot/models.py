# models.py
import torch
from llama_index.llms.huggingface import HuggingFaceLLM
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from ragchatbot.config import Config
from ragchatbot.utils import SingletonMeta

class LLMModel(metaclass=SingletonMeta):
    def __init__(self):
        if not hasattr(self, 'initialized'):  # This will prevent reinitialization
            self._main_llm = HuggingFaceLLM(
                context_window=Config.get('max_tokens'),
                max_new_tokens=Config.get('max_tokens') // 4, 
                model_name=Config.get('main_model'),
                tokenizer_name=Config.get('main_model'),
                device_map=Config.get('device'),
                generate_kwargs={"temperature": 0.7, "top_k": 50, "top_p": 0.95},
                model_kwargs={"torch_dtype": torch.float16, "load_in_8bit": False, "trust_remote_code":True},
                # messages_to_prompt=messages_to_prompt,
                # completion_to_prompt=completion_to_prompt,
            )
            if Config.get('main_model') == Config.get('sub_model'):
                self._sub_llm = self._main_llm
            else:
                self._sub_llm = HuggingFaceLLM(model_name=Config.get('sub_model'), device=Config.get('device'))
            self.initialized = True

    @property
    def main_llm(self):
        return self._main_llm
    
    @property
    def sub_llm(self):
        return self._sub_llm

class EmbeddingModel(metaclass=SingletonMeta):
    def __init__(self):
        if not hasattr(self, 'initialized'):  # This will prevent reinitialization
            self._embedding = HuggingFaceEmbedding(model_name=Config.get('embedding_model'), device=Config.get('device'), trust_remote_code=True)
            self.initialized = True

    @property
    def embedding(self):
        return self._embedding


# class LLMModel:
#     def __init__(self, main_model, sub_model, device):
#         self.tokenizer = AutoTokenizer.from_pretrained(main_model, device_map=device, trust_remote_code=True)
#         self.model = AutoModelForCausalLM.from_pretrained(main_model, device_map=device, trust_remote_code=True, torch_dtype=torch.float16)
#         self.model.eval()
#         # whether main_model equals sub_model
#         if main_model == sub_model:
#             self.sub_model = self.model
#             self.sub_tokenizer = self.tokenizer
#         else:
#             self.sub_tokenizer = AutoTokenizer.from_pretrained(sub_model, device_map=device, trust_remote_code=True)
#             self.sub_model = AutoModelForCausalLM.from_pretrained(sub_model, device_map=device, trust_remote_code=True, torch_dtype=torch.float16)
#             self.sub_model.eval()

#     def answer_question(self, question, context, max_tokens=8000):
#         # Coding the question and context
#         inputs = self.tokenizer.encode_plus(context, question, add_special_tokens=True, return_tensors='pt').to(self.model.device)
#         # generate answer
#         reply_ids = self.model.generate(**inputs, max_new_tokens=200, pad_token_id=self.tokenizer.eos_token_id, eos_token_id=self.tokenizer.eos_token_id, length_penalty=0.9, no_repeat_ngram_size=3, do_sample=True, top_k=5, top_p=0.9, temperature=0.86, num_beams=5, early_stopping=True, use_cache=True, num_return_sequences=2)
#         # Decode the generated answer
#         return self.tokenizer.decode(reply_ids[0], skip_special_tokens=True)