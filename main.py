import os
import telebot

API_KEY = os.getenv('API_KEY')
bot = telebot.Telebot(API_KEY)

@bot.message_handler(commands=['start'])
def great(message):
    bot.reply_to(message, "Yes I am Here")

@bot.message_handler(commands=['hello'])
def hello(message):
    bot.send_message(message.chat.id, "Hello How are you?")

bot.polling()