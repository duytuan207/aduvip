#!/usr/bin/python
# coding:utf-8

import os
import config
import time

TOKEN = config.TOKEN
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def bot_start(massage):
	bot.send_chat_action(message.chat.id, 'typing')
    bot.send_message(message.chat.id, '欢迎~我可以为你监控服务器在线状态哟 戳 /help 查看帮助！')

@bot.message_handler(commands=['help'])
def bot_help(message):
    bot.send_chat_action(message.chat.id, 'typing')
    bot.send_message(message.chat.id,'我能帮你监控服务器状态哟 \n /add 添加服务器 \n /del 删除服务器 \n /status 查看当前状态')

@bot.message_handler(commands=['add'])
def bot_add(message):
    un = message.from_user.username
    f = open('admin', 'r')
    l = f.read()
    if l.find('%s' %un) == -1:
        bot.reply_to(message,'为了保护隐私，本bot仅限个人使用')
    else:


@bot.message_handler(commands=['del'])
def bot_add(message):
    un = message.from_user.username
    f = open('admin', 'r')
    l = f.read()
    if l.find('%s' %un) == -1:
        bot.reply_to(message,'为了保护隐私，本bot仅限个人使用')
    else:
        f = open("db.py")  
        all_lines = f.readlines()  
        for address in all_lines:  
            markup.add(types.InlineKeyboardButton("%s" % button,callback_data='%s' % (button)))
            bot.send_message(message.chat.id, "要删除哪个服务器咧？", reply_markup=markup)
            file_obj.close()

@bot.message_handler(commands=['list'])
def bot_add(message):
    un = message.from_user.username
    f = open('admin', 'r')
    l = f.read()
    if l.find('%s' %un) == -1:
        bot.reply_to(message,'为了保护隐私，本bot仅限个人使用')
    else:



bot.polling(none_stop=True