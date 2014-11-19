from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django import forms

#导入app的数据库
from web.models import  *
#导入用户认证模块
from django.contrib import  auth
#启用防跨站攻击模块
from django.template import RequestContext
#导入装饰器、标签
from django.contrib.auth.decorators import login_required
#加载时间延迟
import json

import web.views_core






@login_required
def index(request):


    return render_to_response("index.html",{
                              'login_user':request.user,
                              'active_titel':'index'})
@login_required
def index2(request):


    return render_to_response("index2.html",{
                              'login_user':request.user,
                              'active_titel':'index'})


def logout(request):
    buff='yes'
    auth.logout(request)
    return render_to_response("login.html",buff)



def login(request):
    print(request.POST)
    username = request.POST.get('user','')
    password = request.POST.get('passwd','')
    user=auth.authenticate(username=username,password=password)
    if user is not None:
        #跳转到index
        auth.login(request,user)
        response = HttpResponseRedirect('/index/')
        #cookie缓存
        response.set_cookie('username',username,3600)
        return response
    else:
        return render_to_response("login.html",{'err':"登陆失败：请检查账号密码!"}, RequestContext(request))#防止跨站报错
#-----------HOST--------
@login_required
def host(request):

    server_dic={}
    for g in Group.objects.all():
        #查询多对多，用两个下划线
        ip_list =Host.objects.filter(group__name=g.name)
        #打印的g是对象
        print(g)
        #打印的才是可查询的字符串
        print(g.name)
        server_dic[g.name] = ip_list
        print(server_dic)

    return  render_to_response("host.html", {
                                'server_dic': server_dic,
                                'login_user': request.user,
                                'active_titel': 'host'})
@login_required
def get_ip_list(request):
    '''
    print(request.GET)
    ip_dic={}
    print('aaaaaaaaaaaa')
    gname = request.GET['Name']
    ip_list= HostIP.objects.filter(group__name = gname)
    #print(ip_list)
    for hostip in ip_list:
        ip_dic[hostip.name ]=hostip.ip
        print(ip_dic[hostip.name])
        print("===================================================")

    print(ip_dic)'''
    group_dic = {
        'groupSummary': {},
        'serviceSummary': {},
    }
    for group in Group.objects.all():
        ip_list = Host.objects.filter(group__name=group.name)
        group_dic['groupSummary'][group.id] = [group.name, len(ip_list)]

    return HttpResponse(json.dumps(group_dic))
@login_required
def groupDetail(request, group_id):
    group_obj = Group.objects.get(id= group_id)
    ip_list = Host.objects.filter(group__name = group_obj.name)

    return render_to_response('host/groupDetail.html',{
                        'groupObj': group_obj,
                        'ip_list': ip_list,

                        'active_titel': 'host',
                        'login_user': request.user,
                         })
@login_required
def host_list(request):
    group_id = request.GET.get('group_id')
    ip_list = Host.objects.filter(group__id=group_id)
    ip_dic = {}
    for hs in ip_list:
        ip_dic[hs.id] = [hs.display_name, hs.ip]

    return HttpResponse(json.dumps(ip_dic))
@login_required
def hostDetail(request, host_id):
    hostObj = Host.objects.get(id = host_id)

    return  render_to_response('host/hostDetail.html',{
                                'hostObj':hostObj,

                                'active_titel': 'host',
                                'login_user': request.user,
                                })
@login_required
def getGraph(request):
    print(request.GET)
    g_data={
        'load_1':[2, 3, 4, 5, 5.5, 6, 6.5, 8, 5, 2, 4],
        'load_2':[2.1, 8, 5, 8, 6, 4, 2, 3, 4, 5, 4],
        'load_3':[4, 4, 7, 8, 5, 6, 8, 4, 5, 2, 5],
        'load_x':['10:11', '10:12', '10:13', '10:14', '10:15', '10:16', '10:17', '10:18', '10:19', '10:20', '10:21',]
    }
    return HttpResponse(json.dumps(g_data))

@login_required
def hostManager(request):
    group_dic = {}

    for gro in Group.objects.all():
        host_list=Host.objects.filter(group__id=gro.id)
        group_dic[gro.name] = host_list
    test1={"id:1, pId:0, name:随意勾选1, open:true"}

    return  render_to_response('host/hostManager.html',{
                                'group_dic':group_dic,
                                'test1':test1,
                                'active_titel': 'host',
                                'login_user': request.user,
                                })
@login_required
def hostManagerlist(request):
    group_dic = {
        'manager_group': {},
        'manager_ip': {},
        }

    for group in Group.objects.all():
        ip_list = Host.objects.filter(group__name=group.name)
        group_dic['manager_group'][group.id] = [group.name, len(ip_list)]



    return  HttpResponse(json.dumps(group_dic))

