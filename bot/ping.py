#!/usr/bin/python
# coding:utf-8

import subprocess
import shlex
 
def check_ip_ping(ip):
    cmd = 'ping -c 1' + ip
    args = shlex.split(cmd)
    try:
	    subprocess.check_call(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	    return 0
    except subprocess.CalledProcessError:
        return 1