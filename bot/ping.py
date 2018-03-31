#!/usr/bin/python
# coding:utf-8

import subprocess
import os,time,sys,re
 
def check_ip_ping(ip):
    p = subprocess.Popen(["ping -c 1 -i 0.2 -W 3 "+ ip],stdin = subprocess.PIPE,stdout = subprocess.PIPE,stderr = subprocess.PIPE,shell = True)
    out = p.stdout.read()
    regex = re.compile("time=\d*", re.IGNORECASE | re.MULTILINE)
    if len(regex.findall(out)) > 0:
        return 0
    else:
        return 1