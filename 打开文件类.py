#!/usr/bin/python3
import easygui as g
class Openfile:
    def __init__(self):
        g.msgbox('我启动啦！','启动')
    
    def openfile(self):
        with open(g.fileopenbox(default='*.txt')) as f1:
            a = f1.read()
            g.textbox(text=a,msg='文件内容如下',title='')
           
    
    def __del__(self):
        f1.close() 
        g.msgbox('我关闭啦！','关闭')


opf = Openfile()
opf.openfile()
