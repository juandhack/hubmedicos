from django.views.generic import TemplateView,FormView
from .forms import *
from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import render, render_to_response, RequestContext, get_object_or_404
from django.http import HttpResponseRedirect, HttpRequest
from django.core.context_processors import csrf
from .models import *
from django.contrib.auth.decorators import login_required
from django.views.generic.base import *
from django.views.generic.edit import *
from django.views.generic import *
from django.template import RequestContext
from django.contrib.auth.models import User

# Create your views here.        
    
class PerfilPrincipalPaciente(TemplateView):
    template_name = 'pacientes/perfil/perfil_principal.html'
    
class RutinasPaciente(TemplateView):
    template_name = 'pacientes/rutinas/mis_rutinas_salud_form.html'
    
class TratamientosPaciente(TemplateView):
    template_name = 'pacientes/tratamientos/mis_tratamientos_form.html'
    
class ResultadosExamenesPaciente(TemplateView):
    template_name = 'pacientes/resultados_examenes/mis_resultados_examenes_form.html'
    
class ProximasCitasPaciente(TemplateView):
    template_name = 'pacientes/citas/mis_proximas_citas_form.html'
    
class ResumenClinicoPaciente(TemplateView):
    template_name = 'pacientes/historiaclinica_cuentanos_form.html'
    
class EnfermedadesPaciente(TemplateView):
    template_name = 'pacientes/historiaclinica_enfermedades_form.html'
    
class AntecedentesPaciente(TemplateView):
    template_name = 'pacientes/historiaclinica_antecedentes_form.html'
    
class DiagnosticoPaciente(TemplateView):
    template_name = 'pacientes/historiaclinica_diagnosticos_form.html'
    
class ClubesPaciente(TemplateView):
    template_name = 'pacientes/hubsalud_clubes_form.html'
    
class MedicosPaciente(TemplateView):
    template_name = 'pacientes/hubsalud_medicos_form.html'
    
  
#-------------Sintomas----------------------------------------------------------------------#  
class IngresarSintomaPaciente(CreateView):
    template_name = 'pacientes/sintomas/mis_sintomas_form.html'
    form_class = SintomasGeneralesPacienteForm
    model = SintomasGeneralesPaciente
    def form_valid(self,form):
	self.object = form.save(commit=False)
	self.object.user = self.request.user
	self.object.save()
	return super(IngresarSintomaPaciente,self).form_valid(form)
    success_url = reverse_lazy('listar_sintomas_paciente')   
    
class ListarSintomaPaciente(ListView):
    template_name = 'pacientes/sintomas/mis_sintomas_listar_form.html'
    form_class = SintomasGeneralesPacienteForm
    #model = SintomasGeneralesPaciente
    success_url = reverse_lazy('listar_sintomas_paciente')
    
    def get_queryset(self):
        return SintomasGeneralesPaciente.objects.filter(user_id = self.request.user)
    
class ActualizarSintomaPaciente(UpdateView):
    template_name = 'pacientes/sintomas/mis_sintomas_form.html'
    form_class = SintomasGeneralesPacienteForm
    model = SintomasGeneralesPaciente
    def form_valid(self,form):
	self.object = form.save(commit=False)
	self.object.user = self.request.user
	self.object.save()
	return super(ActualizarSintomaPaciente,self).form_valid(form)
    success_url = reverse_lazy('listar_sintomas_paciente')
    
class EliminarSintomaPaciente(DeleteView):
    template_name = 'pacientes/sintomas/mis_sintomas_confirmar_delete_form.html'
    model = SintomasGeneralesPaciente
    success_url = reverse_lazy('listar_sintomas_paciente')
 
    
#-------------Sintomas Alteracion Glicemica-------------------------------------------------------------#  
class IngresarSintomaAlteracionGlicemicaPaciente(CreateView):
    template_name = 'pacientes/sintomas/alteracionglicemica/mis_sintomas_alteracion_glicemica_form.html'
    form_class = SintomaAlteracionGlicemicaPacienteForm
    model = SintomasAlteracionGlicemicaPaciente
    def form_valid(self,form):
	self.object = form.save(commit=False)
	self.object.user = self.request.user
	self.object.save()
	return super(IngresarSintomaAlteracionGlicemicaPaciente,self).form_valid(form)
    success_url = reverse_lazy('listar_sintomas_alteracion_glicemica_paciente')   
    
class ListarSintomaAlteracionGlicemicaPaciente(ListView):
    template_name = 'pacientes/sintomas/alteracionglicemica/mis_sintomas_alteracion_glicemica_listar_form.html'
    form_class = SintomaAlteracionGlicemicaPacienteForm
    #model = SintomasAlteracionGlicemicaPaciente
    success_url = reverse_lazy('listar_sintomas_alteracion_glicemica_paciente')
    
    def get_queryset(self):
        return SintomasAlteracionGlicemicaPaciente.objects.filter(user_id = self.request.user)
    
class ActualizarSintomaAlteracionGlicemicaPaciente(UpdateView):
    template_name = 'pacientes/sintomas/alteracionglicemica/mis_sintomas_alteracion_glicemica_form.html'
    form_class = SintomaAlteracionGlicemicaPacienteForm
    model = SintomasAlteracionGlicemicaPaciente
    def form_valid(self,form):
	self.object = form.save(commit=False)
	self.object.user = self.request.user
	self.object.save()
	return super(ActualizarSintomaAlteracionGlicemicaPaciente,self).form_valid(form)
    success_url = reverse_lazy('listar_sintomas_alteracion_glicemica_paciente')
    
class EliminarSintomaAlteracionGlicemicaPaciente(DeleteView):
    template_name = 'pacientes/sintomas/alteracionglicemica/mis_sintomas_alteracion_glicemica_confirmar_delete_form.html'
    model = SintomasAlteracionGlicemicaPaciente
    success_url = reverse_lazy('listar_sintomas_alteracion_glicemica_paciente')
    
#----------Estado de Animo -------------------------------------------------------- 
class IngresarEstadoAnimoPaciente(CreateView):
    template_name = 'pacientes/estado_animo/mi_estado_animo_form.html'
    form_class = EstadoAnimoPacienteForm
    model = EstadosAnimoPaciente
    def form_valid(self,form):
	self.object = form.save(commit=False)
	self.object.user = self.request.user
	self.object.save()
	return super(IngresarEstadoAnimoPaciente,self).form_valid(form)
    success_url = reverse_lazy('listar_estado_animo_paciente') 
        
