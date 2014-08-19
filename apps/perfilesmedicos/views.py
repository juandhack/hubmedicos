from django.views.generic import TemplateView,FormView
from .forms import *
from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import render, render_to_response, RequestContext
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from .models import *
from django.contrib.auth.decorators import login_required

@login_required
def user_profile(request):
    if request.method == 'POST':
    	form = PerfilesForm(request.POST, instance=request.user.perfiles)
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
	return render_to_response('admin/index.html',data,context_instance=RequestContext(request))

class pacienteshome(TemplateView):
	template_name = 'pacientes/index.html'

class pacienteshome(TemplateView):
	template_name = 'registro/pr.html'
