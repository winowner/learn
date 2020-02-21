#!/usr/bin/env python3
# -*- coding: utf-8 -*-

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

print('L[0:3] =', L[0:3])
print('L[:3] =', L[:3])
print('L[1:3] =', L[1:3])
print('L[-2:] =', L[-2:])

R = list(range(100))
print('R[:10] =', R[:10])
print('R[-10:] =', R[-10:])
print('R[10:20] =', R[10:20])
print('R[:10:2] =', R[:10:2])
print('R[::5] =', R[::5])
<<<<<<< HEAD

def trim(s):
    b = len(s) - 1
    a = ''
    for x in s:
        if x == ' ':
           continue
        a = a + x
    print(a)
    return a

trim("  123 456   ")

str1 = '    sssds '


def strim(st):
    if st[:1] == ' ':
        return strim(st[1:])
    elif st[-1:] == ' ':
        return strim(st[:-1])
    else:
        return st

s = trim(str1)
print('原字符串%s,去空格后为%s,新长度:%s' %(str1,s,len(s)) )
=======
>>>>>>> 1b5da070f37b3b89e5284eca3d43aa8f4297b1fe
