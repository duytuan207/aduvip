#!/usr/bin/python
# coding:utf-8

import os
import time
import config
import caozuo
import telebot
import ping
from apscheduler.schedulers.background import BackgroundScheduler

TOKEN = config.TOKEN
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def bot_start(message):
    bot.send_chat_action(message.chat.id, 'typing')
    bot.send_message(message.chat.id, '欢迎~我可以为你监控服务器在线状态哟 戳 /help 查看帮助！首次使用请戳 /setup')

@bot.message_handler(commands=['help'])
def bot_help(message):
    bot.send_chat_action(message.chat.id, 'typing')
    bot.send_message(message.chat.id,'我能帮你监控服务器状态哟 \n /add 添加服务器 \n /del 删除服务器 \n /list 查看服务器列表 \n /test 查询在线情况')

@bot.message_handler(commands=['add'])
def bot_add(message):
    un = message.from_user.id
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
    un = message.from_user.id
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
    un = message.from_user.id
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
    un = message.from_user.id
    f = open('admin', 'r')
    l = f.read()
    if l.find('%s' %un) == -1:
        bot.reply_to(message,'为了保护隐私，本bot仅限个人使用')
    else:
        f = open("db.py",'r')
        s = f.readlines()
        for ip in s:
            r = ping.check_ip_ping(ip)
            if r == 0:
                bot.send_chat_action(message.chat.id,'typing')
                bot.send_message(message.chat.id,u'%s 正常'%ip)
            elif r == 1:
                bot.send_chat_action(message.chat.id,'typing')
                bot.send_message(message.chat.id,u'⚠⚠ %s 异常'%ip)
            else:
                bot.send_message(message.chat.id,'Error')
        f.close()

@bot.message_handler(commands=['setup'])
def bot_lock(message):
	r = os.path.exists('admin')
	rdb = os.path.exists('db.py')
	if r == False:
		os.mknod("admin")
		bot.send_message(message.chat.id,'已创建绑定id')
	else:
		pass
		bot.send_message(message.chat.id,'绑定id已存在，pass')
	if rdb == False:
		os.mknod("db.py")
		bot.send_message(message.chat.id,'已创建ip库')
	else:
		pass
		bot.send_message(message.chat.id,'ip库文件已存在，pass')
	msg_id = bot.send_message(message.chat.id,'绑定用户id…').message_id
	uid = message.from_user.id
	f = open("admin",'w')
	i = uid
	print >> f,i
	f.close()
	bot.edit_message_text('绑定完成！', message.chat.id, msg_id)
	time.sleep(5)
	bot.edit_message_text('配置完成~', message.chat.id, msg_id)

def bot_warn():
    fs = open("admin",'r')
    id = fs.read()
    f = open("db.py",'r')
    s = f.readlines()
    for ip in s:
        r = ping.check_ip_ping(ip)
        if r == 0:
            pass
        elif r == 1:
            bot.send_chat_action(id,'typing')
            bot.send_message(id,u'[PUSH]⚠⚠警报 ⚠⚠ \n%s 出现异常 \n本警报由bot自动发出，可能受限于服务器环境而出现误报'%ip)
        else:
            bot.send_message(message.chat.id,'Error:未知错误，请向 @johnpoint 反应')
    f.close()

if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    scheduler.add_job(bot_warn,'interval', minutes=1)
    scheduler.start()
    bot.polling()