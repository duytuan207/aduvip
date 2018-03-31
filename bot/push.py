#!/usr/bin/python
# coding:utf-8

import os
import config
import caozuo
import time
import telebot
from telebot import types

TOKEN = config.TOKENP
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def bot_start(message):
    bot.send_chat_action(message.chat.id, 'typing')
    bot.send_message(message.chat.id, '欢迎~我可以为你监控服务器在线状态哟 戳 /help 查看帮助！')
