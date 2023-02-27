import telebot

tomeRange = ['1' , '2' , '3' , '4' , '5' , '6']
apiKey = '1793841737:AAFFzzD2LkBuW1kg0aNq7dKLYNHuAy1BHP4'
# Replace with your own Telegram bot token
bot = telebot.TeleBot(apiKey)

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

    if message.text == 'hi':
        bot.send_message(chat_id, 'Hello this is a test commit for replit')
        
    if message.text == 'im hungry':
        msg1 = bot.send_message(chat_id, 'Please go get something to eat, If you want me to recommend you something please type in continue, if not type cancel.')
        bot.register_next_step_handler(msg1, suggestFood)
        
def whichTome(message):
    if message.text in tomeRange:
        value = int(message.text)
        bot.send_message(chat_id, f'You have entered {value}')
    elif message.text == 'cancel':
        bot.send_message(chat_id, 'Command cancelled')
    else:
        value = message.text
        msg = bot.send_message(chat_id, f'Please eneter a valid tome number, [{value}] is not a valid tome number')
        bot.register_next_step_handler(msg, whichTome)
        
    msg = message.text.lower()
    if 'hungry' in msg:
        msg1 = bot.send_message(chat_id, 'Please go get something to eat, If you want me to recommend you something please type in continue, if not type cancel.')
        bot.register_next_step_handler(msg1, suggestFood)
        
def suggestFood(message):
    if 'continue' in message.text:
        bot.send_message(chat_id, 'You usually like to eat, aglio olio, ramen, fried rice, or thai food')
    elif 'cancel' in message.text:
        bot.send_message(chat_id, 'alright then, I hope you find something to eat soon, please do not let yourself starve.')
    else:
        msg2 = bot.send_message(chat_id, 'Invalid response, please reply either continue, or cancel')
        bot.register_next_step_handler(msg2, suggestFood)
    
    

# Start the bot
bot.polling()