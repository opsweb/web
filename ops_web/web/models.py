from django.db import models
from django import forms
from datetime import datetime

#from django.contrib.auth.models import (User, BaseUserManager, AbstractBaseUser)
#导入admin后台的Users
from django.contrib.auth.models import User

# Create your models here.

'''
class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

    def __unicode__(self):
        return self.name

class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()

    def __str__(self):
        return u'%s %s' % (self.first_name, self.last_name)

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField()

    def __str__(self):
        return self.title
'''

#上传文件
class LogUpload(models.Model):
    id = models.AutoField('id',primary_key=True)
    file_name = models.CharField(max_length=30)
    file_path = models.FileField(upload_to='upload')
    update_time = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.file_path

class ChunZhenIPdb(models.Model):
    StartIP = models.CharField(max_length=50)
    EndIP = models.CharField(max_length=50)
    Country = models.CharField(max_length=90)
    Local = models.CharField(max_length=150)

    def __str__(self):
        return u'%s %s' % (self.StartIP, self.EndIP)

#GetIP提交分析
class GetLogdb(models.Model):
    #分析的文件名
    logviewsfile = models.CharField(max_length=90)
    logdate = models.DateTimeField()
    loggt = models.CharField(max_length=30)
    logoyyline = models.CharField(max_length=30)
    logid = models.CharField(max_length=90)
    logip = models.CharField(max_length=30)
    logdiffip_country = models.CharField(max_length=90)
    logdiffip_loacl = models.CharField(max_length=90)



    def __exit__(self):
        return self.logip

#主机组的数据库
class Idc(models.Model):
    name = models.CharField(max_length=50,unique=True)
    def __str__(self):
        return self.name
#分组，按地域或者业务
class Group(models.Model):
    name = models.CharField(max_length=50,unique=True)
    display_name = models.CharField(max_length=50)
    #多对多，模板的应用列表
    template_list = models.ManyToManyField('templates')

    def __str__(self):
        return self.display_name

#主机管理

class Host(models.Model):

    #名字，资产编号
    hostname = models.CharField(max_length=50,unique=True)
    #软件中的描述
    display_name = models.CharField(max_length=50,unique=True)
    ip = models.IPAddressField(unique=True)
    #负责管理这台服务器的组
    belongs_to = models.ForeignKey('trunk_servers',null=True,blank=True)
    idc = models.ForeignKey('Idc',null=True,blank=True)
    group = models.ManyToManyField('Group',null=True,blank=True)
    template_list = models.ManyToManyField('templates',null=True,blank=True)
    custom_services = models.ManyToManyField('services',null=True,blank=True)
    #m默认SSH或者后面改成socket客户端的端口
    port = models.IntegerField(default='22')
    os = models.CharField(max_length=20,default='linux',verbose_name='Operating System')

    #SNMP监控项
    status_monitor_on = models.BooleanField(default=True)
    snmp_on = models.BooleanField(default=True)
    snmp_version = models.CharField(max_length=10,default='2c')
    snmp_community_name = models.CharField(max_length=50,default='public')
    snmp_security_level = models.CharField(max_length=50,default='auth')
    snmp_auth_protocol = models.CharField(max_length=50,default='DM5')
    snmp_user = models.CharField(max_length=50,default='snmpuser')
    snmp_pass = models.CharField(max_length=50,default='my_pass')

    def __str__(self):
        return self.display_name

#可以存到Redis里面
'''
class ServerStatus(models.Model):
    host = models.IPAddressField(primary_key=True)
    hostname = models.CharField(max_length=100)
    host_status = models.CharField(max_length=100,default='Unkown')
    ping_status = models.CharField(max_length=100,default='Unkown')
    last_check = models.CharField(max_length=100,default='N/A')
    host_uptime = models.CharField(max_length=50,default='Unkown')
    attempt_count = models.IntegerField(default=0)
    breakdown_conunt = models.IntegerField(default=0)
    up_count = models.IntegerField(default=0)
    snmp_alert_count = models.IntegerField(default=0)
    availability = models.IntegerField(max_length=20,default=0)
    def __str__(self):
        return  self.host
'''

class RemoteUser(models.Model):
    name = models.CharField(max_length=50, unique=True)
    def __unicode__(self):
        return self.name
class CenterUser(models.Model):
    user = models.ForeignKey(User, null=True)
    email = models.EmailField()
    remoteuser = models.ManyToManyField(RemoteUser, null=True, blank=True)
    group = models.ManyToManyField(Group, null=True, blank=True)
    ip = models.ManyToManyField(Host, null=True, blank=True)
    def __unicode__(self):
        return '%s' % self.user
class AuthByIpAndRemoteUser(models.Model):
    password = models.CharField(max_length=1024,verbose_name="Password or SSH_KEY")
    AUTH_CHOICES = (('ssh-password', 'ssh-password'),('ssh-key', 'ssh-key'))
    authtype = models.CharField(max_length=100, choices=AUTH_CHOICES)
    ip = models.ForeignKey('Host', null=True, blank=True)
    remoteUser = models.ForeignKey(RemoteUser, null=True, blank=True)
    def __unicode__(self):
        return '%s\t%s' % (self.ip, self.remoteUser)
    #save throw exception
    class Meta:
        unique_together = (('ip','remoteUser'),)