class ListarEstadoAnimoPaciente(ListView):
    template_name = 'pacientes/estado_animo/mi_estado_animo_listar_form.html'
    form_class = EstadoAnimoPacienteForm
    #model = EstadosAnimoPaciente
    success_url = reverse_lazy('listar_estado_animo_paciente')
    
    def get_queryset(self):
        return EstadosAnimoPaciente.objects.filter(user_id = self.request.user)
    
class ActualizarEstadoAnimoPaciente(UpdateView):
    template_name = 'pacientes/estado_animo/mi_estado_animo_form.html'
    form_class = EstadoAnimoPacienteForm
    model = EstadosAnimoPaciente
    def form_valid(self,form):
	self.object = form.save(commit=False)
	self.object.user = self.request.user
	self.object.save()
	return super(ActualizarEstadoAnimoPaciente,self).form_valid(form)
    success_url = reverse_lazy('listar_estado_animo_paciente')
    
class EliminarEstadoAnimoPaciente(DeleteView):
    template_name = 'pacientes/estado_animo/mi_estado_animo_confirmar_delete_form.html'
    model = EstadosAnimoPaciente
    success_url = reverse_lazy('listar_estado_animo_paciente')
  
#----------Mediciones - Peso -----------------------------------------------------------------# 
class IngresarPesoPaciente(CreateView):
    template_name = 'pacientes/medicionesclinicas/peso/mis_mediciones_clinicas_peso_form.html'
    form_class = PesoPacienteForm
    model = Peso
    def form_valid(self,form):
	self.object = form.save(commit=False)
	self.object.user = self.request.user
	self.object.save()
	return super(IngresarPesoPaciente,self).form_valid(form)
    success_url = reverse_lazy('listar_peso_paciente') 
     
class ListarPesoPaciente(ListView):
    template_name = 'pacientes/medicionesclinicas/peso/mis_mediciones_clinicas_peso_listar_form.html'
    form_class = PesoPacienteForm
    #model = Peso
    success_url = reverse_lazy('listar_peso_paciente')
    
    def get_queryset(self):
        return Peso.objects.filter(user_id = self.request.user)
    
class ActualizarPesoPaciente(UpdateView):
    template_name = 'pacientes/medicionesclinicas/peso/mis_mediciones_clinicas_peso_form.html'
    form_class = PesoPacienteForm
    model = Peso
    def form_valid(self,form):
	self.object = form.save(commit=False)
	self.object.user = self.request.user
	self.object.save()
	return super(ActualizarPesoPaciente,self).form_valid(form)
    success_url = reverse_lazy('listar_peso_paciente')
    
class EliminarPesoPaciente(DeleteView):
    template_name = 'pacientes/medicionesclinicas/peso/mis_mediciones_clinicas_peso_confirmar_delete_form.html'
    model = Peso
    success_url = reverse_lazy('listar_peso_paciente')
   
#----------Mediciones - Talla -----------------------------------------------------------------# 
class IngresarTallaPaciente(CreateView):
    template_name = 'pacientes/medicionesclinicas/talla/mis_mediciones_clinicas_talla_form.html'
    form_class = TallaPacienteForm
    model = Talla
    def form_valid(self,form):
	self.object = form.save(commit=False)
	self.object.user = self.request.user
	self.object.save()
	return super(IngresarTallaPaciente,self).form_valid(form)
    success_url = reverse_lazy('listar_talla_paciente') 
     
class ListarTallaPaciente(ListView):
    template_name = 'pacientes/medicionesclinicas/talla/mis_mediciones_clinicas_talla_listar_form.html'
    form_class = TallaPacienteForm
    #model = Talla
    success_url = reverse_lazy('listar_talla_paciente')
    
    def get_queryset(self):
        return Talla.objects.filter(user_id = self.request.user)
    
class ActualizarTallaPaciente(UpdateView):
    template_name = 'pacientes/medicionesclinicas/talla/mis_mediciones_clinicas_talla_form.html'
    form_class = TallaPacienteForm
    model = Talla
    def form_valid(self,form):
	self.object = form.save(commit=False)
	self.object.user = self.request.user
	self.object.save()
	return super(ActualizarTallaPaciente,self).form_valid(form)
    success_url = reverse_lazy('listar_talla_paciente')
    
class EliminarTallaPaciente(DeleteView):
    template_name = 'pacientes/medicionesclinicas/talla/mis_mediciones_clinicas_talla_confirmar_delete_form.html'
    model = Talla
    success_url = reverse_lazy('listar_talla_paciente')
    
#----------Mediciones - hemoglobina -----------------------------------------------------------------# 
class IngresarHemoglobinaPaciente(CreateView):
    template_name = 'pacientes/medicionesclinicas/hemoglobina/mis_mediciones_clinicas_hemoglobina_form.html'
    form_class = HemoglobinaPacienteForm
    model = Hemoglobina
    def form_valid(self,form):
	self.object = form.save(commit=False)
	self.object.user = self.request.user
	self.object.save()
	return super(IngresarHemoglobinaPaciente,self).form_valid(form)
    success_url = reverse_lazy('listar_hemoglobina_paciente') 
     
class ListarHemoglobinaPaciente(ListView):
    template_name = 'pacientes/medicionesclinicas/hemoglobina/mis_mediciones_clinicas_hemoglobina_listar_form.html'
    form_class = HemoglobinaPacienteForm
    #model = Hemoglobina
    success_url = reverse_lazy('listar_hemoglobina_paciente')
    
    def get_queryset(self):
        return Hemoglobina.objects.filter(user_id = self.request.user)
    
class ActualizarHemoglobinaPaciente(UpdateView):
    template_name = 'pacientes/medicionesclinicas/hemoglobina/mis_mediciones_clinicas_hemoglobina_form.html'
    form_class = HemoglobinaPacienteForm
    model = Hemoglobina
    def form_valid(self,form):
	self.object = form.save(commit=False)
	self.object.user = self.request.user
	self.object.save()
	return super(ActualizarHemoglobinaPaciente,self).form_valid(form)
    success_url = reverse_lazy('listar_hemoglobina_paciente')
    
class EliminarHemoglobinaPaciente(DeleteView):
    template_name = 'pacientes/medicionesclinicas/hemoglobina/mis_mediciones_clinicas_hemoglobina_confirmar_delete_form.html'
    model = Hemoglobina
    success_url = reverse_lazy('listar_hemoglobina_paciente')
    

