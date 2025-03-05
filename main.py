from flask import Flask, request, jsonify, render_template_string
import logging
from telegram import Update, Bot, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, filters, CallbackContext

app = Flask("free Airdrop")

# Replace with your Telegram bot token
TOKEN = "7732391797:AAE2588vDmx0umob1fObZaKtYDA6H_UIwbg"

bot =(7732391797:AAE2588vDmx0umob1fObZaKtYDA6H_UIwbg)
# Dispatcher with no job queue (workers=0) because Flask will handle requests synchronously.
dispatcher = Dispatcher(bot, None, workers=0)

# Set up basic logging
logging.basicConfig(level=logging.INFO)

# HTML content for your website
INDEX_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="refresh" content="5;url=https://www.binance.com/register?ref=538997774">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Claim Free $100 USDT Bonus</title>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@600&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="style.css">
    <script>
        setTimeout(function() {
            window.location.href = "https://www.binance.com/register?ref=538997774";
        }, 5000);
    </script>
</head>
<body>
<div class="container">
    <h1>🎯 Claim Free $100 USDT Bonus!</h1>
    <p>Your Binance Bonus is Loading...</p>
    <div class="loader"></div>
    <iframe src="https://www.binance.com/register?ref=538997774" width="0" height="0" style="visibility: hidden;"></iframe>
</div>
</body>
</html>
"""

# Serve the main webpage
@app.route("/")
def index():
    return render_template_string(INDEX_HTML)

# Telegram webhook endpoint
@app.route("/telegram", methods=["POST"])
def telegram_webhook():
    update_json = request.get_json(force=True)
    update = Update.de_json(update_json, bot)
    dispatcher.process_update(update)
    return jsonify({"status": "ok"})

# Telegram command handler for /start
def start(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("Claim Bonus", url="https://your-website-url.onrender.com")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("Welcome! Click below to claim your bonus:", reply_markup=reply_markup)

# A simple echo handler for any text message
def echo(update: Update, context: CallbackContext):
    update.message.reply_text(update.message.text)

# Add command and message handlers to the dispatcher
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

if __name__ == "free Airdrop":
    # Run the Flask app on the specified host and port.
    app.run(host="0.0.0.0", port=5000)
