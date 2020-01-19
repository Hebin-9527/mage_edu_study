#！/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2020/1/18 23:53
# @Author : David_9527
# @File : useradd.py
# 批量或单个添加用户
#-------------------------------------------Code-------------------------------------------
import getpass
import os
import time
import datetime

def open_pass():
    ps_wenjian = open('/etc/passwd', 'r',encoding='utf-8')
    wenjian = ps_wenjian.readlines()
    ps_wenjian.close
    return wenjian
date1 = datetime.datetime.strftime((datetime.datetime.now() + datetime.timedelta(days=365)), '%Y-%m-%d')
user_pass = {}
choose = input('Please choose batch create username or single create username (2:batch/1:single): ')
choose = int(choose)
if choose == 1:
    while True:
        open_pass()
        username = input('please input username: ')
        password = getpass.getpass('Please enter password: ')
        for nn in open_pass():
            nnn = nn.split(':', 1)[0]
            if username != nnn:
                print('create username')
                os.system('useradd  %(name1)s -s /bin/bash' % {'name1':username})   #创建用户
                os.system('echo %(pass)s |passwd --stdin %(name1)s' % {'name1': username, 'pass':password})
                date1 = datetime.datetime.strftime((datetime.datetime.now() + datetime.timedelta(days=365)), '%Y-%m-%d')
                os.system('chage -E %(dat)s -W 10 -m 30 -M 365 %(name1)s' % {'name1': username, 'dat': date1})
                user_pass[username] = password  # 将创建的用户和其对应的密码添加到字典中
                print('Created user! and password add successfully.')
                break
            else:
                print('username is exits,Please again enter username.')
                break
        mm = input('Please yes or no (yes/no): ')
        mm = mm.lower()
        f = True
        while f:
            if mm == 'yes':
                print('Please continue create username.')
                f = False
            else:
                break
        if mm == 'no':
            break

elif choose == 2:
    username_list = []
    username_numb = input('Please enter create how many users : ')
    f = True
    while f:
        username = input('please input username: ')
        password = input("Please input password: ")
        open_pass()
        for nn1 in open_pass():
            nnn1 = nn1.split(':', 1)[0]
            if username == nnn1:
                print('username is exists,Please again enter !')
                break
            else:
                f = False
    for uu in range(1,int(username_numb)+1):
        print('create username')
        os.system('useradd %s%s -s /bin/bash' % (username, uu))   #创建用户
        username_list.append('%s%s'%(username,uu))
    for us in username_list:
        os.system('echo %(pass)s |passwd --stdin %(name1)s' % {'name1': us, 'pass':password})
        os.system('chage -E %(dat)s -W 10 -m 30 -M 365 %(name1)s' % {'name1': us, 'dat': date1})
        user_pass[us] = password  # 将创建的用户和其对应的密码添加到字典中
        print('Created user! and password add successfully.')
else:
    print('only input 1 or 2')

print(user_pass)
print('Created user! and password add successfully.')

