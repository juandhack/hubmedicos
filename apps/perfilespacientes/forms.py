import os, sys
# -*- encoding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm,PasswordChangeForm
from .models import *
from apps.perfilesmedicos.models import RedesSociales
from django.forms import Textarea,TextInput, URLInput, CharField, DateTimeInput, NumberInput
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
            'acerca_de': Textarea(attrs={'cols': 40, 'rows': 10, 'placeholder': _("Escribe un breve resumen de tu perfil")}),
            'fecha_nacimiento': SelectDateWidget(years=range(1930, 2015)),
            'dni': TextInput(attrs={'size':30,'placeholder': _("ej: 71794069")}),
            'nombres': TextInput(attrs={'size':40}),
            'apellidos': TextInput(attrs={'size':40})
        }
       
class ContactosBasicoForm(forms.ModelForm):
    class Meta:
        model = ContactosBasico
        fields = ('pais','dpto','ciudad','telefono','celular','correo')
        
        widgets = {
            'telefono': TextInput(attrs={'placeholder': _("ej: 5415854")}),
            'celular': TextInput(attrs={'placeholder': _("ej: 3014527885")}),
            'correo': TextInput(attrs={'placeholder': _("ej: micorreo@midominio.com")}),
        }
        
class RedesSocialesForm(forms.ModelForm):
    class Meta:
        model = RedesSociales
        fields = ('blog','twitter','facebook','linkedin','you_tube')
        

class SintomasGeneralesPacienteForm(forms.ModelForm):
    class Meta:
        model = SintomasGeneralesPaciente
        exclude = ('user',)
        
class SintomaAlteracionGlicemicaPacienteForm(forms.ModelForm):
    class Meta:
        model = SintomasAlteracionGlicemicaPaciente
        exclude = ('user',)
        
class EstadoAnimoPacienteForm(forms.ModelForm):
    class Meta:
        model = EstadosAnimoPaciente
        exclude = ('user',)
        
        #code
    
    #code

class PesoPacienteForm(forms.ModelForm):
    class Meta:
        model = Peso
        fields = ('peso','fecha','nota','hora')
                
        widgets = {
            'peso': TextInput(attrs={'size':15,'placeholder': _("Kg")}),
            'fecha': SelectDateWidget(years=range(1930, 2015)),
            'hora': TextInput(attrs={'size':15,'placeholder': _("ej: 11:40")}),
            'nota': Textarea(attrs={'cols': 50, 'rows': 5}),
            
        }
        

class TallaPacienteForm(forms.ModelForm):
    class Meta:
        model = Talla
        fields = ('altura','fecha','nota','hora')
                
        widgets = {
            'altura': TextInput(attrs={'size':10,'placeholder': _("Cm")}),
            'fecha': SelectDateWidget(years=range(1930, 2015)),
            'hora': TextInput(attrs={'size':15,'placeholder': _("ej: 11:40")}),
            'nota': Textarea(attrs={'cols': 50, 'rows': 5}),
            
        }
        
   
class GlucosaPacienteForm(forms.ModelForm):
    class Meta:
        model = Glucemia
        fields = ('medicion','contexto_medicion','tipo','fecha','hora','nota')
                
        widgets = {
            'medicion': TextInput(attrs={'size':15,'placeholder': _("mg/dL")}),
            'fecha': SelectDateWidget(years=range(1930, 2015)),
            'hora': TextInput(attrs={'size':15,'placeholder': _("ej: 11:40")}),
            'nota': Textarea(attrs={'cols': 50, 'rows': 5}),
            
        }
        
class HemoglobinaPacienteForm(forms.ModelForm):
    class Meta:
        model = Hemoglobina
        fields = ('porcentaje',)
                
        widgets = {
            'porcentaje': NumberInput(attrs={'size':15,'placeholder': _("%")}),
        }
   
        
class ColesterolPacienteForm(forms.ModelForm):
    class Meta:
        model = Colesterol
        fields = ('ldl','hdl','trigliceridos','colesterol_total','fecha','hora','nota')
                
        widgets = {
            'ldl': NumberInput(attrs={'size':15,'placeholder': _("mg/dL")}),
            'hdl': NumberInput(attrs={'size':15,'placeholder': _("mg/dL")}),
            'trigliceridos': NumberInput(attrs={'size':15,'placeholder': _("mg/dL")}),
            'colesterol_total': NumberInput(attrs={'size':15,'placeholder': _("mg/dL")}),
            'fecha': SelectDateWidget(years=range(1930, 2015)),
            'hora': TextInput(attrs={'size':15,'placeholder': _("ej: 11:40")}),
            'nota': Textarea(attrs={'cols': 50, 'rows': 5}),
            
        }
        
        
class PresionPacienteForm(forms.ModelForm):
    class Meta:
        model = Presion
        fields = ('sistolica','diastolica','pulso','latido_irregular','fecha','nota','hora')
                
        widgets = {
            'sistolica': NumberInput(attrs={'size':5,'placeholder': _("mmHg")}),
            'diastolica': NumberInput(attrs={'size':10,'placeholder': _("mmHg")}),
            'pulso': NumberInput(attrs={'size':10,'placeholder': _("mmHg")}),
      
            'fecha': SelectDateWidget(years=range(1930, 2015)),
            'hora': TextInput(attrs={'size':10,'placeholder': _("ej: 11:40")}),
            'nota': Textarea(attrs={'cols': 30, 'rows': 5}),
            
        }
        
