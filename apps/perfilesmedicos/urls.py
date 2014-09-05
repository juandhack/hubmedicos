from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = patterns('',

	url(r'^home/$' ,'apps.perfilesmedicos.views.user_profile', name='profile'),
        url(r'^home/profesional/$' ,IngresarInfoProfesional.as_view(), name='crear_info_profesional'),
        url(r'^home/profesional/listados/$' ,ListarInfoProfesional.as_view(), name='listar_info_profesional'),
        url(r'^home/profesional/actualizacion/(?P<pk>\d+)/$' ,ActualizarInfoProfesional.as_view(), name='actualizar_info_profesional'),
        url(r'^home/profesional/eliminacion/(?P<pk>\d+)/$' ,EliminarInfoProfesional.as_view(), name='eliminar_info_profesional'),
        url(r'^home/academico/$' ,IngresarInfoAcademica.as_view(), name='crear_info_academica'),
        url(r'^home/academico/listados/$' ,ListarInfoAcademica.as_view(), name='listar_info_academica'),
        url(r'^home/academico/actualizacion/(?P<pk>\d+)/$' ,ActualizarInfoAcademica.as_view(), name='actualizar_info_academica'),
        url(r'^home/academico/eliminacion/(?P<pk>\d+)/$' ,EliminarInfoAcademica.as_view(), name='eliminar_info_academica'),
        url(r'^home/servicios/creacion$' ,IngresarInfoServicios.as_view(), name='crear_info_servicios'),
        url(r'^home/servicios/listados/$' ,ListarInfoServicios.as_view(), name='listar_info_servicios'),
        url(r'^home/servicios/actualizacion/(?P<pk>\d+)/$' ,ActualizarInfoServicios.as_view(), name='actualizar_info_servicios'),
        url(r'^home/servicios/eliminacion/(?P<pk>\d+)/$' ,EliminarInfoServicios.as_view(), name='eliminar_info_servicios'),
	url(r'^home/contacto/$' ,'apps.perfilesmedicos.views.user_contactos', name='contacto'),
	#url(r'^home/academico/$' ,'apps.perfilesmedicos.views.user_academico', name='academico'),
	#url(r'^home/profesional/$' ,'apps.perfilesmedicos.views.user_profesional', name='profesional'),
	url(r'^home/social/$' ,'apps.perfilesmedicos.views.user_social', name='social'),
        #url(r'^home/consultas/$' ,'apps.perfilesmedicos.views.consultas', name='consultas'),
        url(r'^home/pr/creacion/$' ,IngresarPregunta.as_view(), name='crear_pregunta'),
        url(r'^home/pr/visualizacion/(?P<pk>\d+)/$' ,VisualizarPregunta.as_view(), name='visualizar_pregunta'),
        url(r'^home/pr/actualizacion/(?P<pk>\d+)/$' ,ActualizarPregunta.as_view(), name='actualizar_pregunta'),
        url(r'^home/pr/eliminacion/(?P<pk>\d+)/$' ,EliminarPregunta.as_view(), name='eliminar_pregunta'),
        url(r'^home/pr/listados/$' ,ListarPreguntas.as_view(), name='listar_preguntas'),
	url(r'^home/perfilpublico/(?P<userid>(\d)+)/$' ,'apps.perfilesmedicos.views.user_perfil_publico', name='social'),
	url(r'^home/pacientes/$',PacientesHome.as_view()),
	url(r'^home/pr/$',PacientesHome.as_view()),
    #url(r'^tarjeta/$' ,Tarjeta.as_view(), name='tarjeta'),

)