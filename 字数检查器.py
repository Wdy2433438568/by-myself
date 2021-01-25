#!/usr/bin/python3
def findstr(*str1):
    e = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    s = '!@#$%^&*()~`_+{}:"<>?[];,./\|'
    n = '123456789'
    length= len(str1)
    for i in range(length):
        cout = 0 #'英文字母'
        number = 0 #'数字'
        space = 0 #'空格'
        symbols = 0 #'其他字符'
        
        for each in str1[i]:
            if each in e:
                cout +=1
            if each in s:
                symbols +=1
            if each in n:
                number +=1
            if each == ' ':
                space +=1
    print(cout,number,space,symbols)
while 1:
    temp = input("请输入要统计的字符串：")
    name = findstr(temp)
    continue
