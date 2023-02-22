import telebot

# Replace with your own Telegram bot token
bot = telebot.TeleBot("1793841737:AAFFzzD2LkBuW1kg0aNq7dKLYNHuAy1BHP4")

# Replace with your own Telegram chat ID
chat_id = "301795147"

@bot.message_handler(commands=['start'])
def start_message(msg):
    bot.send_message(chat_id, 'Test bot for heroku started up')
    
@bot.message_handler(commands=['test'])
def test_message(msg):
    bot.send_message(chat_id, 'Helps me please')
    bot.send_message(chat_id, 'Test again lel forgot sixth commit')

bot.polling()