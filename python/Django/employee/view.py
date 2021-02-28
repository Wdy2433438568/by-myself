import py.Pymsqlhelper
from django.shortcuts import render,HttpResponse,redirect
import json

def employee(request):
    tk = request.COOKIES.get('ticket')
    if not tk:
        return redirect('/login/')
    else:
        obj = py.Pymsqlhelper.Mysqlhelper()
        result = obj.getall('select employee.id,name,dep_name,department.id as dep_id from employee inner join department on dep_id=department.id order by employee.id',[])
        dep_info = obj.getall('select id,dep_name from department',[])
        obj.close()
        return render(request,'employee.html',{'empinfo':result,'dep_info':dep_info})


def login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    else:
        obj = py.Pymsqlhelper.Mysqlhelper()
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        result = obj.getall('select count(id) from user where user=%s and pwd=%s',[user,pwd])
        print(result)
        obj.close()
        if result[0]['count(id)'] == 1:
            abc = redirect('/employee/')
            abc.set_signed_cookie('ticket','helloworld')
            return abc
        else:
            return render(request,'login.html')

def delete(request):
    eid = request.GET.get('nid')
    print(eid)
    obj = py.Pymsqlhelper.Mysqlhelper()
    obj.iud('delete from employee where id=%s',[eid])
    obj.close()
    return redirect('/employee/')


def edit(request):
    ret ={'status':True,'message':None}
    try:
        name = request.POST.get('name')
        dep_id = request.POST.get('dep_id')
        emp_id = request.POST.get('emp_id')
        obj = py.Pymsqlhelper.Mysqlhelper()
        print(name,dep_id,emp_id)
        obj.iud('update employee set name=%s,dep_id=%s where id=%s',[name,dep_id,emp_id])
        obj.close()
    except Exception as e:
        ret['status'] = False
        ret['message'] = str(e)
    return HttpResponse(json.dumps(ret))

def insert(request):
    ret ={'status':True,'message':None}
    try:
        name = request.POST.get('name')
        dep_id = request.POST.get('dep_id')
        obj = py.Pymsqlhelper.Mysqlhelper()
        obj.iud('insert into employee(name,dep_id) values (%s,%s)',[name,dep_id])
        obj.close()
    except Exception as e:
        ret['status'] = False
        ret['message'] = str(e)
    return HttpResponse(json.dumps(ret))
