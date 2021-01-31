import easygui as g
import os
file_start = g.fileopenbox(default='*.txt')
with open(file_start) as file_start1:
    text = file_start1.read()
    title = os.path.basename(file_start)
    msg = 'open'
    file_after = g.textbox(msg,title,text)
    file_start1.close()
if text != file_after:
    choice = g.buttonbox(title='警告',msg='文件已被修改，您确定要保存修改吗？' ,choices=['覆盖','另立为','放弃'])
    if choice == '放弃':
        pass
    if choice == '覆盖':
        with open(file_start,'w') as file_after2 :
            file_after2.write(file_after)
            file_after2.close()
    if choice == '另立为':
        another_file = g.filesavebox(default='*.txt')
        f1 = open(another_file,'w')
        f1.write(file_after)
        f1.close()
        if os.path.splitext(another_file)[1] != '.txt':
            os.path.basename += '.txt'
    
