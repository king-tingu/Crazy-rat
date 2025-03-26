from telegram.ext import Updater, CommandHandler
import requests

# Telegram Bot Token
TELEGRAM_BOT_TOKEN = "7557926778:AAH74UZc7JB5KSa0tJWRjqlBDlFDeEruog8"

# Define the function to start the bot
def start_bot():
    updater = Updater(TELEGRAM_BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    def start(update, context):
        update.message.reply_text("Bot is up and running! Send commands to interact.")

    def send_command(update, context):
        command = ' '.join(context.args)
        update.message.reply_text(f"Received command: {command}")

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("cmd", send_command))

    # Start polling
    updater.start_polling()
    updater.idle()

