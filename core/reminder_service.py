# core/reminder_service.py

import requests

# Replace with your actual bot token and chat ID
TELEGRAM_BOT_TOKEN = 'your-telegram-bot-token'
CHAT_ID = 'your-chat-id'

# Send a message to Telegram

def send_reminder(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': CHAT_ID,
        'text': message
    }
    response = requests.post(url, data=payload)
    return response.status_code == 200
