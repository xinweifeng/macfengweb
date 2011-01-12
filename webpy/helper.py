#!/usr/bin/python
import sys, os
abspath = os.path.dirname(__file__)
sys.path.append(abspath)
os.chdir(abspath)
import time

ISOTIMEFORMAT = '%Y-%m-%d %X'

def now():
    return time.localtime(time.time())

def now_str():
    return time.strftime(ISOTIMEFORMAT,now())
    
def is_int(uchar):
    try:
        int(uchar)
        return True
    except:
        return False
