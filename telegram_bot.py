from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import requests

# Telegram Bot Token
TELEGRAM_BOT_TOKEN = "7557926778:AAH74UZc7JB5KSa0tJWRjqlBDlFDeEruog8"

# Middleware URL
MIDDLEWARE_URL = "https://your-render-app.onrender.com/command"

# Start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot is up and running! Send commands to interact.")

# Command handler for sending commands
async def send_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    command = ' '.join(context.args)
    if command:
        response = requests.post(MIDDLEWARE_URL, json={"command": command})
        await update.message.reply_text(f"Command sent successfully: {response.text}")
    else:
        await update.message.reply_text("Please provide a command after /cmd")

# Function to start the bot
def start_bot():
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    # Add command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("cmd", send_command))

    # Run the bot
    application.run_polling()
