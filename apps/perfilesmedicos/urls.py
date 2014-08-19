from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = patterns('',

	url(r'^home/$' ,'apps.perfilesmedicos.views.user_profile', name='profile'),
	url(r'^home/contacto/$' ,'apps.perfilesmedicos.views.user_contactos', name='contacto'),
	url(r'^home/academico/$' ,'apps.perfilesmedicos.views.user_academico', name='academico'),
	url(r'^home/profesional/$' ,'apps.perfilesmedicos.views.user_profesional', name='profesional'),
	url(r'^home/social/$' ,'apps.perfilesmedicos.views.user_social', name='social'),
	url(r'^home/perfilpublico/(?P<userid>(\d)+)/$' ,'apps.perfilesmedicos.views.user_perfil_publico', name='social'),
	url(r'^home/pacientes/$',pacienteshome.as_view()),
	url(r'^home/pr/$',pacienteshome.as_view()),
    #url(r'^tarjeta/$' ,Tarjeta.as_view(), name='tarjeta'),

)