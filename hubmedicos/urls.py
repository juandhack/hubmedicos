from django.conf.urls import patterns, include, url
from django.conf import settings
from apps.inicio.views import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hubmedicos.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^', include('zinnia.urls.capabilities')),
    url(r'^blog/', include('zinnia.urls')),
    url(r'^comments/', include('django.contrib.comments.urls')),
    url(r'^' , include('apps.inicio.urls')),
    url(r'^' , include('apps.perfilesmedicos.urls')),
    url(r'^' , include('apps.perfilespacientes.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT,}),
   
)
