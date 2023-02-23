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
    
@bot.message_handler(commands=['startTome'])
def start_Tome(msg):
    bot.send_message(chat_id, 'please enter a number after /startTome')
    
@bot.callback_query_handler(func = lambda call: True)
def callback_query(call):
    if call.data.startswith('/startTome_'):
        value = call.data.split('_')[1]
        bot.send_message(chat_id, f'You have entered {value}')

# Start the bot
bot.polling()