#After main is called, you could launch index.html in your browser to chat with the bot.
#run "bash standalone_embed.sh start" in milvus folder to start milvus server before run main.py
# main.py
from ragchatbot.api import start_api_server
from ragchatbot.initializer import initialize

def main():
    # Initialization
    initialize()
    # Start knowledge base preparation
    
    # Start the API server
    # start_api_server()

if __name__ == "__main__":
    main()