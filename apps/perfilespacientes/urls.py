from django.conf.urls import patterns, include, url
from apps.inicio.views import *
from .views import *

urlpatterns = patterns('',

    #url(r'^pacientes/',LoginViewPacientes.as_view(), name='loginPacientes'),
    #url(r'^pacientes/',PacientesPerfilBasico.as_view(),name='pacientes_perfil_basico'),
    #url(r'^paciente/perfilbasico/',PacientesPerfilBasico.as_view(), name='pacientes_perfil_basico'),
    url(r'^paciente/perfilbasico/$' ,'apps.perfilespacientes.views.perfil_basico', name='perfil_basico_paciente'),
    url(r'^paciente/perfilbasico/contacto/$' ,'apps.perfilespacientes.views.perfil_basico_contactos', name='perfil_basico_contactos_paciente'),


)