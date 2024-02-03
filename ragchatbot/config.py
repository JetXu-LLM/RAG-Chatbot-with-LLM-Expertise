# config.py
import json
import os

class Config:
    _instance = None

    @staticmethod
    def get_instance():
        if Config._instance is None:
            Config()
        return Config._instance

    def __init__(self):
        if Config._instance is not None:
            raise Exception("This class is a singleton!")
        else:
            with open('config.json', 'r') as file:
                self.config = json.load(file)
            # Override config with environment variables if needed
            for key, value in os.environ.items():
                if key in self.config:
                    self.config[key] = value
            Config._instance = self

    @staticmethod
    def get(key, default=None):
        return Config.get_instance().config.get(key, default)
