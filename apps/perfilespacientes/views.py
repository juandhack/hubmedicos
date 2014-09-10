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