#-----------Monitor--------
@login_required
def monitor(request):

    return  render_to_response("monitor.html",
                               {
                                'login_user': request.user,
                                'active_titel': 'monitor',

                               })

@login_required
def monitor_summary_load(request):

    name_dic={
        1:['A1', '上海1', '192.168.10.111/110.123.154.21', 'gate1', 'win', '在线-启用'],
        2:['A6', '无锡', '121.24.154.15', 'game3', 'linux', '在线-未启用'],
        3:['C5', '北京', '121.15.0.15', 'manager1', 'win', '离线'],
        4:['F6', '北京', '121.15.11.125', 'db', 'win', '在线-未知'],
        5:['A2', '香港', '158.155.154.216', 'namelog', 'win', '在线-启用'],
        6:['C1', '上海', '101.12.123.154', 'web', 'linux', '在线-启用'],
        7:['A7', '上海', '101.12.65.56', 'cdn1', 'linux', '离线'],

    }
    #book_list = Book.objects.all()


    return  render_to_response("monitor/monitor_load.html",
                               {'name_list':name_dic,
                                #'book_list':book_list,
                                'login_user':request.user,
                                'active_titel':'monitor',

                               })

#-----------Assets--------
@login_required
def assets(request):

    return  render_to_response("assets.html",  {
                                'login_user':request.user,
                                'active_titel':'assets'})
#-----------YunWei--------
@login_required
def yunwei(request):

    return  render_to_response("yunwei.html", {
                                'login_user':request.user,
                                'active_titel':'yunwei'} )
#-----------Log--------
@login_required
def log(request):

    return  render_to_response("log.html",  {
                                'login_user':request.user,
                                'active_titel':'log'})

#接收上传的文件的类

class UserForm(forms.Form):
    upload_logfile_name=forms.CharField(label="日志别名")
    upload_logfile_path=forms.FileField(label="上传日志")
    #ip_query=forms.IPAddressField(label="查询IP")

#处理上传的日志的url视图
@login_required
def aslog(request):
    #选项卡激活

    #上传的文件列表
    upload_logfile_list = LogUpload.objects.all()
    #IP查询
    if request.method == "GET":
        ipf = request.GET.get('ip_query', '')
        iplog = request.GET.get('views_log', '')
        print(iplog)
        print(ipf)
            #IP查询
        if ipf :
            #获取要查询的IP
            ip_query = ipf
            return render_to_response('aslog.html',{
                                            'views_ip':my_custom_sql(request,ip_query),
                                            'views_ip_add':ipf,
                                            'login_user':request.user,
                                            'active_titel':'log',
                                            'active_path':request.path,
                                            }, RequestContext(request))#防止跨站报错
        if iplog:
            views_log=iplog
            print(views_log)
            vf=GetLogdb.objects.filter(logviewsfile=views_log)


            print(vf)
            return render_to_response('aslog.html',{
                            'vfile':views_log, #get请求的内容
                            'views_log':vf, #数据库内取出点击后分析的所有文件
                            'log_analyse':log_count_main(request,views_log), #点击按钮后 统计线路结果
                            'views_ip_add':ipf,#查询IP
                            'login_user':request.user,
                            'active_titel':'log',
                            'active_path':request.path,
                        }, RequestContext(request))#防止跨站报错
    else:
        ipf = UserForm()




    #处理上传日志
    if request.method == "POST":
        upf = UserForm(request.POST,request.FILES)
        #日志文件上传
        print(request.FILES)
        if upf.is_valid():

            #获取form表单信息
            upload_name=upf.cleaned_data['upload_logfile_name']
            upload_path=upf.cleaned_data['upload_logfile_path']

            upload=LogUpload()
            upload.file_name=upload_name
            upload.file_path=upload_path
            upload.save()
            #预处理日志
            #fll=UserForm(request.FILES)

            #print(fll)
            #file=open('d:/work_project/python_Django/upload/20140807_fqJfpTY.log','wb+')
            print(upload.file_path)
            lfilepath=str(upload.file_path)

            #while 日志处理
            lfilename=open(lfilepath,'r')
            f=lfilename.readline()
            i=0

            while f !='':
                i += 1
                print(i)
                #调用日志处理的方法
                log_strip_main(request,f,lfilepath)
                #print(log_strip_main(request,f),"111111")
                f=lfilename.readline()
            lfilename.close()



            return render_to_response('aslog.html',{
                                            'upsuccess':'1',#文件上传成功返回值

                                            'log_ivews':log_count_main(request,lfilepath),#统计结果
                                            'upload_logfile_list':upload_logfile_list,
                                            'login_user':request.user,
                                            'active_titel':'log',
                                            }, RequestContext(request))#防止跨站报错
    else:
        upf = UserForm()
    return render_to_response('aslog.html',{'upf':upf,
                                            'upload_logfile_list':upload_logfile_list,

                                            'login_user':request.user,
                                            'active_titel':'log',
                                            'active_path':request.path,
                                            }, RequestContext(request))#防止跨站报错



