from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.views.generic import TemplateView,FormView
from django.views.generic.base import View
from django.views.generic.edit import FormView
from .forms import RegistrationForm,LoginForm
from django.core.urlresolvers import reverse_lazy

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from . import config




class index(TemplateView):
	template_name = 'inicio/index.html'

class board(TemplateView):
    template_name = 'inicio/perfil.html'

class pacientes(TemplateView):
	template_name = 'pacientes/perfil_basico_form.html'

class base(TemplateView):
	template_name = 'base.html'

class LoginView(FormView):
    template_name = 'registro/login.html'
    form_class = LoginForm

    @method_decorator(csrf_protect)
    def dispatch(self, *args, **kwargs):
        return super(LoginView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(LoginView, self).form_valid(form)

    def get_success_url(self):
        try:
            return config.LOGIN_REDIRECT_URL_MEDICOS
        except:
            return "/accounts/profile/"
	
class LoginViewPaciente(FormView):
    template_name = 'registro/loginPaciente.html'
    form_class = LoginForm

    @method_decorator(csrf_protect)
    def dispatch(self, *args, **kwargs):
        return super(LoginViewPaciente, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(LoginViewPaciente, self).form_valid(form)

    def get_success_url(self):
        try:
            return config.LOGIN_REDIRECT_URL_PACIENTES
        except:
            return "/accounts/profile/"

class LogoutView(View):

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LogoutView, self).dispatch(*args, **kwargs)

    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/")


class RegisterView(FormView):
    template_name = 'registro/register.html'
    form_class = RegistrationForm

    @method_decorator(csrf_protect)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseRedirect("confirmacion")
        else:
            return super(RegisterView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):

        user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email']
        )

        return super(RegisterView, self).form_valid(form)

    def get_success_url(self):
        return reverse('register-success')

class RegisterViewPaciente(FormView):
    template_name = 'registro/registerPaciente.html'
    form_class = RegistrationForm

    @method_decorator(csrf_protect)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseRedirect("confirmacion")
        else:
            return super(RegisterViewPaciente, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):

        user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email']
        )

        return super(RegisterViewPaciente, self).form_valid(form)

    def get_success_url(self):
        return reverse('register-success_paciente')

class RegisterSuccessView(TemplateView):
    template_name = 'registro/success.html'
    
class RegisterSuccessViewPaciente(TemplateView):
    template_name = 'registro/success_paciente.html'
