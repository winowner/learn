#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime
import os

<<<<<<< HEAD
pwd = os.path.abspath('.')

=======
# pwd = os.path.abspath('.')
pwd = 'D:\soft'
>>>>>>> 1b5da070f37b3b89e5284eca3d43aa8f4297b1fe
print('      Size     Last Modified  Name')
print('------------------------------------------------------------')

for f in os.listdir(pwd):
    fsize = os.path.getsize(f)
    mtime = datetime.fromtimestamp(os.path.getmtime(f)).strftime('%Y-%m-%d %H:%M')
    flag = '/' if os.path.isdir(f) else ''
    print('%10d  %s  %s%s' % (fsize, mtime, f, flag))
