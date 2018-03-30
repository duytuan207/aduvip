#!/usr/bin/python
# coding:utf-8

import os

def add_server(ip):   
    if l.find('%s' %ip) == -1:
            f = open('db.py', 'a+w')
            r = ip
            print >> f, r
            f.close()
            return  '成功添加监控~'
        else:
            return  '添加失败：不可重复添加'
      
def del_server(ip):
    f = open("db.py",'a+w')
    all_lines = f.readlines()  
    for address in all_lines:  
        markup.add(types.InlineKeyboardButton("%s" % button,callback_data='%s' % (button)))
        bot.send_message(message.chat.id, "要删除哪个服务器咧？", reply_markup=markup)
        with open(out_file, 'w') as f:
            f.write(''.join([line for line in open(in_file).readlines() if 'call.data' not in line]))
            file_obj.close()
            return 'done'
	