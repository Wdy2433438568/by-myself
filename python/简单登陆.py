#!/usr/bin.python3
import sys
dic1 = {}
def new_user():
    while 1 :
            number = str(input("请输入账号："))
            if number in dic1 :
                print("该账号已被注册，请重新输入:")
                continue
            else:
                password = str(input("请输入密码:"))  
                dic1.setdefault(number,password)
                print("账号创建成功")
                print(dic1)
                break

def enter_user():
    while 1:
        number2 = str(input("请输入账号："))
        if number2  in dic1:
            password2 = str(input("请输入密码:"))
            if password2 == dic1[number2]:
                print("登陆成功")
                break
        else:
            print("账号错误，请重新输入:")
            continue

while 1:
    print("|--- 新建用户：N/n ---|\n|--- 登陆账号：E/e ---|\n|--- 退出程序：Q/q ---|\n")
    number = str(input("请输入："))
    if number == 'N' or number == 'n':
        new_user()
    if  number == 'E' or number == 'e':
        enter_user()
    if number == 'q' or number == 'Q':
        sys.exit()
        
