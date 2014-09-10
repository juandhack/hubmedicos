import os, sys
# -*- encoding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm,PasswordChangeForm
from apps.perfilespacientes.models import *
from apps.perfilesmedicos.models import *
from django.forms import Textarea

class PerfilBasicoForm(forms.ModelForm):
    class Meta:
        model = PerfilBasico
        fields = ('dni','nombres','apellidos','acerca_de','sexo','imagen')
        labels = {
            'dni': _('Documento de Identidad'),
        }
        help_texts = {
            'dni': _('Ej: 71985445'),
            'acerca_de': _('Acerca de ti'),
        }
        widgets = {
            'acerca_de': Textarea(attrs={'cols': 80, 'rows': 20}),
        }
      
        
        
        

class ContactosBasicoForm(forms.ModelForm):
    class Meta:
        model = ContactosBasico
        fields = ('pais','dpto','ciudad','telefono','celular','correo')
        
        help_texts = {
            'telefono': _('Ej: 2523240'),
            'correo': _('Ej: juan.perez@tucorreo.com'),
        }


class RedesSocialesForm(forms.ModelForm):
    class Meta:
        model = RedesSociales
        fields = ('blog','twitter','facebook','linkedin','you_tube')
        help_texts = {
            'blog': _('Ej: miblog.com'),
            'twitter': _('Ej: @MiCuenta'),
            'facebook' : ('Ej: facebook.com/micuenta '),
            'linkedin' : ('Ej: linkedin.com/micuenta '),
            'you_tube' : ('Ej: youtube.com/micuenta '),
        }       
        