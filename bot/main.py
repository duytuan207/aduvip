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
    bot.send_message(message.chat.id, 'Chào mừng~ Tôi có thể theo dõi trạng thái trực tuyến của máy chủ cho bạn. Nhấp vào /help để xem trợ giúp!  Vui lòng nhấp vào /setup để sử dụng lần đầu tiên')

@bot.message_handler(commands=['help'])
def bot_help(message):
    bot.send_chat_action(message.chat.id, 'typing')
    bot.send_message(message.chat.id,'Tôi có thể giúp bạn theo dõi trạng thái máy chủ \n /add Thêm máy chủ \n /del Xóa máy chủ \n /list Xem danh sách máy chủ \n /test Kiểm tra trạng thái trực tuyến')

@bot.message_handler(commands=['add'])
def bot_add(message):
    un = message.from_user.id
    f = open('admin', 'r')
    l = f.read()
    if l.find('%s' %un) == -1:
        bot.reply_to(message,'Để bảo vệ quyền riêng tư, bot này chỉ được giới hạn cho mục đích sử dụng cá nhân')
    else:
        if len(message.text.split(' ')) == 2:
            r = caozuo.add_server(message.text.split(' ')[1])
            bot.send_chat_action(message.chat.id,'typing')
            bot.send_message(message.chat.id,r)
        else:
            bot.send_chat_action(message.chat.id,'Lỗi tham số')

@bot.message_handler(commands=['del'])
def bot_del(message):
    un = message.from_user.id
    f = open('admin', 'r')
    l = f.read()
    if l.find('%s' %un) == -1:
        bot.reply_to(message,'Để bảo vệ quyền riêng tư, bot này chỉ được giới hạn cho mục đích sử dụng cá nhân')
    else:
        if len(message.text.split(' ')) == 2:
            r = caozuo.del_server(message.text.split(' ')[1])
            bot.send_chat_action(message.chat.id,'typing')
            bot.send_message(message.chat.id,r)
        else:
            bot.send_chat_action(message.chat.id,'Lỗi tham số')

@bot.message_handler(commands=['list'])
def bot_list(message):
    un = message.from_user.id
    f = open('admin', 'r')
    l = f.read()
    if l.find('%s' %un) == -1:
        bot.reply_to(message,'Để bảo vệ quyền riêng tư, bot này chỉ được giới hạn cho mục đích sử dụng cá nhân')
    else:
        f = open("db.py",'r')
        s = f.read()
        bot.send_chat_action(message.chat.id,'typing')
        bot.send_message(message.chat.id,'Danh sách giám sát： \n%s'%s)
        f.close()
        
@bot.message_handler(commands=['test'])
def bot_test(message):
    un = message.from_user.id
    f = open('admin', 'r')
    l = f.read()
    if l.find('%s' %un) == -1:
        bot.reply_to(message,'Để bảo vệ quyền riêng tư, bot này chỉ được giới hạn cho mục đích sử dụng cá nhân')
    else:
        f = open("db.py",'r')
        s = f.readlines()
        for ip in s:
            r = ping.check_ip_ping(ip)
            if r == 0:
                bot.send_chat_action(message.chat.id,'typing')
                bot.send_message(message.chat.id,u'%s Bình thường'%ip)
            elif r == 1:
                bot.send_chat_action(message.chat.id,'typing')
                bot.send_message(message.chat.id,u'⚠⚠ %s Bất thường'%ip)
            else:
                bot.send_message(message.chat.id,'Error')
        f.close()

@bot.message_handler(commands=['setup'])
def bot_lock(message):
	r = os.path.exists('admin')
	rdb = os.path.exists('db.py')
	if r == False:
	    if r == False:
		    os.mknod("admin")
		    bot.send_message(message.chat.id,'Id ràng buộc đã được tạo')
	    else:
		    pass
		    bot.send_message(message.chat.id,'Id liên kết đã tồn tại，pass')
	    if rdb == False:
		    os.mknod("db.py")
		    bot.send_message(message.chat.id,'Thư viện IP đã được tạo')
	    else:
		    pass
		    bot.send_message(message.chat.id,'Tệp thư viện ip đã tồn tại，pass')
	    msg_id = bot.send_message(message.chat.id,'Liên kết id người dùng…').message_id
	    uid = message.from_user.id
	    f = open("admin",'w')
	    i = uid
	    print >> f,i
	    f.close()
	    bot.edit_message_text('Ràng buộc hoàn thành！', message.chat.id, msg_id)
	    time.sleep(10)
	    bot.edit_message_text('Cấu hình hoàn tất~', message.chat.id, msg_id)
	else:
		bot.send_message(message.chat.id,'Đã bị ràng buộc！？')

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
            bot.send_message(id,u'[PUSH]⚠⚠警报 ⚠⚠ \n%s 出现异常 \n**Cảnh báo này được bot tự động đưa ra**'%ip)
        else:
            bot.send_message(message.chat.id,'Error:Lỗi không xác định, xin vui lòng hỏi facebook.com/ndtdzhuhu')
    f.close()

if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    scheduler.add_job(bot_warn,'interval', minutes=1)
    scheduler.start()
    bot.polling()
