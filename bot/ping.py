#!/usr/bin/python
# coding:utf-8

import pyping

def check_ip_ping(ip):
    r = pyping.ping('ip')
    if r.ret_code == 0:
        r = '%s online'%ip
        return r
    else:
        r = '⚠%s offline⚠'%ip
        return r
    