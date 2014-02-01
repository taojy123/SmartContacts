
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

    ('^readme/$', readme),
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
    ('^login_adv/$', login_adv),
    ('^logout/$', logout),


    ('^output/$', output),
    ('^output_img/$', output_img),
    ('^login_user/$', login_user),
    ('^login_page/$', login_page),
    ('^config/$', config),
    ('^update_config/$', update_config),
    ('^regist/$', regist),
    ('^register/$', register),
    ('^send/$', send),
    ('^waybill/(.*)/$', waybill),

    ('^get_ip/$', get_ip),
    ('^set_session/$', set_session),
    ('^get_session/$', get_session),

)
# This will work if DEBUG is True
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()
