import os, sys
# -*- encoding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm,PasswordChangeForm
from .models import *
from apps.perfilesmedicos.models import RedesSociales
from django.forms import Textarea,TextInput, URLInput, CharField, DateTimeInput, NumberInput, DateInput, FileInput
from django.forms.extras import SelectDateWidget
from django.forms.widgets import HiddenInput

class PerfilBasicoForm(forms.ModelForm):
    class Meta:
        model = PerfilBasico
        fields = ('dni','nombres','apellidos','fecha_nacimiento','acerca_de','grupo_sanguineo','sexo','imagen')
        
        widgets = {
            'dni': TextInput(attrs={'maxlength': 50, 'class': 'form-control','style':'width:300px'}),
            'nombres':TextInput(attrs={'maxlength': 50, 'class': 'form-control','style':'width:300px'}),
            'apellidos':TextInput(attrs={'maxlength': 50, 'class': 'form-control','style':'width:300px'}),
            'fecha_nacimiento': DateInput(format='%d/%m/%Y',attrs={'class': 'form-control', 'id':'datePicker2','style':'width:140px'}),
            'sexo': forms.Select(attrs={'style':'width:150px'}),
            'grupo_sanguineo': forms.Select(attrs={'style':'width:150px'}),
            'imagen': FileInput(attrs={'maxlength': 50, 'class': 'form-control','style':'width:250px'}),
            'acerca_de':Textarea(attrs={'cols': 30, 'rows': 10,'class': 'form-control','placeholder': _("Escribe un resumen de tu historial medico "),'style':'width:300px'}),
        }
        labels = {
            'dni': _('Documento de Identidad'),
            'fecha_nacimiento': _('Fecha de Nacimiento'),
            'grupo_sanguineo': _('Grupo de Sangre'),
            'acerca_de':_('Mi resumen medico')
           
        }
        
        
       
class ContactosBasicoForm(forms.ModelForm):
    class Meta:
        model = ContactosBasico
        fields = ('pais','dpto','ciudad','telefono','celular','correo')
        
        widgets = {
            'pais':forms.Select(attrs={'style':'width:213px'}),
            'dpto':forms.Select(attrs={'style':'width:213px'}),
            'ciudad':forms.Select(attrs={'style':'width:213px'}),
            'telefono': TextInput(attrs={'maxlength': 50, 'class': 'form-control','style':'width:200px'}),
            'celular': TextInput(attrs={'maxlength': 50, 'class': 'form-control','style':'width:200px'}),
            'correo': TextInput(attrs={'maxlength': 50, 'class': 'form-control','style':'width:200px'}),
        }
        
        labels = {
            'dpto': _('Departamento'),
        }
        
class RedesSocialesForm(forms.ModelForm):
    class Meta:
        model = RedesSociales
        fields = ('blog','twitter','facebook','linkedin','you_tube')
        
        widgets = {
           
            'blog':TextInput(attrs={'maxlength': 50, 'class': 'form-control','style':'width:200px','placeholder': _("ej: miblog.com")}),
            'twitter': TextInput(attrs={'maxlength': 50, 'class': 'form-control','style':'width:200px','placeholder': _("ej: twitter.com/miusuario")}),
            'facebook': TextInput(attrs={'maxlength': 50, 'class': 'form-control','style':'width:200px','placeholder': _("ej: facebook.com/miusuario")}),
            'linkedin': TextInput(attrs={'maxlength': 50, 'class': 'form-control','style':'width:200px','placeholder': _("ej: linkedin.com/miusuario")}),
            'you_tube':TextInput(attrs={'maxlength': 50, 'class': 'form-control','style':'width:200px','placeholder': _("ej: youtube.com/miusuario")}),
        }
        
       

class SintomasGeneralesPacienteForm(forms.ModelForm):
    class Meta:
        model = SintomasGeneralesPaciente
        exclude = ('user',)
        
        widgets = {
            'sintoma':forms.Select(attrs={'style':'width:30%'}),
        }
         
        
class SintomaAlteracionGlicemicaPacienteForm(forms.ModelForm):
    class Meta:
        model = SintomasAlteracionGlicemicaPaciente
        exclude = ('user',)
        
        widgets = {
            'sintoma':forms.Select(attrs={'style':'width:30%'}),
        }
         
        
