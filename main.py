#Created By @2021-Hashan Dimuthu All Right Reserved

import os
import telebot

API_KEY = os.getenv('API_KEY')
bot = telebot.Telebot(API_KEY)

#start 
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "𝓗𝓮𝓵𝓵𝓸 𝓘 𝓪𝓶 𝓗𝓪𝓼𝓱𝓪𝓷 𝓓𝓲𝓶𝓾𝓽𝓱𝓾'𝓼 𝓒𝓱𝓪𝓽 𝓑𝓸𝓽 :) \n\n 𝓢𝓸𝓶𝓮 𝓒𝓸𝓶𝓶𝓪𝓷𝓭𝓼 𝓪𝓻𝓮 𝔂𝓸𝓾 𝓬𝓪𝓷 𝓰𝓮𝓽 𝓲𝓷 𝓽𝓱𝓲𝓼 𝓬𝓸𝓶𝓶𝓪𝓷𝓭 /help")
    
#help
@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message, "𝓐𝓿𝓵𝓲𝓪𝓫𝓵𝓮 𝓒𝓸𝓶𝓶𝓪𝓷𝓭𝓼 𝓪𝓻𝓮 𝓱𝓮𝓻𝓮 \n\n 𝓕𝓸𝓻 𝓼𝓽𝓪𝓻𝓽 𝓽𝓱𝓲𝓼 𝓫𝓸𝓽 : /start \n\n  𝓕𝓸𝓻 𝓯𝓲𝓷𝓭 𝓜𝔂 𝓖𝓲𝓽𝓱𝓾𝓫 : /github \n\n 𝓕𝓸𝓻 𝓯𝓲𝓷𝓭 𝓜𝔂 𝓣𝓮𝓵𝓮𝓰𝓻𝓪𝓶 : /telegram \n\n 𝓕𝓸𝓻 𝓯𝓲𝓷𝓭 𝓜𝔂 𝔂𝓸𝓾𝓽𝓾𝓫𝓮 : /youtube \n\n ")
 
#hello
@bot.message_handler(commands=['hello'])
def hello(message):
    bot.send_message(message.chat.id, "𝓗𝓮𝓵𝓵𝓸 𝓗𝓸𝔀 𝓪𝓻𝓮 𝔂𝓸𝓾?")

#github
@bot.message_handler(commands=['github'])
def github(message):
    bot.send_message(message.chat.id, "https://github.com/HashanDimuthu")
    
#youtube
@bot.message_handler(commands=['youtube'])
def youtube(message):
    bot.send_message(message.chat.id, "https://www.youtube.com/channel/UCMb9Rcf7mh71x9glgb5oR8A")

#telegram    
@bot.message_handler(commands=['telegram'])
def telegram(message):
    bot.send_message(message.chat.id, "@HashanDimuthu")

bot.polling()
