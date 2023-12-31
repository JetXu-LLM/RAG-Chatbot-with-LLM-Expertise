# main.py
import sys
import logging
from ragchatbot.api import start_api_server
from ragchatbot.utils import load_configuration

def main():
    # 解析命令行参数
    config = load_configuration('config.json')
    main_model = config.get('main_model')
    sub_model = config.get('sub_model')

    # 加载配置
    config = load_configuration('./config.json')
    
    # 启动API服务器
    start_api_server(config)

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)
    # 打开一个文件用于写入
    f = open('output_log', 'w')
    original_stdout = sys.stdout  # 保存原始的sys.stdout
    original_stderr = sys.stderr  # 保存原始的sys.stderr
    sys.stdout = f
    sys.stderr = f
    try:
        print("Main start")
        main()
    finally:
        sys.stdout = original_stdout
        sys.stderr = original_stderr
        f.close()
