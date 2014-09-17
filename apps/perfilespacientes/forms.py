import os, sys
# -*- encoding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm,PasswordChangeForm
from .models import *
from apps.perfilesmedicos.models import RedesSociales
from django.forms import Textarea,TextInput, URLInput, CharField
from django.forms.extras import SelectDateWidget

class PerfilBasicoForm(forms.ModelForm):
    class Meta:
        model = PerfilBasico
        fields = ('dni','nombres','apellidos','acerca_de','sexo','fecha_nacimiento','grupo_sanguineo','imagen')
        labels = {
            'dni': _('Documento de Identidad'),
            'fecha_nacimiento': _('Fecha de Nacimiento'),
            'grupo_sanguineo': _('Grupo de Sangre'),
        }
        
        widgets = {
            'acerca_de': Textarea(attrs={'cols': 35, 'rows': 10, 'placeholder': _("Escribe un breve resumen de tu perfil")}),
            'fecha_nacimiento': SelectDateWidget(years=range(1930, 2015)),
            'dni': TextInput(attrs={'placeholder': _("Ej: 71794069")})
        }
       
        
        
        

class ContactosBasicoForm(forms.ModelForm):
    class Meta:
        model = ContactosBasico
        fields = ('pais','dpto','ciudad','telefono','celular','correo')
        
        widgets = {
            'telefono': TextInput(attrs={'placeholder': _("Ej: 5415854")}),
            'celular': TextInput(attrs={'placeholder': _("Ej: 3014527885")}),
            'correo': TextInput(attrs={'placeholder': _("Ej: micorreo@midominio.com")}),
        }
        
    
class RedesSocialesForm(forms.ModelForm):
    class Meta:
        model = RedesSociales
        fields = ('blog','twitter','facebook','linkedin','you_tube')
        

class SintomasGeneralesPacienteForm(forms.ModelForm):
    class Meta:
        model = SintomasGeneralesPaciente
        exclude = ('user',)
        #code
    
    #code

        
             
      
        