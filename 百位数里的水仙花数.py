#!/usr/bin/python3
name=input("请输入一个三位数")
value=int(name)
while 1:
    if value // 100 !=0:
        mod1=value//100
        such1=value%100
        number1=mod1**3
        if such1//10 !=0:
            mod2=such1//10
            number2=mod2**3
            mod3=such1%10
            number3=mod3**3
            if number1+number2+number3 == mod1*100+mod2*10+mod3:
                print("yes it is")
                break
            else:
                print("no it is not")
                break
        if (value - mod1*100)//10 == 0:
            mod3 = such1 % 10 
            number3 = mod3**3
            if number1  + number3 == mod1*100+mod3:
                print("yes it is")
                break
            else:
                print("no it is not")
                break 
            
        