class EstadoAnimoPacienteForm(forms.ModelForm):
    class Meta:
        model = EstadosAnimoPaciente
        exclude = ('user',)
        
    
        
        #code
    
    #code

class PesoPacienteForm(forms.ModelForm):
    class Meta:
        model = Peso
        exclude = ('user',)
         
        widgets = {
            'peso': TextInput(attrs={'maxlength': 50, 'class': 'form-control','placeholder': _("Kg"),'style':'width:130px'}),
            #'fecha': DateInput(format='%d/%m/%Y',attrs={'class': 'form-control', 'id':'datePicker','style':'width:130px'}),     
            #'hora': TextInput(attrs={'size': 6, 'class': 'form-control','maxlength': 3,'style':'width:130px','placeholder': _("ej: 11:40")}),       
            'nota': Textarea(attrs={'cols': 50, 'rows': 6,'class': 'form-control','style':'width:98%'}),
            
        }
        

class TallaPacienteForm(forms.ModelForm):
    class Meta:
        model = Talla
        exclude = ('user',)
         
        widgets = {
            'altura': TextInput(attrs={'maxlength': 50, 'class': 'form-control','placeholder': _("Cm"),'style':'width:130px'}),
            #'fecha': DateInput(format='%d/%m/%Y',attrs={'class': 'form-control', 'id':'datePicker','style':'width:130px'}),     
            #'hora': TextInput(attrs={'size': 6, 'class': 'form-control','maxlength': 3,'style':'width:130px','placeholder': _("ej: 11:40")}),       
            'nota': Textarea(attrs={'cols': 50, 'rows': 6,'class': 'form-control','style':'width:98%'}),  
        }       
       
        
   
class GlucosaPacienteForm(forms.ModelForm):
    class Meta:
        model = Glucemia
        exclude = ('user',)
                
        widgets = {
            'medicion': NumberInput(attrs={'class': 'form-control','placeholder': _("mg/dl"),'style':'width:200px'}),
            'contexto_medicion': forms.Select(attrs={'style':'width:200px'}),
            'tipo': forms.Select(attrs={'style':'width:200px'}),
            #'fecha': DateInput(format='%d/%m/%Y',attrs={'class': 'form-control', 'id':'datePicker','style':'width:200px'}),     
            #'hora': TextInput(attrs={'size': 6, 'class': 'form-control','maxlength': 3,'style':'width:130px','placeholder': _("ej: 11:40")}),
            'nota': Textarea(attrs={'cols': 50, 'rows': 6,'class': 'form-control','style':'width:98%'}),   
        }
        
        labels = {
            'contecto_medicion': ('Contexto medición'),
            'tipo':('Tipo de sangre'),
        }
        
class HemoglobinaPacienteForm(forms.ModelForm):
    class Meta:
        model = Hemoglobina
        exclude = ('user',)
                
        widgets = {
            'porcentaje': NumberInput(attrs={'class': 'form-control','placeholder': _("%"),'style':'width:130px'}),
        }
   
        
class ColesterolPacienteForm(forms.ModelForm):
    class Meta:
        model = Colesterol
        exclude = ('user',)
         
          
        widgets = {
            'ldl': NumberInput(attrs={'class': 'form-control','placeholder': _("mg/dL"),'style':'width:130px'}),
            'hdl': NumberInput(attrs={'class': 'form-control','placeholder': _("mg/dL"),'style':'width:130px'}),     
            'trigliceridos': NumberInput(attrs={'class': 'form-control','placeholder': _("mg/dL"),'style':'width:130px'}),
            'colesterol_total':NumberInput(attrs={'class': 'form-control','placeholder': _("mg/dL"),'style':'width:130px'}),
            #'fecha': DateInput(format='%d/%m/%Y',attrs={'class': 'form-control', 'id':'datePicker','style':'width:130px'}),     
            #'hora': TextInput(attrs={'size': 6, 'class': 'form-control','maxlength': 3,'style':'width:130px','placeholder': _("ej: 11:40")}),
            'nota': Textarea(attrs={'cols': 50, 'rows': 5,'class': 'form-control','style':'width:98%'}),
            
        }       
               
        
