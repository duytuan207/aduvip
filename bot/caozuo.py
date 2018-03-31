#!/usr/bin/python
# coding:utf-8

import os
import shutil

def add_server(ip): 
    f= open("db.py",'a+w')
    l = f.read()
    if l.find('%s' %ip) == -1:
        f = open('db.py', 'a+w')
        r = ip
        print >> f, r
        f.close()
        return  '成功添加监控~'
    else:
        return  '添加失败：不可重复添加'
      
def del_server(ip):
    with open('db.py','r') as f:
        with open('db.new', 'w') as g:
            for line in f.readlines():
                if ip not in line:             
                    g.write(line)
    shutil.move('db.new', 'db.py')
    return 'done'