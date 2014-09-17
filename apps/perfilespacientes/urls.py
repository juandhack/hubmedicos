from django.conf.urls import patterns, include, url
from apps.inicio.views import *
from .views import *

urlpatterns = patterns('',

    #url(r'^pacientes/',LoginViewPacientes.as_view(), name='loginPacientes'),
    #url(r'^pacientes/',PacientesPerfilBasico.as_view(),name='pacientes_perfil_basico'),
    url(r'^paciente/diariomedico/sintomas/$',SintomasActualesPaciente.as_view(), name='pacientes_sintomas_actuales'),
    url(r'^paciente/diariomedico/animo/$',EstadoAnimoPaciente.as_view(), name='pacientes_estado_animo'),
    url(r'^paciente/diariomedico/mediciones/$',MedicionesPaciente.as_view(), name='pacientes_mediciones'),
    url(r'^paciente/diariomedico/rutinas/$',RutinasPaciente.as_view(), name='pacientes_rutinas'),
    url(r'^paciente/diariomedico/tratamientos/$',TratamientosPaciente.as_view(), name='pacientes_tratamientos'),
    url(r'^paciente/diariomedico/resultados/$',ResultadosExamenesPaciente.as_view(), name='pacientes_resultados'),
    url(r'^paciente/diariomedico/citas/$',ProximasCitasPaciente.as_view(), name='pacientes_proximas_citas'),
    url(r'^paciente/historiaclinica/resumen/$',ResumenClinicoPaciente.as_view(), name='resumen_clinico_pacientes'),
    url(r'^paciente/historiaclinica/enfermedades/$',EnfermedadesPaciente.as_view(), name='enfermedades_pacientes'),
    url(r'^paciente/historiaclinica/antecedentes/$',AntecedentesPaciente.as_view(), name='antecedentes_pacientes'),
    url(r'^paciente/historiaclinica/diagnosticos/$',DiagnosticoPaciente.as_view(), name='diagnostico_pacientes'),
    url(r'^paciente/hubsalud/clubes/$',ClubesPaciente.as_view(), name='clubes_pacientes'),
    url(r'^paciente/hubsalud/medicos/$',MedicosPaciente.as_view(), name='medicos_pacientes'),
    url(r'^paciente/perfilbasico/$' ,'apps.perfilespacientes.views.perfil_basico', name='perfil_basico_paciente'),
    url(r'^paciente/perfilbasico/contacto/$' ,'apps.perfilespacientes.views.perfil_basico_contactos', name='perfil_basico_contactos_paciente'),
    url(r'^paciente/perfilbasico/social/$' ,'apps.perfilespacientes.views.perfil_basico_social', name='perfil_basico_social_paciente'),


)