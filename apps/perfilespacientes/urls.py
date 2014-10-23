from django.conf.urls import patterns, include, url
from apps.inicio.views import *
from .views import *

urlpatterns = patterns('',

    #Estado animo
    url(r'^paciente/diariomedico/animo/$',IngresarEstadoAnimoPaciente.as_view(), name='ingresar_estado_animo_paciente'),
    url(r'^paciente/diariomedico/animo/listar/$',ListarEstadoAnimoPaciente.as_view(), name='listar_estado_animo_paciente'),
    url(r'^paciente/diariomedico/animo/eliminar/(?P<pk>\d+)/$',EliminarEstadoAnimoPaciente.as_view(), name='eliminar_estado_animo_paciente'),
    
    #Sintomas generales
    url(r'^paciente/diariomedico/sintomas/$',IngresarSintomaPaciente.as_view(), name='pacientes_sintomas_ingresar'),
    url(r'^paciente/diariomedico/sintomas/listar/$',ListarSintomaPaciente.as_view(), name='listar_sintomas_paciente'),
    url(r'^paciente/diariomedico/sintomas/actualizacion/(?P<pk>\d+)/$' ,EliminarSintomaPaciente.as_view(), name='eliminar_sintomas_paciente'),
   
    #Sintomas alteracion glicemica
    url(r'^paciente/diariomedico/sintomas/alteracion_glicemica/ingresar$',IngresarSintomaAlteracionGlicemicaPaciente.as_view(), name='ingresar_sintomas_alteracion_glicemica_paciente'),
    url(r'^paciente/diariomedico/sintomas/alteracion_glicemica/listar/$',ListarSintomaAlteracionGlicemicaPaciente.as_view(), name='listar_sintomas_alteracion_glicemica_paciente'),
    url(r'^paciente/diariomedico/sintomas/alteracion_glicemica/actualizacion/(?P<pk>\d+)/$' ,EliminarSintomaAlteracionGlicemicaPaciente.as_view(), name='eliminar_sintomas_alteracion_glicemica_paciente'),
    
    #Mediciones peso
    url(r'^paciente/diariomedico/mediciones/peso/ingresar$',IngresarPesoPaciente.as_view(), name='ingresar_peso_paciente'),
    url(r'^paciente/diariomedico/mediciones/peso/listar/$',ListarPesoPaciente.as_view(), name='listar_peso_paciente'),
    url(r'^paciente/diariomedico/mediciones/peso/actualizar/(?P<pk>\d+)/$',ActualizarPesoPaciente.as_view(), name='actualizar_peso_paciente'),
    url(r'^paciente/diariomedico/mediciones/peso/eliminar/(?P<pk>\d+)/$' ,EliminarPesoPaciente.as_view(), name='eliminar_peso_paciente'),
    
    #Mediciones talla
    url(r'^paciente/diariomedico/mediciones/talla/ingresar$',IngresarTallaPaciente.as_view(), name='ingresar_talla_paciente'),
    url(r'^paciente/diariomedico/mediciones/talla/listar/$',ListarTallaPaciente.as_view(), name='listar_talla_paciente'),
    url(r'^paciente/diariomedico/mediciones/talla/actualizar/(?P<pk>\d+)/$',ActualizarTallaPaciente.as_view(), name='actualizar_talla_paciente'),
    url(r'^paciente/diariomedico/mediciones/talla/eliminar/(?P<pk>\d+)/$' ,EliminarTallaPaciente.as_view(), name='eliminar_talla_paciente'),
    
    #Mediciones hemoglobina
    url(r'^paciente/diariomedico/mediciones/hemoglobina/ingresar$',IngresarHemoglobinaPaciente.as_view(), name='ingresar_hemoglobina_paciente'),
    url(r'^paciente/diariomedico/mediciones/hemoglobina/listar/$',ListarHemoglobinaPaciente.as_view(), name='listar_hemoglobina_paciente'),
    url(r'^paciente/diariomedico/mediciones/hemoglobina/actualizar/(?P<pk>\d+)/$',ActualizarHemoglobinaPaciente.as_view(), name='actualizar_hemoglobina_paciente'),
    url(r'^paciente/diariomedico/mediciones/hemoglobina/eliminar/(?P<pk>\d+)/$' ,EliminarHemoglobinaPaciente.as_view(), name='eliminar_hemoglobina_paciente'),
    
    #Mediciones colesterol
    url(r'^paciente/diariomedico/mediciones/colesterol/ingresar$',IngresarColesterolPaciente.as_view(), name='ingresar_colesterol_paciente'),
    url(r'^paciente/diariomedico/mediciones/colesterol/listar/$',ListarColesterolPaciente.as_view(), name='listar_colesterol_paciente'),
    url(r'^paciente/diariomedico/mediciones/colesterol/actualizar/(?P<pk>\d+)/$',ActualizarColesterolPaciente.as_view(), name='actualizar_colesterol_paciente'),
    url(r'^paciente/diariomedico/mediciones/colesterol/eliminar/(?P<pk>\d+)/$' ,EliminarColesterolPaciente.as_view(), name='eliminar_colesterol_paciente'),
    
    #Mediciones presion
    url(r'^paciente/diariomedico/mediciones/presion/ingresar$',IngresarPresionPaciente.as_view(), name='ingresar_presion_paciente'),
    url(r'^paciente/diariomedico/mediciones/presion/listar/$',ListarPresionPaciente.as_view(), name='listar_presion_paciente'),
    url(r'^paciente/diariomedico/mediciones/presion/actualizar/(?P<pk>\d+)/$',ActualizarPresionPaciente.as_view(), name='actualizar_presion_paciente'),
    url(r'^paciente/diariomedico/mediciones/presion/eliminar/(?P<pk>\d+)/$' ,EliminarPresionPaciente.as_view(), name='eliminar_presion_paciente'),
    
     #Mediciones glucoday
    url(r'^paciente/diariomedico/mediciones/gluco/ingresar$',IngresarGlucosaPaciente.as_view(), name='ingresar_gluco_paciente'),
    url(r'^paciente/diariomedico/mediciones/gluco/listar/$',ListarGlucosaPaciente.as_view(), name='listar_gluco_paciente'),
    url(r'^paciente/diariomedico/mediciones/gluco/actualizar/(?P<pk>\d+)/$',ActualizarGlucosaPaciente.as_view(), name='actualizar_gluco_paciente'),
    url(r'^paciente/diariomedico/mediciones/gluco/eliminar/(?P<pk>\d+)/$' ,EliminarGlucosaPaciente.as_view(), name='eliminar_gluco_paciente'),
    
    #Rutinas ejercicio
    url(r'^paciente/diariomedico/rutinas/ejercicio/ingresar$',IngresarRutinaEjercicioPaciente.as_view(), name='ingresar_ejercicio_paciente'),
    url(r'^paciente/diariomedico/rutinas/ejercicio/listar/$',ListarRutinaEjercicioPaciente.as_view(), name='listar_ejercicio_paciente'),
    url(r'^paciente/diariomedico/rutinas/ejercicio/actualizar/(?P<pk>\d+)/$',ActualizarRutinaEjercicioPaciente.as_view(), name='actualizar_ejercicio_paciente'),
    url(r'^paciente/diariomedico/rutinas/ejercicio/eliminar/(?P<pk>\d+)/$' ,EliminarRutinaEjercicioPaciente.as_view(), name='eliminar_ejercicio_paciente'),
    
    #Rutinas alimentacion
    url(r'^paciente/diariomedico/rutinas/alimentacion/ingresar$',IngresarRutinaAlimentacionPaciente.as_view(), name='ingresar_alimentacion_paciente'),
    url(r'^paciente/diariomedico/rutinas/alimentacion/listar/$',ListarRutinaAlimentacionPaciente.as_view(), name='listar_alimentacion_paciente'),
    url(r'^paciente/diariomedico/rutinas/alimentacion/actualizar/(?P<pk>\d+)/$',ActualizarRutinaAlimentacionPaciente.as_view(), name='actualizar_alimentacion_paciente'),
    url(r'^paciente/diariomedico/rutinas/alimentacion/eliminar/(?P<pk>\d+)/$' ,EliminarRutinaAlimentacionPaciente.as_view(), name='eliminar_alimentacion_paciente'),
    
    #Tratamientos medicamentos
    url(r'^paciente/diariomedico/tratamientos/medicamentos/ingresar$',IngresarMedicamentoPaciente.as_view(), name='ingresar_medicamento_paciente'),
    url(r'^paciente/diariomedico/tratamientos/medicamentos/listar/$',ListarMedicamentoPaciente.as_view(), name='listar_medicamento_paciente'),
    url(r'^paciente/diariomedico/tratamientos/medicamentos/actualizar/(?P<pk>\d+)/$',ActualizarMedicamentoPaciente.as_view(), name='actualizar_medicamento_paciente'),
    url(r'^paciente/diariomedico/tratamientos/medicamentos/eliminar/(?P<pk>\d+)/$' ,EliminarMedicamentoPaciente.as_view(), name='eliminar_medicamento_paciente'),
    
    #Tratamientos terapias
    url(r'^paciente/diariomedico/tratamientos/terapias/ingresar$',IngresarTerapiaPaciente.as_view(), name='ingresar_terapia_paciente'),
    url(r'^paciente/diariomedico/tratamientos/terapias/listar/$',ListarTerapiaPaciente.as_view(), name='listar_terapia_paciente'),
    url(r'^paciente/diariomedico/tratamientos/terapias/actualizar/(?P<pk>\d+)/$',ActualizarTerapiaPaciente.as_view(), name='actualizar_terapia_paciente'),
    url(r'^paciente/diariomedico/tratamientos/terapias/eliminar/(?P<pk>\d+)/$' ,EliminarTerapiaPaciente.as_view(), name='eliminar_terapia_paciente'),
    
    #Resultados examenes
    url(r'^paciente/diariomedico/resultados/laboratorio/ingresar$',IngresarResultadosLabPaciente.as_view(), name='ingresar_resultado_lab_paciente'),
    url(r'^paciente/diariomedico/resultados/laboratorio/listar/$',ListarResultadosLabPaciente.as_view(), name='listar_resultado_lab_paciente'),
    url(r'^paciente/diariomedico/resultados/laboratorio/actualizar/(?P<pk>\d+)/$',ActualizarResultadosLabPaciente.as_view(), name='actualizar_resultado_lab_paciente'),
    url(r'^paciente/diariomedico/resultados/laboratorio/eliminar/(?P<pk>\d+)/$' ,EliminarResultadosLabPaciente.as_view(), name='eliminar_resultado_lab_paciente'),
    
    #Citas
    url(r'^paciente/diariomedico/citas/ingresar$',IngresarCitaPaciente.as_view(), name='ingresar_cita_paciente'),
    url(r'^paciente/diariomedico/citas/listar/$',ListarCitaPaciente.as_view(), name='listar_cita_paciente'),
    url(r'^paciente/diariomedico/citas/actualizar/(?P<pk>\d+)/$',ActualizarCitaPaciente.as_view(), name='actualizar_cita_paciente'),
    url(r'^paciente/diariomedico/citas/eliminar/(?P<pk>\d+)/$' ,EliminarCitaPaciente.as_view(), name='eliminar_cita_paciente'),
    
    #Historia clinica resumen
    url(r'^paciente/diariomedico/historiaclinica/resumen/ingresar$',IngresarResumenClinicoPaciente.as_view(), name='ingresar_resumenclinico_paciente'),
    url(r'^paciente/diariomedico/historiaclinica/resumen/listar/$',ListarResumenClinicoPaciente.as_view(), name='listar_resumenclinico_paciente'),
    url(r'^paciente/diariomedico/historiaclinica/resumen/actualizar/(?P<pk>\d+)/$',ActualizarResumenClinicoPaciente.as_view(), name='actualizar_resumenclinico_paciente'),
    url(r'^paciente/diariomedico/historiaclinica/resumen/eliminar/(?P<pk>\d+)/$' ,EliminarResumenClinicoPaciente.as_view(), name='eliminar_resumenclinico_paciente'),
    
    #Historia clinica enfermedad 
    url(r'^paciente/diariomedico/historiaclinica/enfermedad/ingresar$',IngresarEnfermedadPaciente.as_view(), name='ingresar_enfermedad_paciente'),
    url(r'^paciente/diariomedico/historiaclinica/enfermedad/listar/$',ListarEnfermedadPaciente.as_view(), name='listar_enfermedad_paciente'),
    url(r'^paciente/diariomedico/historiaclinica/enfermedad/actualizar/(?P<pk>\d+)/$',ActualizarEnfermedadPaciente.as_view(), name='actualizar_enfermedad_paciente'),
    url(r'^paciente/diariomedico/historiaclinica/enfermedad/eliminar/(?P<pk>\d+)/$' ,EliminarEnfermedadPaciente.as_view(), name='eliminar_enfermedad_paciente'),
    
    #Historia clinica cirugias
    url(r'^paciente/diariomedico/historiaclinica/cirugias/ingresar$',IngresarCirugiaPaciente.as_view(), name='ingresar_cirugia_paciente'),
    url(r'^paciente/diariomedico/historiaclinica/cirugias/listar/$',ListarCirugiaPaciente.as_view(), name='listar_cirugia_paciente'),
    url(r'^paciente/diariomedico/historiaclinica/cirugias/actualizar/(?P<pk>\d+)/$',ActualizarCirugiaPaciente.as_view(), name='actualizar_cirugia_paciente'),
    url(r'^paciente/diariomedico/historiaclinica/cirugias/eliminar/(?P<pk>\d+)/$' ,EliminarCirugiaPaciente.as_view(), name='eliminar_cirugia_paciente'),
    
    #Historia clinica familiares
    url(r'^paciente/diariomedico/historiaclinica/familiares/ingresar$',IngresarFamiliarPaciente.as_view(), name='ingresar_familiar_paciente'),
    url(r'^paciente/diariomedico/historiaclinica/familiares/listar/$',ListarFamiliarPaciente.as_view(), name='listar_familiar_paciente'),
    url(r'^paciente/diariomedico/historiaclinica/familiares/actualizar/(?P<pk>\d+)/$',ActualizarFamiliarPaciente.as_view(), name='actualizar_familiar_paciente'),
    url(r'^paciente/diariomedico/historiaclinica/familiares/eliminar/(?P<pk>\d+)/$' ,EliminarFamiliarPaciente.as_view(), name='eliminar_familiar_paciente'),
    
     #Enfermedad Actual
    url(r'^paciente/diariomedico/historiaclinica/enfermedad_actual/ingresar$',IngresarEnfermedadActualPaciente.as_view(), name='ingresar_enfermedad_actual_paciente'),
    url(r'^paciente/diariomedico/historiaclinica/enfermedad_actual/listar/$',ListarEnfermedadActualPaciente.as_view(), name='listar_enfermedad_actual_paciente'),
    url(r'^paciente/diariomedico/historiaclinica/enfermedad_actual/actualizar/(?P<pk>\d+)/$',ActualizarEnfermedadActualPaciente.as_view(), name='actualizar_enfermedad_actual_paciente'),
    url(r'^paciente/diariomedico/historiaclinica/enfermedad_actual/eliminar/(?P<pk>\d+)/$' ,EliminarEnfermedadActualPaciente.as_view(), name='eliminar_enfermedad_actual_paciente'),
    
     #Historia Clinica Toxicos
    url(r'^paciente/diariomedico/historiaclinica/toxicos/ingresar$',IngresarToxicosPaciente.as_view(), name='ingresar_toxicos_paciente'),
    url(r'^paciente/diariomedico/historiaclinica/toxicos/listar/$',ListarToxicosPaciente.as_view(), name='listar_toxicos_paciente'),
    url(r'^paciente/diariomedico/historiaclinica/toxicos/actualizar/(?P<pk>\d+)/$',ActualizarToxicosPaciente.as_view(), name='actualizar_toxicos_paciente'),
    url(r'^paciente/diariomedico/historiaclinica/toxicos/eliminar/(?P<pk>\d+)/$' ,EliminarToxicosPaciente.as_view(), name='eliminar_toxicos_paciente'),
   
    #Historia Clinica Alergias
    url(r'^paciente/diariomedico/historiaclinica/alergias/ingresar$',IngresarAlergiasPaciente.as_view(), name='ingresar_alergias_paciente'),
    url(r'^paciente/diariomedico/historiaclinica/alergias/listar/$',ListarAlergiasPaciente.as_view(), name='listar_alergias_paciente'),
    url(r'^paciente/diariomedico/historiaclinica/alergias/actualizar/(?P<pk>\d+)/$',ActualizarAlergiasPaciente.as_view(), name='actualizar_alergias_paciente'),
    url(r'^paciente/diariomedico/historiaclinica/alergias/eliminar/(?P<pk>\d+)/$' ,EliminarAlergiasPaciente.as_view(), name='eliminar_alergias_paciente'),
    
     #Historia Clinica Inmunizacion
    url(r'^paciente/diariomedico/historiaclinica/inmunizacion/ingresar$',IngresarInmunizacionPaciente.as_view(), name='ingresar_inmunizacion_paciente'),
    url(r'^paciente/diariomedico/historiaclinica/inmunizacion/listar/$',ListarInmunizacionPaciente.as_view(), name='listar_inmunizacion_paciente'),
    url(r'^paciente/diariomedico/historiaclinica/inmunizacion/actualizar/(?P<pk>\d+)/$',ActualizarInmunizacionPaciente.as_view(), name='actualizar_inmunizacion_paciente'),
    url(r'^paciente/diariomedico/historiaclinica/inmunizacion/eliminar/(?P<pk>\d+)/$' ,EliminarInmunizacionPaciente.as_view(), name='eliminar_inmunizacion_paciente'),
    
    #Historia Clinica Medicamento Historial
    url(r'^paciente/diariomedico/historiaclinica/medicamento_historial/ingresar$',IngresarMedicamentoHistorialPaciente.as_view(), name='ingresar_medicamento_historial_paciente'),
    url(r'^paciente/diariomedico/historiaclinica/medicamento_historial/listar/$',ListarMedicamentoHistorialPaciente.as_view(), name='listar_medicamento_historial_paciente'),
    url(r'^paciente/diariomedico/historiaclinica/medicamento_historial/actualizar/(?P<pk>\d+)/$',ActualizarMedicamentoHistorialPaciente.as_view(), name='actualizar_medicamento_historial_paciente'),
    url(r'^paciente/diariomedico/historiaclinica/medicamento_historial/eliminar/(?P<pk>\d+)/$' ,EliminarMedicamentoHistorialPaciente.as_view(), name='eliminar_medicamento_historial_paciente'),
    
     #Historia Clinica Gineco Historial
    url(r'^paciente/diariomedico/historiaclinica/gineco_historial/ingresar$',IngresarGinecoHistorialPaciente.as_view(), name='ingresar_gineco_historial_paciente'),
    url(r'^paciente/diariomedico/historiaclinica/gineco_historial/listar/$',ListarGinecoHistorialPaciente.as_view(), name='listar_gineco_historial_paciente'),
    url(r'^paciente/diariomedico/historiaclinica/gineco_historial/actualizar/(?P<pk>\d+)/$',ActualizarGinecoHistorialPaciente.as_view(), name='actualizar_gineco_historial_paciente'),
    url(r'^paciente/diariomedico/historiaclinica/gineco_historial/eliminar/(?P<pk>\d+)/$' ,EliminarGinecoHistorialPaciente.as_view(), name='eliminar_gineco_historial_paciente'),
    
    #Historia Clinica Gineco diario
    url(r'^paciente/diariomedico/historiaclinica/gineco_diario/ingresar$',IngresarGinecoDiarioPaciente.as_view(), name='ingresar_gineco_diario_paciente'),
    url(r'^paciente/diariomedico/historiaclinica/gineco_diario/listar/$',ListarGinecoDiarioPaciente.as_view(), name='listar_gineco_diario_paciente'),
    url(r'^paciente/diariomedico/historiaclinica/gineco_diario/actualizar/(?P<pk>\d+)/$',ActualizarGinecoDiarioPaciente.as_view(), name='actualizar_gineco_diario_paciente'),
    url(r'^paciente/diariomedico/historiaclinica/gineco_diario/eliminar/(?P<pk>\d+)/$' ,EliminarGinecoDiarioPaciente.as_view(), name='eliminar_gineco_diario_paciente'),
    
     #Hub Salud Clubes
    url(r'^paciente/hubsalud/clubes/ingresar$',IngresarClubPaciente.as_view(), name='ingresar_club_paciente'),
    url(r'^paciente/hubsalud/clubes/listar/$',ListarClubPaciente.as_view(), name='listar_club_paciente'),
    url(r'^paciente/hubsalud/clubes/actualizar/(?P<pk>\d+)/$',ActualizarClubPaciente.as_view(), name='actualizar_club_paciente'),
    url(r'^paciente/hubsalud/clubes/eliminar/(?P<pk>\d+)/$' ,EliminarClubPaciente.as_view(), name='eliminar_club_paciente'),
    
    url(r'^paciente/perfilbasico/$' ,'apps.perfilespacientes.views.perfil_basico', name='perfil_basico_paciente'),
    url(r'^paciente/perfilbasico/contacto/$' ,'apps.perfilespacientes.views.perfil_basico_contactos', name='perfil_basico_contactos_paciente'),
    url(r'^paciente/perfilbasico/social/$' ,'apps.perfilespacientes.views.perfil_basico_social', name='perfil_basico_social_paciente'),

    #url(r'^paciente/perfilbasico/principal$' ,PerfilPrincipalPaciente.as_view(), name='perfil_principal_paciente'),
    #url(r'^paciente/perfilbasico/principal/$' ,'apps.perfilespacientes.views.perfil_basico', name='perfil_principal_paciente'),
    url(r'^paciente/perfilbasico/principal/$' ,'apps.perfilespacientes.views.perfil_principal_paciente_home', name='perfil_principal_paciente'),

)