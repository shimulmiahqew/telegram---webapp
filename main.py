import logging
import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Get the Telegram bot token from environment variables
TOKEN = os.getenv("7732391797:AAE2588vDmx0umob1fObZaKtYDA6H_UIwbg")

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Function to handle /start command
def start(update: Update, context: CallbackContext):
    update.message.reply_text('Hello! I am your Telegram bot.')

# Main function to start the bot
def main():
    # Create an Updater object and pass the bot token
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Add the command handler to the dispatcher
    dispatcher.add_handler(CommandHandler('start', start))

    # Start polling for updates from Telegram
    updater.start_polling()

    # Keep the bot running
    updater.idle()

if __name__ == '__main__':
    main()