class PresionPacienteForm(forms.ModelForm):
    class Meta:
        model = Presion
        exclude = ('user',)
        
        widgets = {
            'sistolica': NumberInput(attrs={'class': 'form-control','placeholder': _("mmHg"),'style':'width:200px'}),
            'diastolica': NumberInput(attrs={'class': 'form-control','placeholder': _("mmHg"),'style':'width:200px'}),     
            'pulso': NumberInput(attrs={'class': 'form-control','placeholder': _("mmHg"),'style':'width:200px'}),
            'latido_irregular':forms.Select(attrs={'style':'width:200px'}),
            #'fecha': DateInput(format='%d/%m/%Y',attrs={'class': 'form-control', 'id':'datePicker','style':'width:200px'}),     
            #'hora': TextInput(attrs={'size': 6, 'class': 'form-control','maxlength': 3,'style':'width:130px','placeholder': _("ej: 11:40")}),
            'nota': Textarea(attrs={'cols': 50, 'rows': 5,'class': 'form-control','style':'width:98%'}),
            
        }           
        
        
class RutinaEjercicioPacienteForm(forms.ModelForm):
    class Meta:
        model = RutinaEjercicio
        exclude = ('user',)
        
        widgets = {
            'nombre': TextInput(attrs={'maxlength': 50, 'class': 'form-control','placeholder': _("ej: ciclismo")}),
            'descripcion': Textarea(attrs={'cols': 10, 'rows': 3,'class': 'form-control','placeholder': _("ej: entrenamiento para partida de tenis")}),
            'duracion': NumberInput(attrs={'class': 'form-control','placeholder': _("minutos"),'style':'width:200px'}),
            'distancia': NumberInput(attrs={'class': 'form-control','placeholder': _("km"),'style':'width:200px'}),
            'num_pasos': NumberInput(attrs={'class': 'form-control','style':'width:200px'}),
            'calorias_quemadas': NumberInput(attrs={'class': 'form-control','style':'width:200px'}),
            #'fecha': DateInput(format='%d/%m/%Y',attrs={'class': 'form-control', 'id':'datePicker','style':'width:200px'}),     
            #'hora': TextInput(attrs={'size': 6, 'class': 'form-control','maxlength': 3,'style':'width:130px','placeholder': _("ej: 11:40")}),
            'nota': Textarea(attrs={'cols': 50, 'rows': 5,'class': 'form-control'}),
            
        }
        
class RutinaAlimentacionPacienteForm(forms.ModelForm):
    class Meta:
        model = RutinaAlimentacion
        exclude = ('user',)
                
        widgets = {
            'nombre': TextInput(attrs={'maxlength': 50, 'class': 'form-control','style':'width:30%'}),
            'tipo_comida':forms.Select(attrs={'style':'width:18%'}),
            'tamanio_porcion': NumberInput(attrs={'class': 'form-control','style':'width:15%'}),
            'cantidad_porcion': NumberInput(attrs={'class': 'form-control','placeholder': _("ej: 2"),'style':'width:15%'}),
            'calorias': NumberInput(attrs={'class': 'form-control','style':'width:15%'}),
            #'fecha': DateInput(format='%d/%m/%Y',attrs={'class': 'form-control', 'id':'datePicker','style':'width:200px'}),     
            #'hora': TextInput(attrs={'size': 6, 'class': 'form-control','maxlength': 3,'style':'width:130px','placeholder': _("ej: 11:40")}),
            'nota': Textarea(attrs={'cols': 50, 'rows': 5,'class': 'form-control','style':'width:98%'}),
            
        }
        
