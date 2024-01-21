#After main is called, you could launch index.html in your browser to chat with the bot.

# main.py
import sys
import logging
from ragchatbot.api import start_api_server
from ragchatbot.utils import load_configuration

def main():
    # Parse command line arguments
    config = load_configuration('config.json')
    main_model = config.get('main_model')
    sub_model = config.get('sub_model')

    # Load configuration
    config = load_configuration('./config.json')
    
    # Start the API server
    start_api_server(config)

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)
    # Open a file for writing
    f = open('output_log', 'w')
    original_stdout = sys.stdout  # Save the original sys.stdout
    original_stderr = sys.stderr  # Save the original sys.stderr
    sys.stdout = f
    sys.stderr = f
    try:
        print("Main start")
        main()
    finally:
        sys.stdout = original_stdout
        sys.stderr = original_stderr
        f.close()
