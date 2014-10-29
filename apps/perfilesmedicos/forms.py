import os, sys
# -*- encoding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm,PasswordChangeForm
from apps.perfilesmedicos.models import *
from django.forms import Textarea, TextInput, FileInput

class PerfilesForm(forms.ModelForm):
    class Meta:
        model = Perfiles
        fields = ('dni','nombres','apellidos','acerca_de','imagen')
        labels = {
            'dni': _('Documento de Identidad'),
        }
        
        widgets = {
            
            'dni':TextInput(attrs={'maxlength': 50, 'class': 'form-control','style':'width:300px'}),
            'nombres':TextInput(attrs={'maxlength': 50, 'class': 'form-control','style':'width:300px'}),
            'apellidos':TextInput(attrs={'maxlength': 50, 'class': 'form-control','style':'width:300px'}),
            'acerca_de': Textarea(attrs={'cols': 80, 'rows': 20}),
            'imagen': FileInput(attrs={'maxlength': 50, 'class': 'form-control','style':'width:250px'}),
            'acerca_de':Textarea(attrs={'cols': 30, 'rows': 10,'class': 'form-control','placeholder': _("Escribe algo sobre ti "),'style':'width:300px'}),
        }
      
class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contactos
        fields = ('pais','dpto','ciudad','telefono','celular','correo')
        
       
class PerfilAcademicoForm(forms.ModelForm):
    class Meta:
        model = PerfilAcademico
        fields = ('institucion','titulo','logros','anioinicio','aniofin')
       

class PerfilProfesionalForm(forms.ModelForm):
    class Meta:
        model = PerfilProfesional
        fields = ('organizacion','especialidad','cargo','funcionesrealizadas','anioinicio','aniofin')
       

class RedesSocialesForm(forms.ModelForm):
    class Meta:
        model = RedesSociales
        fields = ('blog','twitter','facebook','linkedin','you_tube')
        widgets = {
            'blog' : TextInput(attrs={'size':30,'placeholder': _("ej: miblog.com")}),
            'twitter' : TextInput(attrs={'size':30,'placeholder': _("ej: twitter.com/miusuario")}),
            'facebook' : TextInput(attrs={'size':30,'placeholder': _("ej: facebook.com/miusuario")}),
            'linkedin' : TextInput(attrs={'size':30,'placeholder': _("ej: linkedin.com/miusuario")}),
            'you_tube' : TextInput(attrs={'size':30,'placeholder': _("ej: youtube.com/miusuario")}),
            
        }       
        
class ConsultasForm(forms.ModelForm):
    class Meta:
        model = PreguntasRespuestas
        exclude = ('user',)

class ServiciosForm(forms.ModelForm):
    class Meta:
        model = Servicios
        fields = ('organizacion','especialidad','descripcion','direccion','pais','dpto','telefono','celular','correo','blog')
       


        
        