class MedicamentoPacienteForm(forms.ModelForm):
    class Meta:
        model = Medicamento
        exclude = ('user','dosis','tipo_dosis','modo_admin','motivo_admin',)
                
        widgets = {
            'nombre': TextInput(attrs={'maxlength': 50, 'class': 'form-control','style':'width:300px','placeholder': _("ej: albuterol")}),
            'concentracion': NumberInput(attrs={'class': 'form-control','style':'width:30%','placeholder': _("ej: 500")}),
            'tipo_concentracion':forms.Select(attrs={'style':'width:30%'}),
            'dosis': NumberInput(attrs={'class': 'form-control','style':'width:100px','placeholder': _("ej: 2")}),
            'tipo_dosis':forms.Select(attrs={'class':'selectMenu','style':'width:300px'}),
            'frecuencia_admin': TextInput(attrs={'maxlength': 50, 'class': 'form-control','style':'width:30%','placeholder': _("ej: 2 veces al dia")}),
            'modo_admin':forms.Select(attrs={'class':'selectMenu','style':'width:300px'}),
            'motivo_admin': TextInput(attrs={'maxlength': 50, 'class': 'form-control','style':'width:300px'}),
            'fecha_inicio': DateInput(format='%d/%m/%Y',attrs={'class': 'form-control', 'id':'datePicker','style':'width:30%'}),
            'fecha_final': DateInput(format='%d/%m/%Y',attrs={'class': 'form-control', 'id':'datePicker2','style':'width:30%'}),
            'nota': Textarea(attrs={'cols': 50, 'rows': 6,'class': 'form-control','style':'width:98%'}),
            
        }
        
        labels = {

            
        }
        
        
class TerapiaPacienteForm(forms.ModelForm):
    class Meta:
        model = Terapia
        fields = ('nombre',)
                
        widgets = {
            'nombre': Textarea(attrs={'cols': 30, 'rows': 5,'class': 'form-control'}),
            
        }
        
        
class ResultadosLabPacienteForm(forms.ModelForm):
    class Meta:
        model = ResultadosLab
        exclude = ('user',)
                
        widgets = {
            'nombre_analisis': TextInput(attrs={'maxlength': 50, 'class': 'form-control','style':'width:300px'}),
            'fecha':  DateInput(format='%d/%m/%Y',attrs={'class': 'form-control', 'id':'datePicker','style':'width:200px'}),
            'resultado': NumberInput(attrs={'class': 'form-control','style':'width:300px','placeholder': _("ej: 5")}),
            'marca':forms.Select(attrs={'class':'selectMenu','style':'width:300px'}),
            'nota': Textarea(attrs={'cols': 30, 'rows': 5,'class': 'form-control'}),
            
        }
        
        
class CitaPacienteForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = ('proveedor','nombre_especialista','especialidad','proposito','fecha','hora','nota')
        exclude = ('user',)
                
        widgets = {
            'proveedor': TextInput(attrs={'maxlength': 50, 'class': 'form-control','style':'width:40%'}),
            'fecha': DateInput(format='%d/%m/%Y',attrs={'class': 'form-control', 'id':'datePicker','style':'width:20%'}),
            'hora': TextInput(attrs={'size': 6, 'class': 'form-control','maxlength': 3,'style':'width:20%','placeholder': _("ej: 11:40")}),
            'proposito': forms.Select(attrs={'style':'width:30%'}),
            'nombre_especialista': TextInput(attrs={'maxlength': 50, 'class': 'form-control','style':'width:40%'}),
            'especialidad': forms.Select(attrs={'style':'width:30%'}),
            'nota': Textarea(attrs={'cols': 50, 'rows': 6,'class': 'form-control','style':'width:98%'}),
        }
        
        labels = {
            
            'proveedor':_('Centro'),
            
        }
      
         
            
class ResumenClinicoPacienteForm(forms.ModelForm):
    class Meta:
        model = ResumenClinico
        fields = ('resumen',)
                
        widgets = {
            'resumen': Textarea(attrs={'cols': 70, 'rows': 15,'class': 'form-control'}),
        }
        
        labels = {
            'resumen': ('Mi historia médica - Reseña'),
            
        }
        

