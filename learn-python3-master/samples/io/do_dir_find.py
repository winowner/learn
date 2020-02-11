#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re, os
'''
编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径。
'''

def main():
    # 定义搜索关键字
    key_word = input('Please input the file name to search: ')

    # 列出当前目录下所有文件夹
    dir_list = [f for f in os.listdir('.') if os.path.isdir(f)]
    # 获得当前目录绝对地址
    dir_path_list = [os.path.abspath('.')]

    # 初始化文件夹地址的拷贝，用于比较
    dir_path_list_1 = []
    # 初始化结果列表
    result = []

    # 比较关键词与地址是否匹配并添加到列表result中
    def compare(dir, path):
        pattern = re.compile(key_word.lower())
        if pattern.search(dir.lower()):
            result.append(path)

    for dir_path in dir_path_list:
        # 获得一级文件夹下的文件列表
        f_list_0 = [f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))]
        for f in f_list_0:
            temp_f_path = os.path.join(dir_path, f)
            # 比较关键字与文件名
            compare(os.path.split(temp_f_path)[1], temp_f_path)

    # 当上一个文件夹地址与最新文件夹地址不同时（有新地址加入）持续循环
    while dir_path_list_1 != dir_path_list:
        # 拷贝文件夹地址
        dir_path_list_1 = dir_path_list.copy()
        # 遍历所有文件夹
        for dir_path in dir_path_list:
            # 找出所有下一级文件夹
            dir_list = [dir for dir in os.listdir(dir_path) if os.path.isdir(os.path.join(dir_path, dir))]
            for dir in dir_list:
                temp_dir_path = os.path.join(dir_path, dir)
                # 当文件夹地址为新
                if temp_dir_path not in dir_path_list:
                    # 比较关键字与目录名
                    compare(os.path.split(temp_dir_path)[1], temp_dir_path)
                    # 将文件夹地址添加进文件夹地址列表
                    dir_path_list.append(temp_dir_path)
                    # 获得该新文件夹下的文件列表
                    f_list = [f for f in os.listdir(temp_dir_path) if os.path.isfile(os.path.join(temp_dir_path, f))]
                    for f in f_list:
                        temp_f_path = os.path.join(temp_dir_path, f)
                        # 比较关键字与文件名
                        compare(os.path.split(temp_f_path)[1], temp_f_path)

    # 写入文件
    with open(os.path.join('.', 'search result.txt'), 'a+') as f:
        f.write('\nKey word is: %s\n\n' % key_word)
        for r in result:
            f.write(r + '\n')

    # 程序结束
    print('Search ends')


if __name__ == '__main__':
    main()