class RutinaEjercicioPacienteForm(forms.ModelForm):
    class Meta:
        model = RutinaEjercicio
        fields = ('nombre','descripcion','duracion','distancia','num_pasos','calorias_quemadas','nota','fecha','hora')
                
        widgets = {
            'nombre': TextInput(attrs={'size':20,'placeholder': _("ej: ciclismo")}),
            'descripcion': TextInput(attrs={'size':16}),
            'diastolica': TextInput(attrs={'size':10,'placeholder': _("ej: entrenamiento para partida de tenis")}),
            'duracion': NumberInput(attrs={'size':10,'placeholder': _("minutos")}),
            'distancia': NumberInput(attrs={'size':10,'placeholder': _("km")}),
            'num_pasos': NumberInput(attrs={'size':5}),
            'calorias_quemadas': NumberInput(attrs={'size':5    }),
            'fecha': SelectDateWidget(years=range(1930, 2015)),
            'hora': TextInput(attrs={'size':20,'placeholder': _("Ej: 13:40")}),
            'nota': Textarea(attrs={'cols': 30, 'rows': 5}),
            
        }
        
class RutinaAlimentacionPacienteForm(forms.ModelForm):
    class Meta:
        model = RutinaAlimentacion
        fields = ('nombre','tipo_comida','tamanio_porcion','cantidad_porcion','calorias','fecha','hora','nota')
                
        widgets = {
            'nombre': TextInput(attrs={'size':15,'placeholder': _("ej: ciclismo")}),
            'tamanio_porcion': NumberInput(attrs={'size':15}),
            'cantidad_porcion': NumberInput(attrs={'size':15,'placeholder': _("ej: 2")}),
            'calorias': NumberInput(attrs={'size':15}),
            'fecha': SelectDateWidget(years=range(1930, 2015)),
            'hora': TextInput(attrs={'size':15,'placeholder': _("Ej: 13:40")}),
            'nota': Textarea(attrs={'cols': 50, 'rows': 5}),
            
        }
        
class MedicamentoPacienteForm(forms.ModelForm):
    class Meta:
        model = Medicamento
        fields = ('nombre','concentracion','tipo_concentracion','dosis','tipo_dosis','modo_admin','frecuencia_admin','motivo_admin','fecha_inicio','fecha_final','nota')
                
        widgets = {
            'nombre': TextInput(attrs={'size':40,'placeholder': _("ej: albuterol")}),
            'concentracion': NumberInput(attrs={'size':50,'placeholder': _("ej: 500")}),
            'dosis': NumberInput(attrs={'size':15,'placeholder': _("ej: 2")}),
            'frecuencia_admin': TextInput(attrs={'size':15,'placeholder': _("ej: 2 veces al dia")}),
            'motivo_admin': TextInput(attrs={'size':15}),
            'fecha_inicio': SelectDateWidget(years=range(1930, 2015)),
            'fecha_final': SelectDateWidget(years=range(1930, 2015)),
            'nota': Textarea(attrs={'cols': 50, 'rows': 5}),
            
        }
        
        
class TerapiaPacienteForm(forms.ModelForm):
    class Meta:
        model = Terapia
        fields = ('nombre',)
                
        widgets = {
            'nombre': TextInput(attrs={'size':15}),
            
        }
        
        
class ResultadosLabPacienteForm(forms.ModelForm):
    class Meta:
        model = ResultadosLab
        fields = ('nombre_analisis','fecha','resultado','marca','nota')
                
        widgets = {
            'nombre_analisis': TextInput(attrs={'size':15}),
            'fecha': SelectDateWidget(years=range(1930, 2015)),
            'resultado': NumberInput(attrs={'size':15,'placeholder': _("valor")}),
            'nota': Textarea(attrs={'cols': 30, 'rows': 5}),
            
        }
        
        
class CitaPacienteForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = ('proveedor','fecha','hora','proposito','nombre_especialista','especialidad','nota')
                
        widgets = {
            'proveedor': TextInput(attrs={'size':20}),
            'fecha': SelectDateWidget(years=range(1930, 2015)),
            'hora': TextInput(attrs={'size':20,'placeholder': _("ej: 11:40")}),
            'proposito': TextInput(attrs={'size':15}),
            'nombre_especialista': TextInput(attrs={'size':30}),
            'especialidad': TextInput(attrs={'size':30}),
            'nota': Textarea(attrs={'cols': 30, 'rows': 5}),
        }
      
      
class ResumenClinicoPacienteForm(forms.ModelForm):
    class Meta:
        model = ResumenClinico
        fields = ('resumen',)
                
        widgets = {
            'resumen': Textarea(attrs={'cols': 40, 'rows': 10}),
            
        }
        

class EnfermedadPacienteForm(forms.ModelForm):
    class Meta:
        model = Enfermedad
        fields = ('nombre','estado','fecha','evolucion','nota')
                
        widgets = {
            'nombre': TextInput(attrs={'size':25}),
            'fecha': SelectDateWidget(years=range(1930, 2015)),
            'evolucion': TextInput(attrs={'size':20}),
            'nota': Textarea(attrs={'cols': 30, 'rows': 5}),
        }
        
class CirugiaPacienteForm(forms.ModelForm):
    class Meta:
        model = Cirugia
        fields = ('nombre','fecha','hora','ubicacion_cuerpo','proveedor','nota')
                
        widgets = {
            'nombre': TextInput(attrs={'size':25}),
            'fecha': SelectDateWidget(years=range(1930, 2015)),
            'hora': TextInput(attrs={'size':20,'placeholder': _("ej: 11:40")}),
            'ubicacion_cuerpo': TextInput(attrs={'size':20}),
            'proveedor': TextInput(attrs={'size':30}),
            'nota': Textarea(attrs={'cols': 30, 'rows': 5}),
        }
        