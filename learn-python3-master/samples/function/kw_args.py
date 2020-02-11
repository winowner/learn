#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def print_scores(**kw):
    print('      Name  Score')
    print('------------------')
    for name, score in kw.items():
        print('%10s  %d' % (name, score))
    print()

print_scores(Adam=99, Lisa=88, Bart=77)

data = {
    'Adam Lee': 99,
    'Lisa S': 88,
    'F.Bart': 77
}

print_scores(**data)

<<<<<<< HEAD
def print_info(name, height=180, *, gender, city='Beijing', age):
    print('Personal Info')
    print('---------------')
    print('   Name: %s' % name)
    print(' Height: %s' % height)
=======
def print_info(name, *, gender, city='Beijing', age):
    print('Personal Info')
    print('---------------')
    print('   Name: %s' % name)
>>>>>>> 1b5da070f37b3b89e5284eca3d43aa8f4297b1fe
    print(' Gender: %s' % gender)
    print('   City: %s' % city)
    print('    Age: %s' % age)
    print()

print_info('Bob', gender='male', age=20)
print_info('Lisa', gender='female', city='Shanghai', age=18)
<<<<<<< HEAD

print_info('clc', age='10', gender='male')
=======
>>>>>>> 1b5da070f37b3b89e5284eca3d43aa8f4297b1fe
