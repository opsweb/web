from django import forms
from django.contrib import admin
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.contrib.auth.models import User as djangouser, Group as djangogroup
from django.contrib.sites.models import Site as djangosite
#import logging.config, logging, logging.handlers

# Register your models here.
import web.models
import web.admin_ip, web.admin_user, web.admin_auth

from web.models import *

#定义可以搜索等自定义选项
'''
class BookAdmin(admin.ModelAdmin):
    #搜索
    search_fields=('title', 'publication_date',)
    #增加 排序显示
    list_display=('title','publication_date', 'publisher')
    #年份月份 筛选
    list_filter=('publication_date',)
    #日期排序 升序
    ordering=('publication_date',)

    #变成右侧添加方式
    filter_horizontal = ('authors',)
    #将选择的添加publisher 发行商，由下拉列表改成文本框搜索
    raw_id_fields = ('publisher',)'''


class TemplatesForm(forms.ModelForm):
    class Meta:
        model = templates
    ips = forms.ModelMultipleChoiceField(
        queryset=Host.objects.all(),
        required=False,
        widget=FilteredSelectMultiple(
            verbose_name= ('Ip list'),
            is_stacked=False
        )
    )

    def __init__(self, *args, **kwargs):
        super(TemplatesForm, self).__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields['ips'].initial = self.instance.ip_set.all()

    def save(self, commit=True):
        groupmachine = super(TemplatesForm, self).save(commit=False)
        if commit:
            groupmachine.save()
        if groupmachine.pk:
            groupmachine.ip_set = self.cleaned_data['ips']
            self.save_m2m()
        return groupmachine


class TemplatesAdmin(admin.ModelAdmin):
	form = TemplatesForm


class ServicesAdmin(admin.ModelAdmin):
    list_display = ('name', 'monitor_type','check_interval')
    filter_horizontal = ('item_list',)
class ItemsAdmin(admin.ModelAdmin):
    list_display = ('name','key','data_type','enabled')
class LogAdmin(admin.ModelAdmin):
    list_display = ('user','ip','event_type','cmd','event_log','result','track_mark')
class OpsLogAdmin(admin.ModelAdmin):
    list_display = ('log_type','finish_date','log_type','tri_user','run_user','cmd','total_task','success_num','failed_num','track_mark','note')
class StatusAdmin(admin.ModelAdmin):
    search_fields = ('host','host_status')
    list_display = ('host','host_status','ping_status','availability','host_uptime','breakdown_count','up_count','attempt_count')
class TriggersAdmin(admin.ModelAdmin):
    list_display = ('name',)
class QuickLinkAdmin(admin.ModelAdmin):
    list_display = ('link_name','url','color')

admin.site.register(Idc)
admin.site.register(Host, web.admin_ip.IpAdmin)
admin.site.register(Group, web.admin_ip.GroupAdmin)
admin.site.register(RemoteUser, web.admin_user.RemoteUserAdmin)
admin.site.register(CenterUser, web.admin_user.TriaquaeUserAdmin)
admin.site.register(AuthByIpAndRemoteUser, web.admin_auth.AuthByIpAndRemoteUserAdmin)
admin.site.register(ServerStatus,StatusAdmin)


admin.site.register(templates,TemplatesAdmin)
admin.site.register(services,ServicesAdmin)
admin.site.register(items,ItemsAdmin)
admin.site.register(triggers,TriggersAdmin)
admin.site.register(graphs)
admin.site.register(operations)
admin.site.register(conditions)
admin.site.register(actions)
admin.site.register(trunk_servers)
admin.site.register(OpsLogTemp,LogAdmin)
admin.site.register(OpsLog,OpsLogAdmin)
admin.site.register(QuickLink,QuickLinkAdmin)