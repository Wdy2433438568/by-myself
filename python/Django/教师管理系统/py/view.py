from django.shortcuts import redirect,HttpResponse,render
import pymysql

def teacher(request):
    conn =pymysql.connect(
        user='root',host='localhost',password='root',charset='utf8',db='python',port=3306
    )
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    sql = 'select id,name from teacher'
    cursor.execute(sql)
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return render(request,'teacher.html',{'user':data})

def add_t(request):
    if request.method == 'GET':
        return render(request,'add_teacher.html')
    else:
        t = request.POST.get('add_t')
        conn =pymysql.connect(
            user='root',host='localhost',password='root',charset='utf8',db='python',port=3306
        )
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        sql = 'insert into teacher(name) values("%s")'% t
        print(sql)
        cursor.execute(sql)
        conn.commit()
        cursor.close()
        conn.close()
        return redirect('/teacher/')

def del_t(request):
    nid = request.GET.get('nid')
    conn =pymysql.connect(
        user='root',host='localhost',password='root',charset='utf8',db='python',port=3306
    )
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    sql = 'delete from teacher where id =%s'% nid
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()
    return redirect('/teacher/')
def edit_t(request):
    if request.method == 'GET':
        nid = request.GET.get('nid')
        conn =pymysql.connect(
            user='root',host='localhost',password='root',charset='utf8',db='python',port=3306
        )
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        sql = 'select id,name from teacher where id =%s'% nid
        print(sql)
        cursor.execute(sql)
        response=cursor.fetchone()
        cursor.close()
        conn.close()
        return render(request,'edit_t.html',{'result':response})
    else:
        nid = request.GET.get('nid')
        print("nid:",nid)
        name = request.POST.get('title')
        print("name:",name)
        conn =pymysql.connect(
            user='root',host='localhost',password='root',charset='utf8',db='python',port=3306
        )
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        sql = 'update teacher set name="%s" where id=%s'% (name,nid)
        print(sql)
        cursor.execute(sql)

        conn.commit()
        cursor.close()
        conn.close()
        return redirect('/teacher/')
