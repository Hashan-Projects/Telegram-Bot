#Created By @2021-Hashan Dimuthu All Right Reserved

import os
import telebot

API_KEY = os.getenv('API_KEY')
bot = telebot.Telebot(API_KEY)

@bot.message_handler(commands=['start'])
def great(message):
    bot.reply_to(message, "𝓨𝓮𝓼 𝓘 𝓪𝓶 𝓗𝓮𝓻𝓮 /n/n")

@bot.message_handler(commands=['hello'])
def hello(message):
    bot.send_message(message.chat.id, "𝓗𝓮𝓵𝓵𝓸 𝓗𝓸𝔀 𝓪𝓻𝓮 𝔂𝓸𝓾?")

@bot.message_handler(commands=[''])
def (message):

bot.polling()
