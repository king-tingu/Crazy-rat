from flask import Flask, request
import requests
import telegram_bot  # Import the bot script

app = Flask(__name__)

# Telegram bot logic
telegram_bot.start_bot()  # Function to start the bot

@app.route('/payload', methods=['POST'])
def handle_payload():
    data = request.json
    print(f"Payload Data: {data}")
    message = f"Received payload data: {data}"
    send_telegram_message(message)
    return "Data received", 200

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{telegram_bot.TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": telegram_bot.TELEGRAM_CHAT_ID,
        "text": message
    }
    requests.post(url, json=payload)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