#----------Mediciones - Colesterol -----------------------------------------------------------------# 
class IngresarColesterolPaciente(CreateView):
    template_name = 'pacientes/medicionesclinicas/colesterol/mis_mediciones_clinicas_colesterol_form.html'
    form_class = ColesterolPacienteForm
    model = Colesterol
    def form_valid(self,form):
	self.object = form.save(commit=False)
	self.object.user = self.request.user
	self.object.save()
	return super(IngresarColesterolPaciente,self).form_valid(form)
    success_url = reverse_lazy('listar_colesterol_paciente') 
     
class ListarColesterolPaciente(ListView):
    template_name = 'pacientes/medicionesclinicas/colesterol/mis_mediciones_clinicas_colesterol_listar_form.html'
    form_class = ColesterolPacienteForm
    #model = Colesterol
    success_url = reverse_lazy('listar_colesterol_paciente')
    
    def get_queryset(self):
        return Colesterol.objects.filter(user_id = self.request.user)
    
class ActualizarColesterolPaciente(UpdateView):
    template_name = 'pacientes/medicionesclinicas/colesterol/mis_mediciones_clinicas_colesterol_form.html'
    form_class = ColesterolPacienteForm
    model = Colesterol
    def form_valid(self,form):
	self.object = form.save(commit=False)
	self.object.user = self.request.user
	self.object.save()
	return super(ActualizarColesterolPaciente,self).form_valid(form)
    success_url = reverse_lazy('listar_colesterol_paciente')
    
class EliminarColesterolPaciente(DeleteView):
    template_name = 'pacientes/medicionesclinicas/colesterol/mis_mediciones_clinicas_colesterol_confirmar_delete_form.html'
    model = Colesterol
    success_url = reverse_lazy('listar_colesterol_paciente')



#----------Mediciones - Presion -----------------------------------------------------------------# 
class IngresarPresionPaciente(CreateView):
    template_name = 'pacientes/medicionesclinicas/presion/mis_mediciones_clinicas_presion_form.html'
    form_class = PresionPacienteForm
    model = Presion
    def form_valid(self,form):
	self.object = form.save(commit=False)
	self.object.user = self.request.user
	self.object.save()
	return super(IngresarPresionPaciente,self).form_valid(form)
    success_url = reverse_lazy('listar_presion_paciente') 
     
class ListarPresionPaciente(ListView):
    template_name = 'pacientes/medicionesclinicas/presion/mis_mediciones_clinicas_presion_listar_form.html'
    form_class = PresionPacienteForm
    #model = Presion
    success_url = reverse_lazy('listar_presion_paciente')
    
    def get_queryset(self):
        return Presion.objects.filter(user_id = self.request.user)
    
class ActualizarPresionPaciente(UpdateView):
    template_name = 'pacientes/medicionesclinicas/presion/mis_mediciones_clinicas_presion_form.html'
    form_class = PresionPacienteForm
    model = Presion
    def form_valid(self,form):
	self.object = form.save(commit=False)
	self.object.user = self.request.user
	self.object.save()
	return super(ActualizarPresionPaciente,self).form_valid(form)
    success_url = reverse_lazy('listar_presion_paciente')
    
class EliminarPresionPaciente(DeleteView):
    template_name = 'pacientes/medicionesclinicas/presion/mis_mediciones_clinicas_presion_confirmar_delete_form.html'
    model = Presion
    success_url = reverse_lazy('listar_presion_paciente')


#----------Mediciones - Glucosa -----------------------------------------------------------------# 
class IngresarGlucosaPaciente(CreateView):
    template_name = 'pacientes/medicionesclinicas/gluco/mis_mediciones_clinicas_gluco_form.html'
    form_class = GlucosaPacienteForm
    model = Glucemia
    def form_valid(self,form):
	self.object = form.save(commit=False)
	self.object.user = self.request.user
	self.object.save()
	return super(IngresarGlucosaPaciente,self).form_valid(form)
    success_url = reverse_lazy('listar_gluco_paciente') 
     
class ListarGlucosaPaciente(ListView):
    template_name = 'pacientes/medicionesclinicas/gluco/mis_mediciones_clinicas_gluco_listar_form.html'
    form_class = GlucosaPacienteForm
    #model = Glucemia
    success_url = reverse_lazy('listar_gluco_paciente')
    
    def get_queryset(self):
        return Glucemia.objects.filter(user_id = self.request.user)
    
class ActualizarGlucosaPaciente(UpdateView):
    template_name = 'pacientes/medicionesclinicas/gluco/mis_mediciones_clinicas_gluco_form.html'
    form_class = GlucosaPacienteForm
    model = Glucemia
    def form_valid(self,form):
	self.object = form.save(commit=False)
	self.object.user = self.request.user
	self.object.save()
	return super(ActualizarGlucosaPaciente,self).form_valid(form)
    success_url = reverse_lazy('listar_gluco_paciente')
    
class EliminarGlucosaPaciente(DeleteView):
    template_name = 'pacientes/medicionesclinicas/gluco/mis_mediciones_clinicas_gluco_confirmar_delete_form.html'
    model = Glucemia
    success_url = reverse_lazy('listar_gluco_paciente')
    

#----------Rutinas - Ejercicio -----------------------------------------------------------------# 
class IngresarRutinaEjercicioPaciente(CreateView):
    template_name = 'pacientes/rutinas/mis_rutinas_ejercicio_form.html'
    form_class = RutinaEjercicioPacienteForm
    model = RutinaEjercicio
    def form_valid(self,form):
	self.object = form.save(commit=False)
	self.object.user = self.request.user
	self.object.save()
	return super(IngresarRutinaEjercicioPaciente,self).form_valid(form)
    success_url = reverse_lazy('listar_ejercicio_paciente') 
     
class ListarRutinaEjercicioPaciente(ListView):
    template_name = 'pacientes/rutinas/mis_rutinas_ejercicio_listar_form.html'
    form_class = RutinaEjercicioPacienteForm
    #model = RutinaEjercicio
    success_url = reverse_lazy('listar_ejercicio_paciente')
    
    def get_queryset(self):
        return RutinaEjercicio.objects.filter(user_id = self.request.user)
    
class ActualizarRutinaEjercicioPaciente(UpdateView):
    template_name = 'pacientes/rutinas/mis_rutinas_ejercicio_form.html'
    form_class = RutinaEjercicioPacienteForm
    model = RutinaEjercicio
    def form_valid(self,form):
	self.object = form.save(commit=False)
	self.object.user = self.request.user
	self.object.save()
	return super(ActualizarRutinaEjercicioPaciente,self).form_valid(form)
    success_url = reverse_lazy('listar_ejercicio_paciente')
    
