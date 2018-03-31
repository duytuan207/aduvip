#!/usr/bin/python
# coding:utf-8

import os
import config
import caozuo
import time
import telebot
from telebot import types

TOKEN = config.TOKENM
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def bot_start(message):
    bot.send_chat_action(message.chat.id, 'typing')
    bot.send_message(message.chat.id, '欢迎~我可以为你监控服务器在线状态哟 戳 /help 查看帮助！')

@bot.message_handler(commands=['help'])
def bot_help(message):
    bot.send_chat_action(message.chat.id, 'typing')
    bot.send_message(message.chat.id,'我能帮你监控服务器状态哟 \n /add 添加服务器 \n /del 删除服务器 \n /list 查看服务器列表 \n /test 查询在线情况')

@bot.message_handler(commands=['add'])
def bot_add(message):
    un = message.from_user.username
    f = open('admin', 'r')
    l = f.read()
    if l.find('%s' %un) == -1:
        bot.reply_to(message,'为了保护隐私，本bot仅限个人使用')
    else:
        if len(message.text.split(' ')) == 2:
            r = caozuo.add_server(message.text.split(' ')[1])
            bot.send_chat_action(message.chat.id,'typing')
            bot.send_message(message.chat.id,r)
        else:
            bot.send_chat_action(message.chat.id,'参数错误')

@bot.message_handler(commands=['del'])
def bot_del(message):
    un = message.from_user.username
    f = open('admin', 'r')
    l = f.read()
    if l.find('%s' %un) == -1:
        bot.reply_to(message,'为了保护隐私，本bot仅限个人使用')
    else:
        if len(message.text.split(' ')) == 2:
            r = caozuo.del_server(message.text.split(' ')[1])
            bot.send_chat_action(message.chat.id,'typing')
            bot.send_message(message.chat.id,r)
        else:
            bot.send_chat_action(message.chat.id,'参数错误')

@bot.message_handler(commands=['list'])
def bot_list(message):
    un = message.from_user.username
    f = open('admin', 'r')
    l = f.read()
    if l.find('%s' %un) == -1:
        bot.reply_to(message,'为了保护隐私，本bot仅限个人使用')
    else:
        f = open("db.py",'r')
        s = f.read()
        bot.send_chat_action(message.chat.id,'typing')
        bot.send_message(message.chat.id,'监控列表： \n%s'%s)
        f.close()
        
@bot.message_handler(commands=['test'])
def bot_test(message):
    un = message.from_user.username
    f = open('admin', 'r')
    l = f.read()
    if l.find('%s' %un) == -1:
        bot.reply_to(message,'为了保护隐私，本bot仅限个人使用')
    else:
        f = open("db.py",'r')
        s = f.readlines()
        for ip in s:
            r = ping.check_ip_ping(ip)
            bot.send_chat_action(message.chat.id,'typing')
            bot.send_message(message.chat.id,r)
        f.close()

@bot.message_handler(commands=['link'])
def bot_link(message):
    un = message.from_user.username
    f = open('admin', 'r')
    l = f.read()
    if l.find('%s' %un) == -1:
        bot.reply_to(message,'为了保护隐私，本bot仅限个人使用')
    else:
        id = message.chat.id
        f = open('chatid','a+w')
        print >> f,id
        f.close()
        bot.send_message(message.chat.id,'绑定完成')

bot.polling()