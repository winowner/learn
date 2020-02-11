# -*- coding: utf-8 -*-
import os

def Find_file(dir, sname):
    sname = sname.lower()
    for f in os.listdir(dir):
        f = os.path.join(dir, f)
        if sname in f.lower() and os.path.isfile(f):
            print(f)
        elif os.path.isdir(f):
            Find_file(f, sname)

#打印含有字符串的文件名以及相抵路径
Find_file('F:\pyse_workspace','READ') 