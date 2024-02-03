#After main is called, you could launch index.html in your browser to chat with the bot.

# main.py
from ragchatbot.api import start_api_server
from ragchatbot.utils import load_configuration

def main():
    # Load configuration
    config = load_configuration('./config.json')
    
    # Start the API server
    start_api_server(config)

if __name__ == "__main__":
    
    try:
        print("Main start")
        main()
    finally:
        sys.stdout = original_stdout
        sys.stderr = original_stderr
        f.close()