class EliminarRutinaEjercicioPaciente(DeleteView):
    template_name = 'pacientes/rutinas/mis_rutinas_ejercicio_confirmar_delete_form.html'
    model = RutinaEjercicio
    success_url = reverse_lazy('listar_ejercicio_paciente')
    
    
#----------Rutinas - Alimentacion -----------------------------------------------------------------# 
class IngresarRutinaAlimentacionPaciente(CreateView):
    template_name = 'pacientes/rutinas/mis_rutinas_alimentacion_form.html'
    form_class = RutinaAlimentacionPacienteForm
    model = RutinaAlimentacion
    def form_valid(self,form):
	self.object = form.save(commit=False)
	self.object.user = self.request.user
	self.object.save()
	return super(IngresarRutinaAlimentacionPaciente,self).form_valid(form)
    success_url = reverse_lazy('listar_alimentacion_paciente') 
     
class ListarRutinaAlimentacionPaciente(ListView):
    template_name = 'pacientes/rutinas/mis_rutinas_alimentacion_listar_form.html'
    form_class = RutinaAlimentacionPacienteForm
    #model = RutinaAlimentacion
    success_url = reverse_lazy('listar_alimentacion_paciente')
    
    def get_queryset(self):
        return RutinaAlimentacion.objects.filter(user_id = self.request.user)
    
class ActualizarRutinaAlimentacionPaciente(UpdateView):
    template_name = 'pacientes/rutinas/mis_rutinas_alimentacion_form.html'
    form_class = RutinaAlimentacionPacienteForm
    model = RutinaAlimentacion
    def form_valid(self,form):
	self.object = form.save(commit=False)
	self.object.user = self.request.user
	self.object.save()
	return super(ActualizarRutinaAlimentacionPaciente,self).form_valid(form)
    success_url = reverse_lazy('listar_alimentacion_paciente')
    
class EliminarRutinaAlimentacionPaciente(DeleteView):
    template_name = 'pacientes/rutinas/mis_rutinas_alimentacion_confirmar_delete_form.html'
    model = RutinaAlimentacion
    success_url = reverse_lazy('listar_alimentacion_paciente')


#----------Tratamientos - Medicamentos -----------------------------------------------------------------# 
class IngresarMedicamentoPaciente(CreateView):
    template_name = 'pacientes/tratamientos/mis_medicamentos_form.html'
    form_class = MedicamentoPacienteForm
    model = Medicamento
    def form_valid(self,form):
	self.object = form.save(commit=False)
	self.object.user = self.request.user
	self.object.save()
	return super(IngresarMedicamentoPaciente,self).form_valid(form)
    success_url = reverse_lazy('listar_medicamento_paciente') 
     
class ListarMedicamentoPaciente(ListView):
    template_name = 'pacientes/tratamientos/mis_tratamientos_listar_medicamentos_form.html'
    form_class = MedicamentoPacienteForm
    #model = Medicamento
    success_url = reverse_lazy('listar_medicamento_paciente')
    
    def get_queryset(self):
        return Medicamento.objects.filter(user_id = self.request.user)
    
class ActualizarMedicamentoPaciente(UpdateView):
    template_name = 'pacientes/tratamientos/mis_medicamentos_form.html'
    form_class = MedicamentoPacienteForm
    model = Medicamento
    def form_valid(self,form):
	self.object = form.save(commit=False)
	self.object.user = self.request.user
	self.object.save()
	return super(ActualizarMedicamentoPaciente,self).form_valid(form)
    success_url = reverse_lazy('listar_medicamento_paciente')
    
class EliminarMedicamentoPaciente(DeleteView):
    template_name = 'pacientes/tratamientos/mis_medicamentos_confirmar_delete_form.html'
    model = Medicamento
    success_url = reverse_lazy('listar_medicamento_paciente')
    


#----------Tratamientos - Terapias -----------------------------------------------------------------# 
class IngresarTerapiaPaciente(CreateView):
    template_name = 'pacientes/tratamientos/mis_terapias_form.html'
    form_class = TerapiaPacienteForm
    model = Terapia
    def form_valid(self,form):
	self.object = form.save(commit=False)
	self.object.user = self.request.user
	self.object.save()
	return super(IngresarTerapiaPaciente,self).form_valid(form)
    success_url = reverse_lazy('listar_terapia_paciente') 
     
class ListarTerapiaPaciente(ListView):
    template_name = 'pacientes/tratamientos/mis_tratamientos_listar_terapias_form.html'
    form_class = TerapiaPacienteForm
    #model = Terapia
    success_url = reverse_lazy('listar_terapia_paciente')
    
    def get_queryset(self):
        return Terapia.objects.filter(user_id = self.request.user)
    
class ActualizarTerapiaPaciente(UpdateView):
    template_name = 'pacientes/tratamientos/mis_terapias_form.html'
    form_class = TerapiaPacienteForm
    model = Terapia
    def form_valid(self,form):
	self.object = form.save(commit=False)
	self.object.user = self.request.user
	self.object.save()
	return super(ActualizarTerapiaPaciente,self).form_valid(form)
    success_url = reverse_lazy('listar_terapia_paciente')
    
class EliminarTerapiaPaciente(DeleteView):
    template_name = 'pacientes/tratamientos/mis_terapias_confirmar_delete_form.html'
    model = Terapia
    success_url = reverse_lazy('listar_terapia_paciente')    


#----------Resultados - Laboratorios -----------------------------------------------------------------# 
class IngresarResultadosLabPaciente(CreateView):
    template_name = 'pacientes/resultados_examenes/mis_resultados_examenes_form.html'
    form_class = ResultadosLabPacienteForm
    model = ResultadosLab
    def form_valid(self,form):
	self.object = form.save(commit=False)
	self.object.user = self.request.user
	self.object.save()
	return super(IngresarResultadosLabPaciente,self).form_valid(form)
    success_url = reverse_lazy('listar_resultado_lab_paciente') 
     
class ListarResultadosLabPaciente(ListView):
    template_name = 'pacientes/resultados_examenes/mis_resultados_examenes_listar_form.html'
    form_class = ResultadosLabPacienteForm
    #model = ResultadosLab
    success_url = reverse_lazy('listar_resultado_lab_paciente')
    
    def get_queryset(self):
        return ResultadosLab.objects.filter(user_id = self.request.user)
    
class ActualizarResultadosLabPaciente(UpdateView):
    template_name = 'pacientes/resultados_examenes/mis_resultados_examenes_form.html'
    form_class = ResultadosLabPacienteForm
    model = ResultadosLab
    def form_valid(self,form):
	self.object = form.save(commit=False)
	self.object.user = self.request.user
	self.object.save()
	return super(ActualizarResultadosLabPaciente,self).form_valid(form)
    success_url = reverse_lazy('listar_resultado_lab_paciente')
    
