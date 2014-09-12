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
        
        
@login_required
def perfil_basico(request):
    if request.method == 'POST':
    	form = PerfilBasicoForm(request.POST, request.FILES, instance=request.user.perfiles)
    	if form.is_valid():
    		form.save()
    		return HttpResponseRedirect('/paciente/perfilbasico')
    else:
    	user = request.user
    	perfiles = user.perfiles
    	form = PerfilBasicoForm(instance=perfiles)

    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('pacientes/perfil_basico_form.html',args, context_instance=RequestContext(request))

def perfil_basico_contactos(request):
    if request.method == 'POST':
    	form = ContactosBasicoForm(request.POST, request.FILES, instance=request.user.contactos)
    	if form.is_valid():
    		form.save()
    		return HttpResponseRedirect('/paciente/perfilbasico/contacto')
    else:
    	user = request.user
    	contactos = user.contactos
    	form = ContactosBasicoForm(instance=contactos)

    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('pacientes/perfil_basico_contacto_form.html',args, context_instance=RequestContext(request))