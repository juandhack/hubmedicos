from django.conf.urls import patterns, include, url
from .views import sobre

urlpatterns = patterns('',

	url(r'^$' , 'django.contrib.auth.views.login',
		{'template_name':'inicio/index.html'}, name='login'),

	#url(r'^home/$','django.contrib.auth.views.login',
		#{'template_name':'inicio/blank-page.html'}, name='home'),

	#url(r'^home/index/','django.contrib.auth.views.login',
		#{'template_name':'inicio/index.html'}, name='index'),
		#url(r'^home/$','apps.inicio.views.sobre'),
		url(r'^home/$',index2.as_view()),

	
)