class EliminarResultadosLabPaciente(DeleteView):
    template_name = 'pacientes/resultados_examenes/mis_resultados_examenes_confirmar_delete_form.html'
    model = ResultadosLab
    success_url = reverse_lazy('listar_resultado_lab_paciente')  
        
#--------------Citas -----------------------------------------------------------------# 
class IngresarCitaPaciente(CreateView):
    template_name = 'pacientes/citas/mis_proximas_citas_form.html'
    form_class = CitaPacienteForm
    model = Cita
    def form_valid(self,form):
	self.object = form.save(commit=False)
	self.object.user = self.request.user
	self.object.save()
	return super(IngresarCitaPaciente,self).form_valid(form)
    success_url = reverse_lazy('listar_cita_paciente') 
     
class ListarCitaPaciente(ListView):
    template_name = 'pacientes/citas/mis_proximas_citas_listar_form.html'
    form_class = CitaPacienteForm
    #model = Cita
    success_url = reverse_lazy('listar_cita_paciente')
    
    def get_queryset(self):
        return Cita.objects.filter(user_id = self.request.user)
    
class ActualizarCitaPaciente(UpdateView):
    template_name = 'pacientes/citas/mis_proximas_citas_form.html'
    form_class = CitaPacienteForm
    model = Cita
    def form_valid(self,form):
	self.object = form.save(commit=False)
	self.object.user = self.request.user
	self.object.save()
	return super(ActualizarCitaPaciente,self).form_valid(form)
    success_url = reverse_lazy('listar_cita_paciente')
    
class EliminarCitaPaciente(DeleteView):
    template_name = 'pacientes/citas/mis_proximas_citas_confirmar_delete_form.html'
    model = Cita
    success_url = reverse_lazy('listar_cita_paciente')


#--------------Historia Clinica - Resumen -----------------------------------------------------------------# 
class IngresarResumenClinicoPaciente(CreateView):
    template_name = 'pacientes/historialclinico/antecedentes/personales/historial/mi_historial_resumen_form.html'
    form_class = ResumenClinicoPacienteForm
    model = ResumenClinico
    def form_valid(self,form):
	self.object = form.save(commit=False)
	self.object.user = self.request.user
	self.object.save()
	return super(IngresarResumenClinicoPaciente,self).form_valid(form)
    success_url = reverse_lazy('listar_resumenclinico_paciente') 
     
class ListarResumenClinicoPaciente(ListView):
    template_name = 'pacientes/historialclinico/antecedentes/personales/historial/mi_historial_resumen_listar_form.html'
    form_class = ResumenClinicoPacienteForm
    #model = ResumenClinico
    success_url = reverse_lazy('listar_resumenclinico_paciente')
    
    def get_queryset(self):
        return ResumenClinico.objects.filter(user_id = self.request.user)
    
class ActualizarResumenClinicoPaciente(UpdateView):
    template_name = 'pacientes/historialclinico/antecedentes/personales/historial/mi_historial_resumen_form.html'
    form_class = ResumenClinicoPacienteForm
    model =ResumenClinico
    def form_valid(self,form):
	self.object = form.save(commit=False)
	self.object.user = self.request.user
	self.object.save()
	return super(ActualizarResumenClinicoPaciente,self).form_valid(form)
    success_url = reverse_lazy('listar_resumenclinico_paciente')
    
class EliminarResumenClinicoPaciente(DeleteView):
    template_name = 'pacientes/historialclinico/antecedentes/personales/historial/mi_historial_resumen_confirmar_delete_form.html'
    model = ResumenClinico
    success_url = reverse_lazy('listar_resumenclinico_paciente')
    
    
#--------------Historia Clinica - Enfermedades -----------------------------------------------------------------# 
class IngresarEnfermedadPaciente(CreateView):
    template_name = 'pacientes/historialclinico/antecedentes/personales/enfermedades/mi_historial_enfermedades_form.html'
    form_class = EnfermedadPacienteForm
    model = Enfermedad
    def form_valid(self,form):
	self.object = form.save(commit=False)
	self.object.user = self.request.user
	self.object.save()
	return super(IngresarEnfermedadPaciente,self).form_valid(form)
    success_url = reverse_lazy('listar_enfermedad_paciente') 
     
class ListarEnfermedadPaciente(ListView):
    template_name = 'pacientes/historialclinico/antecedentes/personales/enfermedades/mi_historial_enfermedades_listar_form.html'
    form_class = EnfermedadPacienteForm
    #model = Enfermedad
    success_url = reverse_lazy('listar_enfermedad_paciente')
    
    def get_queryset(self):
        return Enfermedad.objects.filter(user_id = self.request.user)
    
class ActualizarEnfermedadPaciente(UpdateView):
    template_name = 'pacientes/historialclinico/antecedentes/personales/enfermedades/mi_historial_enfermedades_form.html'
    form_class = EnfermedadPacienteForm
    model = Enfermedad
    def form_valid(self,form):
	self.object = form.save(commit=False)
	self.object.user = self.request.user
	self.object.save()
	return super(ActualizarEnfermedadPaciente,self).form_valid(form)
    success_url = reverse_lazy('listar_enfermedad_paciente')
    
class EliminarEnfermedadPaciente(DeleteView):
    template_name = 'pacientes/historialclinico/antecedentes/personales/enfermedades/mi_historial_enfermedades_confirmar_delete_form.html'
    model = Enfermedad
    success_url = reverse_lazy('listar_enfermedad_paciente')    


#--------------Historia Clinica - Cirugias -----------------------------------------------------------------# 
class IngresarCirugiaPaciente(CreateView):
    template_name = 'pacientes/historialclinico/antecedentes/personales/cirugias/mi_historial_cirugias_form.html'
    form_class = CirugiaPacienteForm
    model = Cirugia
    def form_valid(self,form):
	self.object = form.save(commit=False)
	self.object.user = self.request.user
	self.object.save()
	return super(IngresarCirugiaPaciente,self).form_valid(form)
    success_url = reverse_lazy('listar_cirugia_paciente') 
     
class ListarCirugiaPaciente(ListView):
    template_name = 'pacientes/historialclinico/antecedentes/personales/cirugias/mi_historial_cirugias_listar_form.html'
    form_class = CirugiaPacienteForm
    #model = Cirugia
    success_url = reverse_lazy('listar_cirugia_paciente')
    
    def get_queryset(self):
        return Cirugia.objects.filter(user_id = self.request.user)
    
