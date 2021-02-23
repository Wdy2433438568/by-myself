ajax:    function get_del_id() {
        var nid=$('#editid').val();
        $.ajax({
            url:'/edit_class_cancle/',
            type:'POST',
            data:{'nid':nid},
            success:function (arg){
                arg = JSON.parse(arg);
                if (arg.status){
                    location.reload();
                }else {
                    alert(arg.message)
                }
            }
        })
    }
    
 html:<input type="button" value="删除" onclick="get_del_id()">
 
 跳转后功能实现:
 def modal_cancle_class(request):
    ret = {'status':True,'message':None}
    try:
        nid = request.POST.get('nid')
        PyMySQLhelper.dori('delete from class where id =%s',(nid,))
    except Exception as e:
        ret['status'] = False
        ret['message'] = '这都能错？不会吧？'
    print("nid",nid)
    return HttpResponse(json.dumps(ret))
