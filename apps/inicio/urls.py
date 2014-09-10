from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = patterns('',

	#url(r'^$' , 'django.contrib.auth.views.login',
		#{'template_name':'inicio/index.html'}, name='login'),

	#url(r'^home/$','django.contrib.auth.views.login',
		#{'template_name':'inicio/blank-page.html'}, name='home'),

	#url(r'^home/index/','django.contrib.auth.views.login',
		#{'template_name':'inicio/index.html'}, name='index'),
		#url(r'^home/$','apps.inicio.views.sobre'),
		#url(r'^home/$',board.as_view()),
	url(r'^$',index.as_view()),
	#url(r'^pacientes/',pacientes.as_view()),
        url(r'^login/medico/$', LoginView.as_view(), name='login_medico'),
        url(r'^login/paciente/$',LoginViewPaciente.as_view(), name='login_paciente'),
        url(r'^logout/$', LogoutView.as_view(), name='logout'),
	url(r'^reg/medico/$', RegisterView.as_view(), name='registro_medico'),
        url(r'^reg/paciente/$', RegisterViewPaciente.as_view(), name='registro_paciente'),
        url(r'^registrarse/confirmacion/$',RegisterSuccessView.as_view(), name='register-success'),
        url(r'^registrarse/confirmacionpaciente/$',RegisterSuccessViewPaciente.as_view(), name='register-success_paciente'),
        )	


