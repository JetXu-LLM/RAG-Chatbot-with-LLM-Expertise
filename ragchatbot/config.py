# config.py
import json
import os
from ragchatbot.utils import SingletonMeta

class Config(metaclass=SingletonMeta):
    _config = None

    def __init__(self):
        if Config._config is None:
            with open('config.json', 'r') as file:
                Config._config = json.load(file)
            # Override config with environment variables if needed
            for key, value in os.environ.items():
                if key in Config._config:
                    Config._config[key] = value

    @classmethod
    def get(cls, key, default=None):
        # Ensure the singleton instance is created
        if cls._config is None:
            cls()
        return cls._config.get(key, default)