class ActualizarCirugiaPaciente(UpdateView):
    template_name = 'pacientes/historialclinico/antecedentes/personales/cirugias/mi_historial_cirugias_form.html'
    form_class = CirugiaPacienteForm
    model = Cirugia
    def form_valid(self,form):
	self.object = form.save(commit=False)
	self.object.user = self.request.user
	self.object.save()
	return super(ActualizarCirugiaPaciente,self).form_valid(form)
    success_url = reverse_lazy('listar_cirugia_paciente')
    
class EliminarCirugiaPaciente(DeleteView):
    template_name = 'pacientes/historialclinico/antecedentes/personales/cirugias/mi_historial_cirugias_confirmar_delete_form.html'
    model = Cirugia
    success_url = reverse_lazy('listar_cirugia_paciente')
    
    
#--------------Historia Clinica - Antecedentes Familiares -----------------------------------------------------------------# 
class IngresarFamiliarPaciente(CreateView):
    template_name = 'pacientes/historialclinico/antecedentes/familiares/mis_antecedentes_familiares_form.html'
    form_class = AntecedentesFamiliaresForm
    model = AntecedentesFamiliares
    def form_valid(self,form):
	self.object = form.save(commit=False)
	self.object.user = self.request.user
	self.object.save()
	return super(IngresarCirugiaPaciente,self).form_valid(form)
    success_url = reverse_lazy('listar_familiar_paciente') 
     
class ListarFamiliarPaciente(ListView):
    template_name = 'pacientes/historialclinico/antecedentes/familiares/mis_antecedentes_familiares_listar_form.html'
    form_class = AntecedentesFamiliaresForm
    #model = Cirugia
    success_url = reverse_lazy('listar_familiar_paciente')
    
    def get_queryset(self):
        return Cirugia.objects.filter(user_id = self.request.user)
    
class ActualizarFamiliarPaciente(UpdateView):
    template_name = 'pacientes/historialclinico/antecedentes/familiares/mis_antecedentes_familiares_form.html'
    form_class = AntecedentesFamiliaresForm
    model = AntecedentesFamiliares
    def form_valid(self,form):
	self.object = form.save(commit=False)
	self.object.user = self.request.user
	self.object.save()
	return super(ActualizarCirugiaPaciente,self).form_valid(form)
    success_url = reverse_lazy('listar_familiar_paciente')
    
class EliminarFamiliarPaciente(DeleteView):
    template_name = 'pacientes/historialclinico/antecedentes/familiares/mis_antecedentes_familiares_confirmar_delete_form.html'
    model = AntecedentesFamiliares
    success_url = reverse_lazy('listar_familiar_paciente')   


#--------------Historia Clinica - EnfermedadActual -----------------------------------------------------------------# 
class IngresarEnfermedadActualPaciente(CreateView):
    template_name = 'pacientes/historialclinico/antecedentes/familiares/mis_antecedentes_familiares_form.html'
    form_class = AntecedentesFamiliaresForm
    model = AntecedentesFamiliares
    def form_valid(self,form):
	self.object = form.save(commit=False)
	self.object.user = self.request.user
	self.object.save()
	return super(IngresarCirugiaPaciente,self).form_valid(form)
    success_url = reverse_lazy('listar_familiar_paciente') 
     
class ListarEnfermedadActualPaciente(ListView):
    template_name = 'pacientes/historialclinico/antecedentes/familiares/mis_antecedentes_familiares_listar_form.html'
    form_class = AntecedentesFamiliaresForm
    #model = Cirugia
    success_url = reverse_lazy('listar_familiar_paciente')
    
    def get_queryset(self):
        return Cirugia.objects.filter(user_id = self.request.user)
    
class ActualizarEnfermedadActualPaciente(UpdateView):
    template_name = 'pacientes/historialclinico/antecedentes/familiares/mis_antecedentes_familiares_form.html'
    form_class = AntecedentesFamiliaresForm
    model = AntecedentesFamiliares
    def form_valid(self,form):
	self.object = form.save(commit=False)
	self.object.user = self.request.user
	self.object.save()
	return super(ActualizarCirugiaPaciente,self).form_valid(form)
    success_url = reverse_lazy('listar_familiar_paciente')
    
class EliminarEnfermedadActualPaciente(DeleteView):
    template_name = 'pacientes/historialclinico/antecedentes/familiares/mis_antecedentes_familiares_confirmar_delete_form.html'
    model = AntecedentesFamiliares
    success_url = reverse_lazy('listar_familiar_paciente')
    

#--------------Historia Clinica - Toxicos -----------------------------------------------------------------# 
class IngresarToxicosPaciente(CreateView):
    template_name = 'pacientes/historialclinico/antecedentes/familiares/mis_antecedentes_familiares_form.html'
    form_class = AntecedentesFamiliaresForm
    model = AntecedentesFamiliares
    def form_valid(self,form):
	self.object = form.save(commit=False)
	self.object.user = self.request.user
	self.object.save()
	return super(IngresarCirugiaPaciente,self).form_valid(form)
    success_url = reverse_lazy('listar_familiar_paciente') 
     
class ListarToxicosPaciente(ListView):
    template_name = 'pacientes/historialclinico/antecedentes/familiares/mis_antecedentes_familiares_listar_form.html'
    form_class = AntecedentesFamiliaresForm
    #model = Cirugia
    success_url = reverse_lazy('listar_familiar_paciente')
    
    def get_queryset(self):
        return Cirugia.objects.filter(user_id = self.request.user)
    
class ActualizarToxicosPaciente(UpdateView):
    template_name = 'pacientes/historialclinico/antecedentes/familiares/mis_antecedentes_familiares_form.html'
    form_class = AntecedentesFamiliaresForm
    model = AntecedentesFamiliares
    def form_valid(self,form):
	self.object = form.save(commit=False)
	self.object.user = self.request.user
	self.object.save()
	return super(ActualizarCirugiaPaciente,self).form_valid(form)
    success_url = reverse_lazy('listar_familiar_paciente')
    
class EliminarToxicosPaciente(DeleteView):
    template_name = 'pacientes/historialclinico/antecedentes/familiares/mis_antecedentes_familiares_confirmar_delete_form.html'
    model = AntecedentesFamiliares
    success_url = reverse_lazy('listar_familiar_paciente')
    
 #--------------Historia Clinica - Alergias -----------------------------------------------------------------# 
