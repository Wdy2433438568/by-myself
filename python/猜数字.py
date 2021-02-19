#!/usr/bin/python3
import random
import easygui as g
i=random.randint(1,10)
g.msgbox(msg='第一次')
msg = '猜猜看'
title = '猜数字'
time = 3
while 1:
    if time != 0:
        guess = g.integerbox(msg,title,lowerbound=1,upperbound=10)
        if guess == i:
            g.msgbox("fuck yeah!")
            break
        else:
            if guess > i:
                g.msgbox('your times left:'+str(time))
                time -= 1
                g.msgbox('')
            else:
                g.msgbox('bigger')
                time -= 1
                g.msgbox('your times left:'+str(time))
    else:
        break
g.msgbox('game over!')
