#!/usr/bin/python3
password='0'
symbol=r"'!,@,#,$,%,^,&,*,|,{,},\\'"
while True:
    temp=input("请输入密码")
    password=temp
    for each in range(len(password)):
        if password.isalnum() and len(password) <=8 and password[each] not in symbol:
            print('低级密码')
            print("请按以下方式提升您的密码安全级别：\n\
                \t1. 密码必须由数字、字母及特殊字符三种组合\n\
                \t2. 密码只能由字母开头\n\
                \t3. 密码长度不能低于16位'")
            break
       
        if  len(password)>=8 and password[each] in symbol:
            if len(password)>=16 and password[0].isalpha:
                print("高级密码")
                continue
            else:
                print("中级密码")  
                print("请按以下方式提升您的密码安全级别：\n\
                \t1. 密码必须由数字、字母及特殊字符三种组合\n\
                \t2. 密码只能由字母开头\n\
                \t3. 密码长度不能低于16位'")
                continue
                    
    
    
