from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

#加载app
from web.views_core import *
from web.views_core import * #sayHi,second,time,login,login1
#加载static静态文件
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', index),
    url(r'index/$', index),
    url(r'notify/mail/$', notify_mail),
    url(r'notify/notifications/$',notify_notifications),
    url(r'table/$',table),
    url(r'^dashboard/$',dashboard),

    #url(r'^login/$', login),
    #url(r'^logout/$', logout),
    #url(r'^$', login),







    #定义未登录的跳转
    url(r'^accounts/login/$', 'django.contrib.auth.views.login',{'template_name':'login.html'}),




) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
