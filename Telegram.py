import telebot
import re

tomeRange = 1 , 2 , 3 , 4 , 5 , 6

# Replace with your own Telegram bot token
bot = telebot.TeleBot("1793841737:AAFFzzD2LkBuW1kg0aNq7dKLYNHuAy1BHP4")

# Replace with your own Telegram chat ID
chat_id = "301795147"


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(chat_id, 'Hello this is a test for the telegrambot running on my raspberry pi')
    
@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(chat_id, 'second test for raspberry pi hosted bot lel')
    
@bot.message_handler(content_types=['text'])
def start_Tome(message):
    if message.text == '/startTome':
        msg = bot.send_message(chat_id, 'Please provide which tome to start with')
        bot.register_next_step_handler(msg, whichTome)
        
def whichTome(message):
    if int(message.text) in tomeRange:
        value = int(message.text)
        bot.send_message(chat_id, f'You have entered {value}')
    

# Start the bot
bot.polling()