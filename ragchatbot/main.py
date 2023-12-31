# main.py
import argparse
from ragchatbot.api import start_api_server
from ragchatbot.utils import load_configuration

def main():
    # 解析命令行参数
    parser = argparse.ArgumentParser(description="RAG-Chatbot-with-LLM-Expertise")
    parser.add_argument('--config', type=str, help='Path to the configuration file.')
    args = parser.parse_args()

    # 加载配置
    config = load_configuration(args.config)
    
    # 启动API服务器
    start_api_server(config)

if __name__ == "__main__":
    main()
