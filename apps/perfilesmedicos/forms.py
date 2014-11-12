import os, sys
# -*- encoding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm,PasswordChangeForm
from apps.perfilesmedicos.models import *
from django.forms import Textarea, TextInput, FileInput, DateInput

class PerfilesForm(forms.ModelForm):
    class Meta:
        model = Perfiles
        fields = ('dni','nombres','apellidos','acerca_de','imagen')
        labels = {
            'dni': _('Documento de Identidad'),
        }
        
        widgets = {
            
            'dni':TextInput(attrs={'maxlength': 50, 'class': 'form-control','style':'width:30%'}),
            'nombres':TextInput(attrs={'maxlength': 50, 'class': 'form-control','style':'width:50%'}),
            'apellidos':TextInput(attrs={'maxlength': 50, 'class': 'form-control','style':'width:50%'}),
            'acerca_de': Textarea(attrs={'cols': 50, 'rows': 6,'class': 'form-control','style':'width:90%'}),
            'imagen': FileInput(attrs={'maxlength': 50, 'class': 'form-control','style':'width:50%'}),
            'acerca_de':Textarea(attrs={'cols': 30, 'rows': 10,'class': 'form-control','placeholder': _("Escribe algo sobre ti "),'style':'width:90%'}),
        }
      
class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contactos
        fields = ('pais','dpto','ciudad','telefono','celular','correo')
        
       
class PerfilAcademicoForm(forms.ModelForm):
    class Meta:
        model = PerfilAcademico
        fields = ('institucion','titulo','logros','anioinicio','aniofin')
        
        widgets = {
            'institucion':TextInput(attrs={'maxlength': 50, 'class': 'form-control','style':'width:60%'}),
            'titulo':TextInput(attrs={'maxlength': 50, 'class': 'form-control','style':'width:60%'}),
            'logros':Textarea(attrs={'cols': 50, 'rows': 6,'class': 'form-control','style':'width:90%'}), 
            'anioinicio':  DateInput(format='%d/%m/%Y',attrs={'class': 'form-control', 'id':'datePicker','style':'width:140px'}),
            'aniofin':  DateInput(format='%d/%m/%Y',attrs={'class': 'form-control', 'id':'datePicker2','style':'width:140px'}),
            
        }
       

class PerfilProfesionalForm(forms.ModelForm):
    class Meta:
        model = PerfilProfesional
        fields = ('organizacion','especialidad','cargo','funcionesrealizadas','anioinicio','aniofin')
        
        
        widgets = {
            'organizacion':TextInput(attrs={'maxlength': 50, 'class': 'form-control','style':'width:60%'}),
            'especialidad': forms.Select(attrs={'style':'width:30%'}),
            'cargo':TextInput(attrs={'maxlength': 50, 'class': 'form-control','style':'width:40%'}), 
            'funcionesrealizadas':  Textarea(attrs={'cols': 50, 'rows': 6,'class': 'form-control','style':'width:90%'}),
            'anioinicio':  DateInput(format='%d/%m/%Y',attrs={'class': 'form-control', 'id':'datePicker','style':'width:30%'}),
            'aniofin':  DateInput(format='%d/%m/%Y',attrs={'class': 'form-control', 'id':'datePicker2','style':'width:30%'}),
            
        }
       

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
        

class ServiciosForm(forms.ModelForm):
    class Meta:
        model = Servicios
        fields = ('organizacion','especialidad','descripcion','direccion','pais','dpto','telefono','celular','correo','blog')
        
        
class PreguntasRespuestasForm(forms.ModelForm):
    class Meta:
        model = PreguntasRespuestas
        exclude = ('user',)
        
        widgets = {
            
            'pregunta' : Textarea(attrs={'cols': 50, 'rows': 6,'class': 'form-control','style':'width:90%'}),
            'respuesta': Textarea(attrs={'cols': 50, 'rows': 6,'class': 'form-control','style':'width:90%'}),
            'categoria': forms.Select(attrs={'style':'width:30%'}),
        }
        
class CategoriaPyRForm(forms.ModelForm):
    class Meta:
        model = CategoriaPR
        exclude = ('user',)
        
        widgets = {
            
            'categoria': TextInput(attrs={'maxlength': 50, 'class': 'form-control','style':'width:60%'}),
        }
        

class ClubMedicoSubscripcionForm(forms.ModelForm):
    class Meta:
        model = ClubMedicoSubscripcion
        exclude = ('user',)
        widgets = {
            
            'club': forms.Select(attrs={'style':'width:30%'}),
            'rol': forms.Select(attrs={'style':'width:30%'}),
            
        }
        

       


        
        