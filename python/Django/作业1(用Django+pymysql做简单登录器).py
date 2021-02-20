"""
利用Django和pymysql实现用户登陆功能
"""
"""s4_mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.shortcuts import HttpResponse,render,redirect
import pymysql

def login(request):
    """
    处理用户请求，并返回内容
    :param request:用户请求相关的所有信息（对象）
    :return:
    """
    #return HttpResponse('') HttpResponse 只能导入字符串

    if request.method== 'GET':
        return render(request,'login.html')#自动找到模板路径下的login.html文件然后读取文件返回给用户，模板路径配置去setings.py下的template下去设置
    else:
        u = request.POST.get('username')#用户post提交的数据（请求体里的数据）
        p = request.POST.get('pwd')
        conn = pymysql.connect(user='root',host='localhost',password='root',port=3306,charset='utf8',db='python')
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        sql = 'select count(id) from User where username="%s" and password="%s"'% (u,p)
        cursor.execute(sql)
        f1=cursor.fetchall()
        cursor.close()
        conn.close()
        if f1[0]['count(id)'] != 0:
            return redirect('/index/')#登陆成功
        else:
            return render(request,'login.html',{'error':'用户名或密码错误'}) #登陆失败

def index(request):
    return render(request,'index.html',{'name':'alex','user':['吴丹阳','nmsl'],'user_dict':{'k1':'wdy','k2':'lsp'},'userlistdict':[{'id':'1','name':'wdy','email':'2433438568@qq.com'},
                                                                                                                                {'id':'2','name':'wdy2','email':'2433438578@qq.com'},
                                                                                                                                {'id':'3','name':'wdy3','email':'1433438568@qq.com'},]})

urlpatterns = [
    #path('admin/', admin.site.urls),
    path(r"login/",login),
    path(r"index/",index)
]
