
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm,PasswordChangeForm
from apps.perfilesmedicos.models import *

class PerfilesForm(forms.ModelForm):
    class Meta:
        model = Perfiles
        fields = ('dni','nombres','apellidos','acerca_de')

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contactos
        fields = ('dpto','ciudad','telefono','celular','correo')

class PerfilAcademicoForm(forms.ModelForm):
    class Meta:
        model = PerfilAcademico
        fields = ('institucion','titulo','logros')

class PerfilProfesionalForm(forms.ModelForm):
    class Meta:
        model = PerfilProfesional
        fields = ('organizacion','especialidad','cargo','aniosejercidos','numregistroprof','funcionesrealizadas')

class RedesSocialesForm(forms.ModelForm):
    class Meta:
        model = RedesSociales
        fields = ('blog','twitter','facebook','linkedin','you_tube')


        
        