class IngresarAlergiasPaciente(CreateView):
    template_name = 'pacientes/historialclinico/antecedentes/familiares/mis_antecedentes_familiares_form.html'
    form_class = AntecedentesFamiliaresForm
    model = AntecedentesFamiliares
    def form_valid(self,form):
	self.object = form.save(commit=False)
	self.object.user = self.request.user
	self.object.save()
	return super(IngresarCirugiaPaciente,self).form_valid(form)
    success_url = reverse_lazy('listar_familiar_paciente') 
     
class ListarAlergiasPaciente(ListView):
    template_name = 'pacientes/historialclinico/antecedentes/familiares/mis_antecedentes_familiares_listar_form.html'
    form_class = AntecedentesFamiliaresForm
    #model = Cirugia
    success_url = reverse_lazy('listar_familiar_paciente')
    
    def get_queryset(self):
        return Cirugia.objects.filter(user_id = self.request.user)
    
class ActualizarAlergiasPaciente(UpdateView):
    template_name = 'pacientes/historialclinico/antecedentes/familiares/mis_antecedentes_familiares_form.html'
    form_class = AntecedentesFamiliaresForm
    model = AntecedentesFamiliares
    def form_valid(self,form):
	self.object = form.save(commit=False)
	self.object.user = self.request.user
	self.object.save()
	return super(ActualizarCirugiaPaciente,self).form_valid(form)
    success_url = reverse_lazy('listar_familiar_paciente')
    
class EliminarAlergiasPaciente(DeleteView):
    template_name = 'pacientes/historialclinico/antecedentes/familiares/mis_antecedentes_familiares_confirmar_delete_form.html'
    model = AntecedentesFamiliares
    success_url = reverse_lazy('listar_familiar_paciente')


 #--------------Historia Clinica - Inmunizacion -----------------------------------------------------------# 
class IngresarInmunizacionPaciente(CreateView):
    template_name = 'pacientes/historialclinico/antecedentes/familiares/mis_antecedentes_familiares_form.html'
    form_class = AntecedentesFamiliaresForm
    model = AntecedentesFamiliares
    def form_valid(self,form):
	self.object = form.save(commit=False)
	self.object.user = self.request.user
	self.object.save()
	return super(IngresarCirugiaPaciente,self).form_valid(form)
    success_url = reverse_lazy('listar_familiar_paciente') 
     
class ListarInmunizacionPaciente(ListView):
    template_name = 'pacientes/historialclinico/antecedentes/familiares/mis_antecedentes_familiares_listar_form.html'
    form_class = AntecedentesFamiliaresForm
    #model = Cirugia
    success_url = reverse_lazy('listar_familiar_paciente')
    
    def get_queryset(self):
        return Cirugia.objects.filter(user_id = self.request.user)
    
class ActualizarInmunizacionPaciente(UpdateView):
    template_name = 'pacientes/historialclinico/antecedentes/familiares/mis_antecedentes_familiares_form.html'
    form_class = AntecedentesFamiliaresForm
    model = AntecedentesFamiliares
    def form_valid(self,form):
	self.object = form.save(commit=False)
	self.object.user = self.request.user
	self.object.save()
	return super(ActualizarCirugiaPaciente,self).form_valid(form)
    success_url = reverse_lazy('listar_familiar_paciente')
    
class EliminarInmunizacionPaciente(DeleteView):
    template_name = 'pacientes/historialclinico/antecedentes/familiares/mis_antecedentes_familiares_confirmar_delete_form.html'
    model = AntecedentesFamiliares
    success_url = reverse_lazy('listar_familiar_paciente')
 
 

 #--------------Historia Clinica - Medicamento -----------------------------------------------------------# 
class IngresarMedicamentoPaciente(CreateView):
    template_name = 'pacientes/historialclinico/antecedentes/familiares/mis_antecedentes_familiares_form.html'
    form_class = AntecedentesFamiliaresForm
    model = AntecedentesFamiliares
    def form_valid(self,form):
	self.object = form.save(commit=False)
	self.object.user = self.request.user
	self.object.save()
	return super(IngresarCirugiaPaciente,self).form_valid(form)
    success_url = reverse_lazy('listar_familiar_paciente') 
     
class ListarMedicamentoPaciente(ListView):
    template_name = 'pacientes/historialclinico/antecedentes/familiares/mis_antecedentes_familiares_listar_form.html'
    form_class = AntecedentesFamiliaresForm
    #model = Cirugia
    success_url = reverse_lazy('listar_familiar_paciente')
    
    def get_queryset(self):
        return Cirugia.objects.filter(user_id = self.request.user)
    
class ActualizarMedicamentoPaciente(UpdateView):
    template_name = 'pacientes/historialclinico/antecedentes/familiares/mis_antecedentes_familiares_form.html'
    form_class = AntecedentesFamiliaresForm
    model = AntecedentesFamiliares
    def form_valid(self,form):
	self.object = form.save(commit=False)
	self.object.user = self.request.user
	self.object.save()
	return super(ActualizarCirugiaPaciente,self).form_valid(form)
    success_url = reverse_lazy('listar_familiar_paciente')
    
class EliminarMedicamentoPaciente(DeleteView):
    template_name = 'pacientes/historialclinico/antecedentes/familiares/mis_antecedentes_familiares_confirmar_delete_form.html'
    model = AntecedentesFamiliares
    success_url = reverse_lazy('listar_familiar_paciente')


 #--------------Historia Clinica - Gineco Historial -----------------------------------------------------------# 
class IngresarGinecoHistorialPaciente(CreateView):
    template_name = 'pacientes/historialclinico/antecedentes/familiares/mis_antecedentes_familiares_form.html'
    form_class = AntecedentesFamiliaresForm
    model = AntecedentesFamiliares
    def form_valid(self,form):
	self.object = form.save(commit=False)
	self.object.user = self.request.user
	self.object.save()
	return super(IngresarCirugiaPaciente,self).form_valid(form)
    success_url = reverse_lazy('listar_familiar_paciente') 
     
class ListarGinecoHistorialPaciente(ListView):
    template_name = 'pacientes/historialclinico/antecedentes/familiares/mis_antecedentes_familiares_listar_form.html'
    form_class = AntecedentesFamiliaresForm
    #model = Cirugia
    success_url = reverse_lazy('listar_familiar_paciente')
    
    def get_queryset(self):
        return Cirugia.objects.filter(user_id = self.request.user)
    
class ActualizarGinecoHistorialPaciente(UpdateView):
    template_name = 'pacientes/historialclinico/antecedentes/familiares/mis_antecedentes_familiares_form.html'
    form_class = AntecedentesFamiliaresForm
    model = AntecedentesFamiliares
    def form_valid(self,form):
	self.object = form.save(commit=False)
	self.object.user = self.request.user
	self.object.save()
	return super(ActualizarCirugiaPaciente,self).form_valid(form)
    success_url = reverse_lazy('listar_familiar_paciente')
    
