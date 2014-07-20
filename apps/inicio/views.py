from django.views.generic import TemplateView,FormView
from .forms import UserForm
from django.core.urlresolvers import reverse_lazy
from .models import Perfiles
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404

class Registrarse(FormView):
	template_name = 'inicio/registrarse.html'
	form_class = UserForm
	success_url = reverse_lazy('registrarse')

	def form_valid(self, form):
		user = form.save()
		perfil = Perfiles()
		perfil.usuario = user
		perfil.telefono = form.cleaned_data['telefono']
		perfil.save()
		return super(Registrarse , self).form_valid(form)

class base(TemplateView):
	template_name = 'inicio/board.html'

class index(TemplateView):
	template_name = 'inicio/index.html'

class blank_page(TemplateView):
	template_name = 'inicio/blank-page.html'

class board(TemplateView):
	template_name = 'inicio/board.html'

class bootstrap_elements(TemplateView):
	template_name = 'inicio/bootstrap-elements.html'

class bootstrap_grid(TemplateView):
	template_name = 'inicio/bootstrap-grid.html'

class charts(TemplateView):
	template_name = 'inicio/charts.html'

class formularios(TemplateView):
	template_name = 'inicio/forms.html'

class tables(TemplateView):
	template_name = 'inicio/tables.html'

class tipografia(TemplateView):
	template_name = 'inicio/typography.html'
