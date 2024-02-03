#After main is called, you could launch index.html in your browser to chat with the bot.

# main.py
from ragchatbot.api import start_api_server
from ragchatbot.utils import setup_logging
import ragchatbot.config as config

def main():
    # This sets up logging as configured in logging.json
    setup_logging()
    # Start the API server
    start_api_server()

if __name__ == "__main__":
    main()