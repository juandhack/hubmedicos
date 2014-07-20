from django.conf.urls import patterns, include, url
from apps.inicio.views import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hubmedicos.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
 #INICIO
    url(r'^' , include('apps.inicio.urls')),
    url(r'^cuentas/', include('registration.urls')),
    url(r'^admin/', include(admin.site.urls)),
   
)
