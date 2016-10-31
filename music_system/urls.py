from django.conf.urls import patterns, url
from django.conf.urls import include
from django.contrib import admin
from device import views

prefix1 = "device/"
prefix2 = "group/"

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^%s$'%prefix1, views.index, name='index'),
    url(r'^%s(?P<device_id>\w+)/$'%prefix1, views.device_control, name='device control'),
    url(r'^%s(?P<group_id>\w+)/$'%prefix2, views.group_control, name='group control'),
    url(r'^playlist/', views.show_list, name='play list')
)
