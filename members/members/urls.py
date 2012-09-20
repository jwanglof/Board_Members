from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from see_members.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'members.views.home', name='home'),
    # url(r'^members/', include('members.foo.urls')),

    ("^$", home),
    (r"^member/(?P<member_id>\d+)/$", member_specific),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
