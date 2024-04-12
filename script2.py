from telegram import Bot
from flask import Flask, request

# Initialize Flask app
app = Flask(__name__)

# Your Telegram Bot Token
TOKEN = '7146222220:AAFvvXi5HLiyKneyL55KU9XOo1LAN1QLSDo'

# Initialize Telegram Bot
bot = Bot(token=TOKEN)

# Group chat ID where you want to send messages
GROUP_CHAT_ID = '1002013774317'

@app.route('/send-message', methods=['POST'])
def send_message():
    # Get form data
    message = request.form.get('message')

    # Send message to group chat
    bot.send_message(chat_id=GROUP_CHAT_ID, text=message)

    return 'Message sent successfully!'

if __name__ == '__main__':
    app.run(debug=True)
