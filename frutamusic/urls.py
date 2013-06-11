from django.conf.urls import patterns, include, url
#coding: utf-8
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^blog/', include('blog.urls')),
    # Examples:
    # url(r'^$', 'frutamusic.views.home', name='home'),
    # url(r'^frutamusic/', include('frutamusic.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
