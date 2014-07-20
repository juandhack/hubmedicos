from django.conf.urls import patterns, include, url
from .views import base,pacientes,board,index

urlpatterns = patterns('',

	#url(r'^$' , 'django.contrib.auth.views.login',
		#{'template_name':'inicio/index.html'}, name='login'),

	#url(r'^home/$','django.contrib.auth.views.login',
		#{'template_name':'inicio/blank-page.html'}, name='home'),

	#url(r'^home/index/','django.contrib.auth.views.login',
		#{'template_name':'inicio/index.html'}, name='index'),
		#url(r'^home/$','apps.inicio.views.sobre'),
		url(r'^home/$',base.as_view()),
		url(r'^$',index.as_view()),
	    url(r'^pacientes/',pacientes.as_view()),
		url(r'^home/board/',board.as_view()),
	


	
)