class ServerStatus(models.Model):
    host = models.IPAddressField(primary_key=True)
    hostname = models.CharField(max_length=100)
    host_status = models.CharField(max_length=10,default='Unkown')
    ping_status = models.CharField(max_length=100,default='Unkown')
    last_check = models.CharField(max_length=100,default='N/A')
    host_uptime = models.CharField(max_length=50,default='Unkown')
    attempt_count = models.IntegerField(default=0)
    breakdown_count = models.IntegerField(default=0)
    up_count = models.IntegerField(default=0)
    snmp_alert_count = models.IntegerField(default=0)
    availability = models.CharField(max_length=20,default=0)
    def __unicode__(self):
        return self.host

class OpsLog(models.Model):
    start_date = models.DateTimeField(auto_now_add=True)
    finish_date = models.DateTimeField(null=True,blank=True)
    log_type = models.CharField(max_length=50)
    tri_user = models.CharField(max_length=30)
    run_user = models.CharField(max_length=30)
    cmd = models.TextField()
    total_task = models.IntegerField()
    success_num = models.IntegerField()
    failed_num = models.IntegerField()
    track_mark = models.IntegerField(unique=True)
    note = models.CharField(max_length=100,blank=True,null=True)
    def __unicode__(self):
        return self.cmd

class OpsLogTemp(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    user = models.CharField(max_length=30)
    ip = models.IPAddressField()
    event_type = models.CharField(max_length=50)
    cmd = models.TextField()
    event_log = models.TextField()
    result = models.CharField(max_length=30,default='unknown')
    track_mark = models.IntegerField(blank=True)
    note = models.CharField(max_length=100,blank=True)
    def __unicode__(self):
        return self.ip

class QuickLink(models.Model):
    link_name = models.CharField(max_length=50)
    url = models.URLField()
    COLOR_CHOICES = (('btn-danger', 'red'),('btn-warning', 'yellow'),('btn-success','green'), ('btn-primary','dark-blue'),('btn-info','blue'))
    color = models.CharField(max_length=100, choices=COLOR_CHOICES)

#Trunk Server
class trunk_servers(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=150, blank=True)
    ip_address = models.IPAddressField()
    prot = models.IntegerField(default = 9998)

    def __str__(self):
        return self.name

#模板和模板下面的监控项
class templates(models.Model):
    name = models.CharField(max_length=50, unique=True)
    service_list = models.ManyToManyField('services')
    graph_list = models.ManyToManyField('graphs', blank=True, null=True)

    def __str__(self):
        return self.name

#监控项
class services(models.Model):
    name = models.CharField(max_length=50, unique=True)
    #admin后台下拉可选菜单
    monitor_type_list = (('agent', 'Agent'), ('snmp', 'SNMP'), ('wget', 'Wget'))
    monitor_type = models.CharField(max_length=50,choices=monitor_type_list)
    #客户端取监控项数据的插件key,客户端根据这个找到对应的脚本
    plugin = models.CharField(max_length=100)
    #items 对应的item_list
    item_list = models.ManyToManyField('items')
    #触发器
    trigger = models.ForeignKey('triggers', null=True, blank=True)
    #监控间隔30s
    check_interval = models.IntegerField(default=300)

    def __str__(self):
        return  self.name

class items(models.Model):
    name = models.CharField(max_length=50, unique=True)
    #根据key找到监控的项
    key = models.CharField(max_length=100, unique=True)
    #监控的返回类型 浮点 字符串 整型
    data_type_option = (('float', 'Float'), ('string', 'String'), ('integer','Integer'))
    data_type = models.CharField(max_length=50, choices=data_type_option)
    #以什么单位报警
    unit = models.CharField(max_length=30, default='%')
    #监控项是否打开
    enabled = models.BooleanField(default=True)

    def __str__(self):
        return self.name

#触发器
class triggers(models.Model):
    name = models.CharField(max_length=50, unique=True)
    #前端的表达式，存到字典里，传送给后端判断
    expression = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.name
#画图
class graphs(models.Model):
    name = models.CharField(max_length=50, unique=True)
    datasets = models.ManyToManyField('items')
    graph_type = models.CharField(max_length=50)
    def __str__(self):
        return self.name

#报警中心、报警规则
#使用正则，可以判断很多服务器机器之间的关系，是否有集群冗余等等，确定报警等级
class actions(models.Model):
    name = models.CharField(max_length=100, unique=True)
    condition = models.ManyToManyField('conditions')
    operation_list = models.ManyToManyField('operations')
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=250)
    recovery_notice = models.BooleanField(default=True)
    recovery_subject = models.CharField(max_length=100)
    recovery_message = models.CharField(max_length=250)
    enabled = models.BooleanField(default=True)

    def __str__(self):
        return  self.name
class conditions(models.Model):
    name = models.CharField(max_length=100, unique=True)
    condition_type = models.CharField(max_length=100)
    operator = models.CharField(max_length=30)
    value = models.CharField(max_length=250)
    def __str__(self):
        return self.name

class operations(models.Model):
    send_to_users = models.ManyToManyField('CenterUser')
    send_to_groups = models.ManyToManyField('Group')
    notifier_type = (('email', 'Email'),('sms', 'SMS'))
    send_via =models.CharField(max_length=30, choices=notifier_type)
    #报警间隔
    notice_times = models.IntegerField(default=5)
    notice_interval = models.IntegerField(default=300, verbose_name='notice_interval(sec)')
