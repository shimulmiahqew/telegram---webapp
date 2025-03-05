import os
from flask import Flask
from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, CallbackContext, Dispatcher
from dotenv import load_dotenv

# Load Environment
load_dotenv()
TOKEN = os.getenv("7732391797:AAE2588vDmx0umob1fObZaKtYDA6H_UIwbg"
                 )

app = Flask(Money-Airdrop)
bot = Bot("7732391797:AAE2588vDmx0umob1fObZaKtYDA6H_UIwbg"
         )

@app.route('/')
def home():
    return "✅ Bot is Live!"

def start(update: Update, context: CallbackContext):
    update.message.reply_text("🎁 Welcome to USDT Giveaway Bot!")

def setup_dispatcher():
    dispatcher = Dispatcher(bot, None, workers=0)
    dispatcher.add_handler(CommandHandler("start", start))
    return dispatcher

@app.route('/webhook', methods=["POST"])
def webhook():
    dispatcher = setup_dispatcher()
    dispatcher.process_update(Update.de_json(bot.get_updates()[0], bot))
    return "Webhook Received!"

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

                     
                     
                
