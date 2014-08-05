from django.views.generic import TemplateView,FormView
from .forms import UserForm
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from .models import Perfiles


class Perfil(FormView):
	template_name = 'inicio/perfil.html'
	form_class = UserForm
	success_url = reverse_lazy('perfil')

	def form_valid(self, form):
		user = form.save()

		return super(Perfil , self).form_valid(form)


class Tarjeta(TemplateView):
	template_name = 'admin/index.html'