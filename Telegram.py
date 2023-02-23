import telebot
import re

# Replace with your own Telegram bot token
bot = telebot.TeleBot("1793841737:AAFFzzD2LkBuW1kg0aNq7dKLYNHuAy1BHP4")

# Replace with your own Telegram chat ID
chat_id = "301795147"


@bot.message_handler(commands=['start'])
def start_message(msg):
    bot.send_message(chat_id, 'Hello this is a test for the telegrambot running on my raspberry pi')
    
@bot.message_handler(commands=['help'])
def help_message(msg):
    bot.send_message(chat_id, 'second test for raspberry pi hosted bot lel')
    
@bot.message_handler(commands=['count'])
def count_message(msg):
    param = re.search(r'/count (\d+)', msg.txt)
    if param:
        value = param.group(1)
        bot.send_message(chat_id, f'You have entered {value}')

# Start the bot
bot.polling()