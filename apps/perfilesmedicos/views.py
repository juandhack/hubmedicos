from django.views.generic import TemplateView,FormView
from .forms import *
from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import render, render_to_response, RequestContext
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from .models import *
from admin.forms import *
from django.contrib.auth.decorators import login_required
from django.views.generic.base import *
from django.views.generic.edit import *
from django.views.generic import *
from django.template import RequestContext

@login_required
def user_profile(request):
    if request.method == 'POST':
    	form = PerfilesForm(request.POST, request.FILES, instance=request.user.perfiles)
    	if form.is_valid():
    		form.save()
    		return HttpResponseRedirect('/home/')
    else:
    	user = request.user
    	perfiles = user.perfiles
    	form = PerfilesForm(instance=perfiles)

    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('inicio/perfil.html',args, context_instance=RequestContext(request))


def user_contactos(request):
    if request.method == 'POST':
    	form = ContactoForm(request.POST, instance=request.user.contactos)
    	if form.is_valid():
    		form.save()
    		return HttpResponseRedirect('/home/contacto')
    else:
    	user = request.user
        contactos = user.contactos
    	form = ContactoForm(instance=contactos)

    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('inicio/contacto.html',args, context_instance=RequestContext(request))


def user_academico(request):
    if request.method == 'POST':
    	form = PerfilAcademicoForm(request.POST, instance=request.user.academico)
    	if form.is_valid():
    		form.save()
    		return HttpResponseRedirect('/home/academico')
    else:
    	user = request.user
    	academico = user.academico
    	form = PerfilAcademicoForm(instance=academico)

    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('inicio/academico.html',args, context_instance=RequestContext(request))


def user_profesional(request):
    if request.method == 'POST':
    	form = PerfilProfesionalForm(request.POST, instance=request.user.profesional)
    	if form.is_valid():
    		form.save()
    		return HttpResponseRedirect('/home/profesional')
    else:
    	user = request.user
    	profesional = user.profesional
    	form = PerfilProfesionalForm(instance=profesional)

    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('inicio/profesional.html',args, context_instance=RequestContext(request))


def user_social(request):
    if request.method == 'POST':
    	form = RedesSocialesForm(request.POST, instance=request.user.sociales)
    	if form.is_valid():
    		form.save()
    		return HttpResponseRedirect('/home/social')
    else:
    	user = request.user
    	sociales = user.sociales
    	form = RedesSocialesForm(instance=sociales)

    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('inicio/social.html',args, context_instance=RequestContext(request))


def user_perfil_publico(request,userid):
	data = {}
	data['usuario'] = Perfiles.objects.filter(user_id = userid)
	data['contactos'] = Contactos.objects.filter(user_id = userid)
	data['academico'] = PerfilAcademico.objects.filter(user_id = userid)
	data['profesional'] = PerfilProfesional.objects.filter(user_id = userid)
	data['social'] = RedesSociales.objects.filter(user_id = userid)
	data['consultas'] = PreguntasRespuestas.objects.filter(user_id = userid)
	data['servicios'] = Servicios.objects.filter(user_id = userid)
	return render_to_response('perfil/index.html',data,context_instance=RequestContext(request))
    
    

	
    
class IngresarPregunta(CreateView):
    template_name = 'inicio/preguntasrespuestas_form.html'
    form_class = ConsultasForm
    model = PreguntasRespuestas
    def form_valid(self,form):
	self.object = form.save(commit=False)
	self.object.user = self.request.user
	self.object.save()
	return super(IngresarPregunta,self).form_valid(form)
    success_url = reverse_lazy('listar_preguntas')   
	
class VisualizarPregunta(DetailView):
    template_name = 'inicio/listarpr_form.html'
    model = PreguntasRespuestas
    
class EliminarPregunta(DeleteView):
    template_name = 'inicio/preguntasrespuestas_confirm_delete.html'
    model = PreguntasRespuestas
    success_url = reverse_lazy('listar_preguntas')
  
    
class ActualizarPregunta(UpdateView):
    template_name = 'inicio/preguntasrespuestas_form.html'
    form_class = ConsultasForm
    model = PreguntasRespuestas
    def form_valid(self,form):
	self.object = form.save(commit=False)
	self.object.user = self.request.user
	self.object.save()
	return super(ActualizarPregunta,self).form_valid(form)
    success_url = reverse_lazy('listar_preguntas')  
    
class ListarPreguntas(ListView):
    template_name = 'inicio/listarpr_form.html'
    form_class = ConsultasForm
    model = PreguntasRespuestas
    success_url = reverse_lazy('listar_preguntas')
    
    def get_queryset(self):
        return PreguntasRespuestas.objects.filter(user_id = self.request.user)
   

class PacientesHome(TemplateView):
	template_name = 'pacientes/medicos_pacientes_fichas.html'
	
    
