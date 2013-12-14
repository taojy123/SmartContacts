
from django.conf.urls import patterns, include, url
from views import *
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'xxx.views.home', name='home'),
    # url(r'^xxx/', include('xxx.foo.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    ('^$', index),
    ('^/$', index),
    ('^index/$', index),
    ('^add_contacts/$', add_contacts),
    ('^get_contacts/(.*)/$', get_contacts),
    ('^add_send/$', add_send),
    ('^get_send/(.*)/$', get_send),
    ('^get_user_info/(.*)/$', get_user_info),
    ('^upload_img/(.*)/$', upload_img),
    ('^show_img/(.*)/$', show_img),
    ('^list_img/(.*)/$', list_img),
    ('^del_img/(.*)/$', del_img),
    ('^find_img/$', find_img),
    ('^search_send/$', search_send),
                       
    ('^reg/$', reg),
    ('^login/$', login),
    ('^logout/$', logout),
)
# This will work if DEBUG is True
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()
