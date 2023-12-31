# utils.py
import json

def load_configuration(file_path):
    with open(file_path, 'r') as config_file:
        config = json.load(config_file)
    return config