class EnfermedadPacienteForm(forms.ModelForm):
    class Meta:
        model = Enfermedad
        exclude = ('user',)
                
        widgets = {
            'nombre': TextInput(attrs={'maxlength': 50, 'class': 'form-control','style':'width:300px'}),
            'estado': forms.Select(attrs={'class':'selectMenu','style':'width:300px'}),
            'fecha_inicio': DateInput(format='%d/%m/%Y',attrs={'class': 'form-control', 'id':'datePicker','style':'width:300px'}),
            'fecha_final': DateInput(format='%d/%m/%Y',attrs={'class': 'form-control', 'id':'datePicker2','style':'width:300px'}),
            'evolucion': TextInput(attrs={'maxlength': 50, 'class': 'form-control','style':'width:300px'}),
            'nota': Textarea(attrs={'cols': 30, 'rows': 5,'class': 'form-control'}),
        }
        
class CirugiaPacienteForm(forms.ModelForm):
    class Meta:
        model = Cirugia
        exclude = ('user',)
                
        widgets = {
            'nombre': TextInput(attrs={'maxlength': 50, 'class': 'form-control'}),
            'fecha': DateInput(format='%d/%m/%Y',attrs={'class': 'form-control', 'id':'datePicker'}),
            'ubicacion_cuerpo': TextInput(attrs={'maxlength': 50, 'class': 'form-control'}),
            'proveedor': TextInput(attrs={'maxlength': 50, 'class': 'form-control'}),
            'nota': Textarea(attrs={'cols': 30, 'rows': 5,'class': 'form-control'}),
        }
 


class AntecedentesFamiliaresForm(forms.ModelForm):
    class Meta:
      
        model = AntecedentesFamiliares
        exclude = ('user',)
                
        widgets = {
            
            'nombre_familiar': TextInput(attrs={'maxlength': 30, 'class': 'form-control'}),
            'relacion':forms.Select(attrs={'class':'selectMenu','style':'width:300px'}),
            'enfermedad': TextInput(attrs={'maxlength': 30, 'class': 'form-control'}),
            'fecha_inicio': DateInput(format='%d/%m/%Y',attrs={'class': 'form-control', 'id':'datePicker'}),
            'fecha_final': DateInput(format='%d/%m/%Y',attrs={'class': 'form-control', 'id':'datePicker2'}),
            'estado':forms.Select(attrs={'class':'selectMenu','style':'width:300px'}),
            'como_finalizo': TextInput(attrs={'size':25,'class': 'form-control'}),
            'nota': Textarea(attrs={'cols': 30, 'rows': 5,'class': 'form-control'}),
        }
        
        labels = {
            'relacion': ('Relación'),
            'como_finalizo':('Cómo evolucionó')
        }
        
    
       
class ToxicoForm(forms.ModelForm):
    class Meta:
        model = Toxico
        exclude = ('user',)
        
        widgets = {
            
            'num_cigarrillos': TextInput(attrs={'size': 3, 'class': 'form-control','maxlength': 3,'style':'width:50px'}),
            'num_anios_fumador':TextInput(attrs={'size': 3, 'class': 'form-control','maxlength': 3,'style':'width:50px'}),
            'tipo_bebedor':forms.Select(attrs={'class':'selectMenu','style':'width:200px'}),
            'tipo_droga':Textarea(attrs={'cols': 30, 'rows': 5,'class': 'form-control'}),
            
        }
        
        labels = {
            'num_anios_fumador':('Num años fumador'),
            'tipo_bebedor':('Frecuencia'),
      
        }
        
     
        

class AlergiaForm(forms.ModelForm):
    class Meta:
        model = Alergia
        exclude = ('user',)
        widgets = {
            
            'nombre': TextInput(attrs={'maxlength': 30, 'class': 'form-control','style':'width:320px'}),
            'reaccion': forms.Select(attrs={'class':'selectMenu','style':'width:320px'}),
            'tipo':forms.Select(attrs={'class':'selectMenu','style':'width:320px'}),
            'fecha_inicio': DateInput(format='%d/%m/%Y',attrs={'class': 'form-control', 'id':'datePicker','style':'width:320px'}),
            'nota': Textarea(attrs={'cols': 30, 'rows': 5,'class': 'form-control'}),
        }
        
        labels = {
            'fecha_recepcion':('Fecha de aplicación'),
            'num_secuencia':('Numero de secuencia'),
           
        }
  
        
