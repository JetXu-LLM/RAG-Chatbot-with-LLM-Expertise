import logging
import logging.config
import json
import os
from huggingface_hub import login
from ragchatbot.config import Config
from llama_index.core import Settings
from ragchatbot.models import LLMModel, EmbeddingModel
from llama_index.core.node_parser import SentenceSplitter

def setup_logging(default_path='logging.json', default_level=logging.INFO, env_key='LOG_CFG'):
    """Setup logging configuration"""
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = json.load(f)
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)

def global_setting():
    login(Config.get('hugging_face_hub_token'))
    Settings.llm = LLMModel().sub_llm
    Settings.embed_model = EmbeddingModel().embedding
    Settings.node_parser = SentenceSplitter(chunk_size=Config.get('chunk_size'), chunk_overlap=Config.get('chunk_overlap'))
    Settings.num_output = Config.get('max_tokens') // 4
    Settings.context_window = Config.get('max_tokens')

def initialize():
    print("Start initializing...")
    setup_logging()
    global_setting()
    print("Initialization finished.")