#自己定义了mysql查询
@login_required
def my_custom_sql(request,ip):
    from django.db import  connection
    #获得一个游标(cursor)对象
    cursor=connection.cursor()
    cursor.execute('select  *  from web_chunzhenipdb where INET_ATON(%s) between INET_ATON(startIp) and INET_ATON(endIp)' ,[ip])
    #返回结果
    raw = cursor.fetchone()
    #return HttpResponse(row)
    #返回一个list类型的
    lis=[]
    dic={}

    dic['startip']=raw[1]
    dic['endip']=raw[2]
    dic['country']=raw[3]
    dic['local']=raw[4]

    lis.append(dic)

    return lis
#游戏IP日志mysql查询
@login_required
def log_mysql_query(request,ip):
    from django.db import  connection
    #获得一个游标(cursor)对象
    cursor=connection.cursor()
    cursor.execute('select  *  from web_chunzhenipdb where INET_ATON(%s) between INET_ATON(startIp) and INET_ATON(endIp)' ,[ip])
    #返回结果
    raw = cursor.fetchone()
    #return HttpResponse(row)
    lwa="null"
    lwb="null"

    lwa=raw[3]
    lwb=raw[4]

    return lwa,lwb

#----------- Message ----------
@login_required
def message(request):
    return  render_to_response("message.html",  {
                                'login_user':request.user,
                                'active_titel':'message'})


#游戏IP日志mysql查询
@login_required
def log_strip_main(request,f,lfilepath):
    getlog1=GetLogdb()
    getlog1.logviewsfile =lfilepath
    #f=f.decode('utf-8')
    #print(f)
    #对日志字符串进行切割
    #日志段落定义
    #s1=f.find(' lv2')
    #打印出日期
    log_date=f[0:18]
    getlog1.logdate=log_date
    #print(f[0:s1])
    #打印GT
    s2=f.find(':Abnormal')
    #log_GT=f[s2-5:s2]
    log_GT=f[24:29]
    getlog1.loggt=log_GT
    #判断GT是电信还是联通
    #ccnetline=f.find('GT11')
    ccnetline=f[24:28]
    if ccnetline=='GT11':
        getlog1.logoyyline="联通"

    else:
        getlog1.logoyyline="电信"

    #存到数据库

    #print(f[s2-5:s2])
    #打印ID
    s3=f.find('ID(')
    s4=f.find('), IP')
    log_ID=f[s3+3:s4]
    #print(f[s3+3:s4])
    getlog1.logid=log_ID
    #打印出IP
    #print(f[s4+6:-1])
    log_IP=f[s4+6:-2]
    #将IP存到数据库
    logip_countyy,logip_local=log_mysql_query(request,log_IP)
    getlog1.logdiffip_country=logip_countyy
    getlog1.logdiffip_loacl=logip_local

    getlog1.logip=log_IP
    getlog1.save()
    #time.sleep(0.005)


    return "ok"

#游戏IP日志统计
@login_required
def log_count_main(request,fviews):
    from django.db import  connection
    #获得一个游标(cursor)对象
    cursor=connection.cursor()
    cursor.execute(
                '''SELECT  leixing ,COUNT(*)
                FROM(select case WHEN logoyyline = '电信' AND logdiffip_loacl='电信' THEN '电信:电信'
                WHEN logoyyline = '电信' AND logdiffip_loacl='联通' THEN '电信:联通'
                WHEN logoyyline = '电信' AND logdiffip_loacl<>'电信' AND logdiffip_loacl<>'联通' THEN '电信:其他'
                WHEN logoyyline = '联通' AND logdiffip_loacl='联通' THEN '联通:联通'
                WHEN logoyyline = '联通' AND logdiffip_loacl='电信' THEN '联通:电信'
                WHEN logoyyline = '联通' AND logdiffip_loacl<>'电信' AND logdiffip_loacl<>'联通' THEN '联通:其他'
                ELSE '其他'
                END leixing
                from  web_getlogdb
                WHERE logviewsfile=%s
                ) A
                GROUP BY leixing''',[fviews])
    #返回结果

    fetchall = cursor.fetchall()

    card=[]
    for obj in fetchall:
        dic={}
        dic['leixing']=obj[0]
        dic['count']=obj[1]
        card.append(dic)
    #context['card']=card
    print(card)
    return  card

#select count(*) from web_getlogdb WHERE (logviewsfile='upload/111111.txt') and logoyyline='电信' and logdiffip_loacl='电信';
#select logoyyline,logdiffip_loacl,count(*) as num from web_getlogdb by logoyyline,logdiffip_loacl

#线路查询