class InmunizacionForm(forms.ModelForm):
    class Meta:
        model = Inmunizacion
        exclude = ('user',)
        
        widgets = {
            
            'nombre': TextInput(attrs={'maxlength': 30, 'class': 'form-control'}),
            'fecha_recepcion': DateInput(format='%d/%m/%Y',attrs={'class': 'form-control', 'id':'datePicker'}),
            'num_secuencia': TextInput(attrs={'size': 3, 'class': 'form-control','maxlength': 3,'style':'width:50px'}),
            'efectos_secundarios':Textarea(attrs={'cols': 30, 'rows': 3,'class': 'form-control'}),
            'nota': Textarea(attrs={'cols': 30, 'rows': 5,'class': 'form-control'}),
        }
        
        labels = {
            'fecha_recepcion':('Fecha de aplicación'),
            'num_secuencia':('Numero de secuencia'),
           
        }

class MedicamentoHistorialForm(forms.ModelForm):
    class Meta:
        model = MedicamentoHistorial
        exclude = ('user',)
    
        widgets = {
            
            'nombre': TextInput(attrs={'maxlength': 30, 'class': 'form-control'}),
            'motivo':TextInput(attrs={'maxlength': 30, 'class': 'form-control'}),
            'fecha_inicio': DateInput(format='%d/%m/%Y',attrs={'class': 'form-control', 'id':'datePicker'}),
            'fecha_fin': DateInput(format='%d/%m/%Y',attrs={'class': 'form-control', 'id':'datePicker2'}),
            'nota': Textarea(attrs={'cols': 30, 'rows': 5,'class': 'form-control'}),
        }
    

class GinecoHistorialForm(forms.ModelForm):
    class Meta:
        model = GinecoHistorial
        exclude = ('user',)
        
        widgets = {
            
            'edad_primera_menstruacion': TextInput(attrs={'size': 3, 'class': 'form-control','maxlength': 3,'style':'width:50px'}),
            'edad_menupausia':TextInput(attrs={'size': 3, 'class': 'form-control','maxlength': 3,'style':'width:50px'}),
            'edad_inicio_vida_sexual': TextInput(attrs={'size': 3, 'class': 'form-control','maxlength': 3,'style':'width:50px'}),
            'num_embarazos':TextInput(attrs={'size': 3, 'class': 'form-control','maxlength': 3,'style':'width:50px'}),
            'num_partos_vaginales':TextInput(attrs={'size': 3, 'class': 'form-control','maxlength': 3,'style':'width:50px'}),
            'num_abortos':TextInput(attrs={'size': 3, 'class': 'form-control','maxlength': 3,'style':'width:50px'}),
            'num_hijos_vivos':TextInput(attrs={'size': 3, 'class': 'form-control','maxlength': 3,'style':'width:50px'}),
            'num_cesareas':TextInput(attrs={'size': 3, 'class': 'form-control','maxlength': 3,'style':'width:50px'}),
            'num_embarazos_ectopicos':TextInput(attrs={'size': 3, 'class': 'form-control','maxlength': 3,'style':'width:50px'}),
            'causas_sangrados_vaginales':Textarea(attrs={'cols': 30, 'rows': 5,'class': 'form-control'}),
            'duracion_sangrados_vaginales':TextInput(attrs={'size': 3, 'class': 'form-control','maxlength': 3,'style':'width:50px'}),
           
        }
        
        labels = {
            'edad_primera_menstruacion':('Edad primera menstruación'),
            'num_cesareas':('Num cesáreas'),
            'num_embarazos_ectopicos':('Num embarazos ectópicos'),
            'duracion_sangrados_vaginales':('Duración sangrados vaginales(días)')
        }
         
class GinecoDiarioForm(forms.ModelForm):
    class Meta:
        model = GinecoDiario
        exclude = ('user',)
        
      
               
class ClubMedicoForm(forms.ModelForm):
    class Meta:
        model = ClubMedico
        exclude = ('user',)
        
class ClubMedicoSubscripcionForm(forms.ModelForm):
    class Meta:
        model = ClubMedicoSubscripcion
        exclude = ('user','rol')
        widgets = {
            
            'club': forms.Select(attrs={'style':'width:30%'}),   
        }
        
      
