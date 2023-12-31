# utils.py
import json

def load_configuration(config_path):
    with open(config_path) as config_file:
        return json.load(config_file)

# 其他可能的工具函数...