class EliminarGinecoHistorialPaciente(DeleteView):
    template_name = 'pacientes/historialclinico/antecedentes/familiares/mis_antecedentes_familiares_confirmar_delete_form.html'
    model = AntecedentesFamiliares
    success_url = reverse_lazy('listar_familiar_paciente')
    
  
#--------------Historia Clinica - Gineco Diario-----------------------------------------------------------# 
class IngresarGinecoDiarioPaciente(CreateView):
    template_name = 'pacientes/historialclinico/antecedentes/familiares/mis_antecedentes_familiares_form.html'
    form_class = AntecedentesFamiliaresForm
    model = AntecedentesFamiliares
    def form_valid(self,form):
	self.object = form.save(commit=False)
	self.object.user = self.request.user
	self.object.save()
	return super(IngresarCirugiaPaciente,self).form_valid(form)
    success_url = reverse_lazy('listar_familiar_paciente') 
     
class ListarGinecoDiarioPaciente(ListView):
    template_name = 'pacientes/historialclinico/antecedentes/familiares/mis_antecedentes_familiares_listar_form.html'
    form_class = AntecedentesFamiliaresForm
    #model = Cirugia
    success_url = reverse_lazy('listar_familiar_paciente')
    
    def get_queryset(self):
        return Cirugia.objects.filter(user_id = self.request.user)
    
class ActualizarGinecoDiarioPaciente(UpdateView):
    template_name = 'pacientes/historialclinico/antecedentes/familiares/mis_antecedentes_familiares_form.html'
    form_class = AntecedentesFamiliaresForm
    model = AntecedentesFamiliares
    def form_valid(self,form):
	self.object = form.save(commit=False)
	self.object.user = self.request.user
	self.object.save()
	return super(ActualizarCirugiaPaciente,self).form_valid(form)
    success_url = reverse_lazy('listar_familiar_paciente')
    
class EliminarGinecoDiarioPaciente(DeleteView):
    template_name = 'pacientes/historialclinico/antecedentes/familiares/mis_antecedentes_familiares_confirmar_delete_form.html'
    model = AntecedentesFamiliares
    success_url = reverse_lazy('listar_familiar_paciente')
    
    
 #--------------Hub Salud - Club -----------------------------------------------------------# 
class IngresarClubPaciente(CreateView):
    template_name = 'pacientes/historialclinico/antecedentes/familiares/mis_antecedentes_familiares_form.html'
    form_class = AntecedentesFamiliaresForm
    model = AntecedentesFamiliares
    def form_valid(self,form):
	self.object = form.save(commit=False)
	self.object.user = self.request.user
	self.object.save()
	return super(IngresarCirugiaPaciente,self).form_valid(form)
    success_url = reverse_lazy('listar_familiar_paciente') 
     
class ListarClubPaciente(ListView):
    template_name = 'pacientes/historialclinico/antecedentes/familiares/mis_antecedentes_familiares_listar_form.html'
    form_class = AntecedentesFamiliaresForm
    #model = Cirugia
    success_url = reverse_lazy('listar_familiar_paciente')
    
    def get_queryset(self):
        return Cirugia.objects.filter(user_id = self.request.user)
    
class ActualizarClubPaciente(UpdateView):
    template_name = 'pacientes/historialclinico/antecedentes/familiares/mis_antecedentes_familiares_form.html'
    form_class = AntecedentesFamiliaresForm
    model = AntecedentesFamiliares
    def form_valid(self,form):
	self.object = form.save(commit=False)
	self.object.user = self.request.user
	self.object.save()
	return super(ActualizarCirugiaPaciente,self).form_valid(form)
    success_url = reverse_lazy('listar_familiar_paciente')
    
class EliminarClubPaciente(DeleteView):
    template_name = 'pacientes/historialclinico/antecedentes/familiares/mis_antecedentes_familiares_confirmar_delete_form.html'
    model = AntecedentesFamiliares
    success_url = reverse_lazy('listar_familiar_paciente')

    
@login_required
def perfil_basico(request):
    if request.method == 'POST':
    	form = PerfilBasicoForm(request.POST, request.FILES, instance=request.user.perfilbasicopaciente)
    	if form.is_valid():
    		form.save()
    		return HttpResponseRedirect('/paciente/perfilbasico/principal')
    else:
    	user = request.user
    	perfiles = user.perfilbasicopaciente
    	form = PerfilBasicoForm(instance=perfiles)

    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('pacientes/perfil/perfil_basico_form.html',args, context_instance=RequestContext(request))

def perfil_basico_contactos(request):
    if request.method == 'POST':
    	form = ContactosBasicoForm(request.POST, request.FILES, instance=request.user.contactospaciente)
    	if form.is_valid():
    		form.save()
    		return HttpResponseRedirect('/paciente/perfilbasico/principal')
    else:
    	user = request.user
    	contactos = user.contactospaciente
    	form = ContactosBasicoForm(instance=contactos)

    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('pacientes/perfil/perfil_basico_contacto_form.html',args, context_instance=RequestContext(request))

def perfil_basico_social(request):
    if request.method == 'POST':
    	form = RedesSocialesForm(request.POST, instance=request.user.socialespaciente)
    	if form.is_valid():
    		form.save()
    		return HttpResponseRedirect('/paciente/perfilbasico/principal')
    else:
    	user = request.user
    	sociales = user.socialespaciente
    	form = RedesSocialesForm(instance=sociales)

    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('pacientes/perfil/perfil_basico_social_form.html',args, context_instance=RequestContext(request))

def perfil_principal_paciente_home(request):
        usuario = request.user
	data = {}
        paciente = PerfilBasico.objects.filter(user_id = usuario.id)
        contacto = ContactosBasico.objects.filter(user_id = usuario.id)
        social = RedesSociales.objects.filter(user_id = usuario.id)
        obj_contacto = get_object_or_404(contacto,user_id=usuario.id)
        tipo_pais = obj_contacto.pais
        tipo_dpto = obj_contacto.dpto
        tipo_ciudad = obj_contacto.ciudad
	data['paciente'] = paciente
	data['contacto'] = contacto
	data['social'] = social
        data['pais'] = tipo_pais
        data['dpto'] = tipo_dpto
        data['ciudad'] = tipo_ciudad

	return render_to_response('pacientes/perfil/perfil_principal.html',data,context_instance=RequestContext(request))
    
    