import os, sys
# -*- encoding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm,PasswordChangeForm
from apps.perfilesmedicos.models import *

class PerfilesForm(forms.ModelForm):
    class Meta:
        model = Perfiles
        fields = ('dni','nombres','apellidos','acerca_de','imagen')
        labels = {
            'dni': _('Documento de Identidad'),
        }
        help_texts = {
            'dni': _('Ej: 71985445'),
            'acerca_de': _('Ingresa un resumen de tu perfil'),
        }
      
        
        
        

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contactos
        fields = ('pais','dpto','ciudad','telefono','celular','correo')
        
        help_texts = {
            'telefono': _('Ej: 2523240'),
            'correo': _('Ej: juan.perez@tucorreo.com'),
        }

class PerfilAcademicoForm(forms.ModelForm):
    class Meta:
        model = PerfilAcademico
        fields = ('institucion','titulo','logros')
        help_texts = {
            'institucion': _('Ej: Universidad del Norte'),
            'titulo': _('Ej: Medico cirujano'),
            'logros': _('Ej: Becado con honores'),
          
        }

class PerfilProfesionalForm(forms.ModelForm):
    class Meta:
        model = PerfilProfesional
        fields = ('organizacion','especialidad','cargo','aniosejercidos','funcionesrealizadas')
        help_texts = {
            'organizacion': _('Ej: Hospital San Juan de Dios'),
            'cargo': _('Ej: Director'),
            'especialidad': _('Ej: Medicina del Trabajo'),
           
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
        
class ConsultasForm(forms.ModelForm):
    class Meta:
        model = PreguntasRespuestas
        fields = ('pregunta','respuesta')



        
        