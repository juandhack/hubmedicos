from django.views.generic import TemplateView,FormView
from .forms import *
from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import render, render_to_response, RequestContext
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from .models import *
from django.contrib.auth.decorators import login_required
from django.views.generic.base import *
from django.views.generic.edit import *
from django.views.generic import *
from django.template import RequestContext

# Create your views here.
class PacientesPerfilBasico(TemplateView):
	template_name = 'pacientes/perfil_basico_form.html'
        
class SintomasActualesPaciente(TemplateView):
    template_name = 'pacientes/mis_sintomas_form.html'
    
class EstadoAnimoPaciente(TemplateView):
    template_name = 'pacientes/mis_estado_de_animo_form.html'
    
class MedicionesPaciente(TemplateView):
    template_name = 'pacientes/medicionesclinicas/mis_mediciones_clinicas_form.html'
    
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
    model = SintomasGeneralesPaciente
    success_url = reverse_lazy('listar_sintomas_paciente')
    
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
    model = EstadosAnimoPaciente
    success_url = reverse_lazy('listar_estado_animo_paciente')
    
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
        
@login_required
def perfil_basico(request):
    if request.method == 'POST':
    	form = PerfilBasicoForm(request.POST, request.FILES, instance=request.user.perfilbasicopaciente)
    	if form.is_valid():
    		form.save()
    		return HttpResponseRedirect('/paciente/perfilbasico')
    else:
    	user = request.user
    	perfiles = user.perfilbasicopaciente
    	form = PerfilBasicoForm(instance=perfiles)

    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('pacientes/perfil_basico_form.html',args, context_instance=RequestContext(request))

def perfil_basico_contactos(request):
    if request.method == 'POST':
    	form = ContactosBasicoForm(request.POST, request.FILES, instance=request.user.contactospaciente)
    	if form.is_valid():
    		form.save()
    		return HttpResponseRedirect('/paciente/perfilbasico/contacto')
    else:
    	user = request.user
    	contactos = user.contactospaciente
    	form = ContactosBasicoForm(instance=contactos)

    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('pacientes/perfil_basico_contacto_form.html',args, context_instance=RequestContext(request))

def perfil_basico_social(request):
    if request.method == 'POST':
    	form = RedesSocialesForm(request.POST, instance=request.user.socialespaciente)
    	if form.is_valid():
    		form.save()
    		return HttpResponseRedirect('/paciente/perfilbasico/social')
    else:
    	user = request.user
    	sociales = user.socialespaciente
    	form = RedesSocialesForm(instance=sociales)

    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('pacientes/perfil_basico_social_form.html',args, context_instance=RequestContext(request))