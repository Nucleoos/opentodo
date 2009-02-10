from django.conf import settings
from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'todo.views.index'),
    (r'^opentodo/', include('todo.urls')),
    (r'^opentodo/logout/$', 'django.contrib.auth.views.logout_then_login'),
    (r'^opentodo/accounts/login/$', 'django.contrib.auth.views.login'),
    (r'^admin/(.*)', admin.site.root),
)