class IngresarInfoProfesional(CreateView):
    template_name = 'perfil/profesional_form.html'
    form_class = PerfilProfesionalForm
    model = PerfilProfesional
    def form_valid(self,form):
	self.object = form.save(commit=False)
	self.object.user = self.request.user
	self.object.save()
	return super(IngresarInfoProfesional,self).form_valid(form)
    success_url = reverse_lazy('listar_info_profesional')
    
class VisualizarInfoProfesional(DetailView):
    template_name = 'perfil/listarexperienciaprofesional_form.html'
    model = PerfilProfesional
    
class EliminarInfoProfesional(DeleteView):
    template_name = 'perfil/profesional_confirmar_delete_form.html'
    model = PerfilProfesional
    success_url = reverse_lazy('listar_info_profesional')
  
    
class ActualizarInfoProfesional(UpdateView):
    template_name = 'perfil/profesional_form.html'
    form_class = PerfilProfesionalForm
    model = PerfilProfesional
    def form_valid(self,form):
	self.object = form.save(commit=False)
	self.object.user = self.request.user
	self.object.save()
	return super(ActualizarInfoProfesional,self).form_valid(form)
    success_url = reverse_lazy('listar_info_profesional')  
    
class ListarInfoProfesional(ListView):
    template_name = 'perfil/listarexperienciaprofesional_form.html'
    form_class = PerfilProfesionalForm
    model = PerfilProfesional
    success_url = reverse_lazy('listar_info_profesional')
    
    def get_queryset(self):
        return PerfilProfesional.objects.filter(user_id = self.request.user)
    
class IngresarInfoAcademica(CreateView):
    template_name = 'perfil/academico_form.html'
    form_class = PerfilAcademicoForm
    model = PerfilAcademico
    def form_valid(self,form):
	self.object = form.save(commit=False)
	self.object.user = self.request.user
	self.object.save()
	return super(IngresarInfoAcademica,self).form_valid(form)
    success_url = reverse_lazy('listar_info_academica')
    
class VisualizarInfoAcademica(DetailView):
    template_name = 'perfil/listarinfoacademica_form.html'
    model = PerfilAcademico
    
class EliminarInfoAcademica(DeleteView):
    template_name = 'perfil/academico_confirmar_delete_form.html'
    model = PerfilAcademico
    success_url = reverse_lazy('listar_info_academica')
  
    
class ActualizarInfoAcademica(UpdateView):
    template_name = 'perfil/academico_form.html'
    form_class = PerfilAcademicoForm
    model = PerfilAcademico
    def form_valid(self,form):
	self.object = form.save(commit=False)
	self.object.user = self.request.user
	self.object.save()
	return super(ActualizarInfoAcademica,self).form_valid(form)
    success_url = reverse_lazy('listar_info_academica')  
    
class ListarInfoAcademica(ListView):
    template_name = 'perfil/listarinfoacademica_form.html'
    form_class = PerfilAcademicoForm
    model = PerfilAcademico
    success_url = reverse_lazy('listar_info_academica')
    
    def get_queryset(self):
        return PerfilAcademico.objects.filter(user_id = self.request.user)

    
class IngresarInfoServicios(CreateView):
    template_name = 'servicios/servicios_form.html'
    form_class = ServiciosForm
    model = Servicios
    def form_valid(self,form):
	self.object = form.save(commit=False)
	self.object.user = self.request.user
	self.object.save()
	return super(IngresarInfoServicios,self).form_valid(form)
    success_url = reverse_lazy('listar_info_servicios')
    
class VisualizarInfoServicios(DetailView):
    template_name = 'servicios/listarinfoservicios_form.html'
    model = Servicios
    
class EliminarInfoServicios(DeleteView):
    template_name = 'servicios/servicios_confirmar_delete_form.html'
    model = Servicios
    success_url = reverse_lazy('listar_info_servicios')
  
    
class ActualizarInfoServicios(UpdateView):
    template_name = 'servicios/servicios_form.html'
    form_class = ServiciosForm
    model = Servicios
    def form_valid(self,form):
	self.object = form.save(commit=False)
	self.object.user = self.request.user
	self.object.save()
	return super(ActualizarInfoServicios,self).form_valid(form)
    success_url = reverse_lazy('listar_info_servicios')  
    
class ListarInfoServicios(ListView):
    template_name = 'servicios/listarinfoservicios_form.html'
    form_class = ServiciosForm
    model = Servicios
    success_url = reverse_lazy('listar_info_servicios')
    
    def get_queryset(self):
        return Servicios.objects.filter(user_id = self.request.user)
    
    
class IngresarEntradaBlog(CreateView):
    template_name = 'blog/entradas_blog_form.html'
    form_class = EntryAdminForm
    ##model = PerfilProfesional
    def form_valid(self,form):
	self.object = form.save(commit=False)
	self.object.user = self.request.user
	self.object.save()
	return super(IngresarEntradaBlog,self).form_valid(form)
    success_url = reverse_lazy('ingresar_entrada_blog')



