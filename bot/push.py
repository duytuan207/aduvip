#!/usr/bin/python
# coding:utf-8

import os
import config
import time
import telebot
import ping

TOKEN = config.TOKENP
bot = telebot.TeleBot(TOKEN)

fs = open("chatid",'r')
id = fs.read()
fs.close()
f = open("db.py",'r')
s = f.readlines()
for ip in s:
    r = ping.check_ip_ping(ip)
    if r == 0:
        pass
    elif r == 1:
        bot.send_chat_action(message.chat.id,'typing')
        bot.send_message(id,u'⚠⚠ %s 异常'%ip)
    else:
        bot.send_message(message.chat.id,'Error')
f.close()
os._exit()


