# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='actions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('subject', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=250)),
                ('recovery_notice', models.BooleanField(default=True)),
                ('recovery_subject', models.CharField(max_length=100)),
                ('recovery_message', models.CharField(max_length=250)),
                ('enabled', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AuthByIpAndRemoteUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('password', models.CharField(verbose_name='Password or SSH_KEY', max_length=1024)),
                ('authtype', models.CharField(choices=[('ssh-password', 'ssh-password'), ('ssh-key', 'ssh-key')], max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CenterUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('email', models.EmailField(max_length=75)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ChunZhenIPdb',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('StartIP', models.CharField(max_length=50)),
                ('EndIP', models.CharField(max_length=50)),
                ('Country', models.CharField(max_length=90)),
                ('Local', models.CharField(max_length=150)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='conditions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('condition_type', models.CharField(max_length=100)),
                ('operator', models.CharField(max_length=30)),
                ('value', models.CharField(max_length=250)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GetLogdb',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('logviewsfile', models.CharField(max_length=90)),
                ('logdate', models.DateTimeField()),
                ('loggt', models.CharField(max_length=30)),
                ('logoyyline', models.CharField(max_length=30)),
                ('logid', models.CharField(max_length=90)),
                ('logip', models.CharField(max_length=30)),
                ('logdiffip_country', models.CharField(max_length=90)),
                ('logdiffip_loacl', models.CharField(max_length=90)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='graphs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('graph_type', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('display_name', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('hostname', models.CharField(max_length=50, unique=True)),
                ('display_name', models.CharField(max_length=50, unique=True)),
                ('ip', models.IPAddressField(unique=True)),
                ('port', models.IntegerField(default='22')),
                ('os', models.CharField(verbose_name='Operating System', default='linux', max_length=20)),
                ('status_monitor_on', models.BooleanField(default=True)),
                ('snmp_on', models.BooleanField(default=True)),
                ('snmp_version', models.CharField(default='2c', max_length=10)),
                ('snmp_community_name', models.CharField(default='public', max_length=50)),
                ('snmp_security_level', models.CharField(default='auth', max_length=50)),
                ('snmp_auth_protocol', models.CharField(default='DM5', max_length=50)),
                ('snmp_user', models.CharField(default='snmpuser', max_length=50)),
                ('snmp_pass', models.CharField(default='my_pass', max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Idc',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='items',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('key', models.CharField(max_length=100, unique=True)),
                ('data_type', models.CharField(choices=[('float', 'Float'), ('string', 'String'), ('integer', 'Integer')], max_length=50)),
                ('unit', models.CharField(default='%', max_length=30)),
                ('enabled', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LogUpload',
            fields=[
                ('id', models.AutoField(verbose_name='id', primary_key=True, serialize=False)),
                ('file_name', models.CharField(max_length=30)),
                ('file_path', models.FileField(upload_to='upload')),
                ('update_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='operations',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('send_via', models.CharField(choices=[('email', 'Email'), ('sms', 'SMS')], max_length=30)),
                ('notice_times', models.IntegerField(default=5)),
                ('notice_interval', models.IntegerField(verbose_name='notice_interval(sec)', default=300)),
                ('send_to_groups', models.ManyToManyField(to='web.Group')),
                ('send_to_users', models.ManyToManyField(to='web.CenterUser')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OpsLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('finish_date', models.DateTimeField(blank=True, null=True)),
                ('log_type', models.CharField(max_length=50)),
                ('tri_user', models.CharField(max_length=30)),
                ('run_user', models.CharField(max_length=30)),
                ('cmd', models.TextField()),
                ('total_task', models.IntegerField()),
                ('success_num', models.IntegerField()),
                ('failed_num', models.IntegerField()),
                ('track_mark', models.IntegerField(unique=True)),
                ('note', models.CharField(blank=True, null=True, max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OpsLogTemp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('user', models.CharField(max_length=30)),
                ('ip', models.IPAddressField()),
                ('event_type', models.CharField(max_length=50)),
                ('cmd', models.TextField()),
                ('event_log', models.TextField()),
                ('result', models.CharField(default='unknown', max_length=30)),
                ('track_mark', models.IntegerField(blank=True)),
                ('note', models.CharField(blank=True, max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='QuickLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('link_name', models.CharField(max_length=50)),
                ('url', models.URLField()),
                ('color', models.CharField(choices=[('btn-danger', 'red'), ('btn-warning', 'yellow'), ('btn-success', 'green'), ('btn-primary', 'dark-blue'), ('btn-info', 'blue')], max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RemoteUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ServerStatus',
            fields=[
                ('host', models.IPAddressField(primary_key=True, serialize=False)),
                ('hostname', models.CharField(max_length=100)),
                ('host_status', models.CharField(default='Unkown', max_length=10)),
                ('ping_status', models.CharField(default='Unkown', max_length=100)),
                ('last_check', models.CharField(default='N/A', max_length=100)),
                ('host_uptime', models.CharField(default='Unkown', max_length=50)),
                ('attempt_count', models.IntegerField(default=0)),
                ('breakdown_count', models.IntegerField(default=0)),
                ('up_count', models.IntegerField(default=0)),
                ('snmp_alert_count', models.IntegerField(default=0)),
                ('availability', models.CharField(default=0, max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='services',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('monitor_type', models.CharField(choices=[('agent', 'Agent'), ('snmp', 'SNMP'), ('wget', 'Wget')], max_length=50)),
                ('plugin', models.CharField(max_length=100)),
                ('check_interval', models.IntegerField(default=300)),
                ('item_list', models.ManyToManyField(to='web.items')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='templates',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('graph_list', models.ManyToManyField(to='web.graphs', blank=True, null=True)),
                ('service_list', models.ManyToManyField(to='web.services')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='triggers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('expression', models.CharField(max_length=1000)),
                ('description', models.CharField(max_length=1000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='trunk_servers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('description', models.CharField(blank=True, max_length=150)),
                ('ip_address', models.IPAddressField()),
                ('prot', models.IntegerField(default=9998)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='services',
            name='trigger',
            field=models.ForeignKey(to='web.triggers', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='host',
            name='belongs_to',
            field=models.ForeignKey(to='web.trunk_servers', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='host',
            name='custom_services',
            field=models.ManyToManyField(to='web.services', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='host',
            name='group',
            field=models.ManyToManyField(to='web.Group', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='host',
            name='idc',
            field=models.ForeignKey(to='web.Idc', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='host',
            name='template_list',
            field=models.ManyToManyField(to='web.templates', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='group',
            name='template_list',
            field=models.ManyToManyField(to='web.templates'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='graphs',
            name='datasets',
            field=models.ManyToManyField(to='web.items'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='centeruser',
            name='group',
            field=models.ManyToManyField(to='web.Group', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='centeruser',
            name='ip',
            field=models.ManyToManyField(to='web.Host', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='centeruser',
            name='remoteuser',
            field=models.ManyToManyField(to='web.RemoteUser', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='centeruser',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='authbyipandremoteuser',
            name='ip',
            field=models.ForeignKey(to='web.Host', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='authbyipandremoteuser',
            name='remoteUser',
            field=models.ForeignKey(to='web.RemoteUser', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='authbyipandremoteuser',
            unique_together=set([('ip', 'remoteUser')]),
        ),
        migrations.AddField(
            model_name='actions',
            name='condition',
            field=models.ManyToManyField(to='web.conditions'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='actions',
            name='operation_list',
            field=models.ManyToManyField(to='web.operations'),
            preserve_default=True,
        ),
    ]
