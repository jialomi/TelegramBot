import telebot
import openai

# Replace with your own Telegram bot token
bot = telebot.TeleBot("1793841737:AAFFzzD2LkBuW1kg0aNq7dKLYNHuAy1BHP4")

# Replace with your own Telegram chat ID
#chat_id = "301795147"

# Set up the OpenAI API
openai.api_key = "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"
# Define a function to handle incoming messages
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    # Use the OpenAI API to generate a response to the message
    response = openai.Completion.create(
        engine="davinci",
        prompt=message.text,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
    )
    
    # Send the response back to the user
    bot.reply_to(message, response.choices[0].text)

# Start the bot
bot.polling()