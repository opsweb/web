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






@login_required
def index(request):


    return render_to_response("core/index.html",{

                              'login_user':request.user,
                              })

@login_required
def notify_mail(request):
        return render_to_response("core/notify/mail.html",{

                              'login_user':request.user,
                              })

@login_required
def notify_notifications(request):
        return render_to_response("core/notify/notifications.html",{

                              'login_user':request.user,
                              })
@login_required
def table(request):
        return render_to_response("core/table.html",{

                              'login_user':request.user,
                              })
@login_required
def dashboard(request):
        return render_to_response("core/dashboard.html",{

                              'login_user':request.user,
                              })