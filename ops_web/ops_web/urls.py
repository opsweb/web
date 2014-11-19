from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

#加载app
from web.views import * #sayHi,second,time,login,login1

#加载static静态文件
from django.conf import settings
from django.conf.urls.static import static
import web.urls


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'python_Django.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^time/$', current_datetime),
    #url(r'^hello/$',sayHi),
    #url(r'mine/$',second),

    #url(r'^time/\d+/$',time),

    url(r'^index/$', index),


    url(r'^login/$', login),
    url(r'^logout/$', logout),
    url(r'^$', login),

    #Host
    url(r'^host/$', host),
    url(r'^get_ip_list/$', get_ip_list),
    url(r'^groupDetail/(\d+)/$', groupDetail),
    #url(r'^host_list/(\d+)/$', host_list),
    #通过get传送来的数据，不能把URL写死
    url(r'^host_list/$', host_list),
    url(r'^hostDetail/(\d+)/$', hostDetail),
    url(r'^getGraph/$', getGraph),
    url(r'^hostManager/$', hostManager),
    url(r'^hostManagerlist/$',hostManagerlist),



    url(r'^monitor/$', monitor),
    url(r'^monitor/monitor_load/$', monitor_summary_load),

    url(r'^assets/$', assets),

    url(r'^yunwei/$', yunwei),

    url(r'^log/$', log),
    url(r'^log/aslog/$', aslog),
    url(r'^log/viewsip/$', my_custom_sql),


    url(r'message/$', message),

    #定义未登录的跳转
    url(r'^accounts/login/$', 'django.contrib.auth.views.login',{'template_name':'login.html'}),
    #定义退出的跳转
    #url(r'^accounts/logout/$', 'django.contrib.auth.views.logout',{'template_name':'login.html'})

    #定义app下面的urls
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^2/', include('web.urls')),




) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
