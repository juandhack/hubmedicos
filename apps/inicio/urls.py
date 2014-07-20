from django.conf.urls import patterns, include, url
from .views import tipografia,base,blank_page,board,index,bootstrap_grid,bootstrap_elements,charts,formularios,tables

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
		url(r'^home/blank/',blank_page.as_view()),
		url(r'^home/board/',board.as_view()),
		url(r'^home/bootsgrid/',bootstrap_grid.as_view()),
		url(r'^home/bootselements/',bootstrap_elements.as_view()),
		url(r'^home/charts/',charts.as_view()),
		url(r'^home/formularios/',formularios.as_view()),
		url(r'^home/tables/',tables.as_view()),
		url(r'^home/tipografia/',tipografia.as_view()),


	
)

