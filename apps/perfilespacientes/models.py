import os, sys
# -*- encoding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from apps.perfilesmedicos.models import *

KIND_SEXO = (
   ('H','Hombre'),
   ('M','Mujer'),
)

GRUPO_SANGUINEO = (
   ('A+','A+'),
   ('A-','A-'),
   ('B+','B+'),
   ('B-','B-'),
   ('AB+','AB+'),
   ('AB-','AB-'),
   ('O+','O+'),
   ('O-','O-'),  
)

class SintomasGenerales(models.Model):
    descripcion = models.CharField(max_length = 160)
    
    def __unicode__(self):
        return self.descripcion
    

class EstadosAnimo(models.Model):
    descripcion = models.CharField(max_length = 120)
    
    def __unicode__(self):
        return self.descripcion
    
    
class SintomasAlteracionGlicemica(models.Model):
    descripcion = models.CharField(max_length = 160)
    
    def __unicode__(self):
        return self.descripcion
    
    
class ContextoMedicion(models.Model):
    descripcion = models.CharField(max_length = 120)
    
    def __unicode__(self):
        return self.descripcion
    
    
class TipoConcentracion(models.Model):
    descripcion = models.CharField(max_length = 120)
    
    def __unicode__(self):
        return self.descripcion
    
    
class TipoDosis(models.Model):
    descripcion = models.CharField(max_length = 120)
    
    def __unicode__(self):
        return self.descripcion
    
    
class ModoAdministracion(models.Model):
    descripcion = models.CharField(max_length = 120)
    
    def __unicode__(self):
        return self.descripcion
    

class Marca(models.Model):
    descripcion = models.CharField(max_length = 120)
    
    def __unicode__(self):
        return self.descripcion
    
    
class EstadoEnfermedad(models.Model):
    descripcion = models.CharField(max_length = 120)
    
    def __unicode__(self):
        return self.descripcion
    

class TipoComida(models.Model):
    descripcion = models.CharField(max_length = 160)
    
    def __unicode__(self):
        return self.descripcion
    

class Latido(models.Model):
    descripcion = models.CharField(max_length = 120)
    
    def __unicode__(self):
        return self.descripcion
    
    
class TipoSangre(models.Model):
    descripcion = models.CharField(max_length = 120)
    
    def __unicode__(self):
        return self.descripcion
      
class RelacionFamiliar(models.Model):
    descripcion = models.CharField(max_length = 160)
    
    def __unicode__(self):
        return self.descripcion
      
class ReaccionAlergia(models.Model):
    descripcion = models.CharField(max_length = 160)
    
    def __unicode__(self):
        return self.descripcion


class PerfilBasico(models.Model):
	user = models.OneToOneField(User)
	dni = models.CharField(max_length=20)
	nombres = models.CharField(max_length=255, null=True, blank=True)
	apellidos = models.CharField(max_length=255, null=True, blank=True)
	acerca_de = models.TextField("Extracto Personal",null=True, blank=True)
	sexo = models.CharField(max_length=10,null=True,blank=True, choices=KIND_SEXO)
        fecha_nacimiento = models.DateField(unique=True, null=True, blank=True)
        grupo_sanguineo = models.CharField("Grupo Sanguíneo",max_length=4,null=True,blank=True,choices=GRUPO_SANGUINEO)
	imagen = models.ImageField("Tu foto",upload_to='pictures',null=True,blank=True)
	def __unicode__(self):
		return self.dni
	

class ContactosBasico(models.Model):

	user = models.OneToOneField(User)
	pais = models.ForeignKey(Pais, null=True, blank=True)
	dpto = models.ForeignKey(Dpto, null=True, blank=True)
	ciudad = models.ForeignKey(Ciudad, null=True, blank=True)
	telefono = models.CharField("Teléfono",max_length=25, null=True, blank=True)
	celular = models.CharField(max_length=30, null=True, blank=True)
	correo = models.EmailField(blank=True, null=True)

	def __unicode__(self):
	     return u'%s %s' % (self.dpto, self.ciudad)

SINTOMAS_GENERALES = (
    ('Malestar general','Malestar general'),
    ('Ansiedad','Ansiedad'),
    ('Nerviosismo','Nerviosismo'),
    ('Dolor de cabeza ','Dolor de cabeza'),
    ('Dolor de cuello ','Dolor de cuello'),
    ('Dolor de oidos ','Dolor de oídos'),
    ('Dolor de garganta','Dolor de garganta'),
    ('Dolor de encias','Dolor de encías'),
    ('Dolor de pecho','Dolor de pecho'),
    ('Dolor de articulaciones','Dolor de articulaciones'),
    ('Dolor de abdomen','Dolor de abdomen'),
    ('Dolor de brazos','Dolor de manos'),
    ('Dolor de piernas','Dolor de piernas'),
    ('Dolor de vejiga','Dolor de vejiga'),
    ('Dolor de genitales','Dolor de genitales'),
    ('Fiebre','fiebre'),
    ('Escalofrios','Escalofríos'),
    ('Frio excesivo y anormal','Frio excesivo y anormal'),
    ('Dificultad respiratoria','Dificultad respiratoria'),
    ('Tos con expectoracion','Tos con expectoración'),
    ('Flujo nasal de cantidad y color anormal','Flujo nasal de cantidad y color anormal'),
    ('Perdida de apetito','Pérdida de apetito'),
    ('Aumento de frecuencia urinaria','Aumento de frecuencia urinaria'),
    ('Cambio de peso injustificdo','Cambio de peso injustificado'),
    ('Nauseas','Nauseas'),
    ('Vomito','Vómito'),
    ('Sangrado por la nariz','Sangrado por la nariz'),
    ('Sangrado por la boca','Sangrado por la boca'),
    ('Sangrado por los genitales','Sangrado por los genitales'),
    ('Sangrado por el recto','Sangrado por el recto'),
    ('Diarrea','Diarrea'),
    ('Estrenimiento','Estreñimiento'),
    ('Ausencia o retraso menstrual','Ausencia o retraso menstrual'),
)

ESTADO_ANIMO = (
    
    ('Feliz','Feliz'),
    ('Optimista','Optimista'),
    ('Euforico','Eufórico'),
    ('Entusiasmado','Entusiasmado'),
    ('Emocionado','Emocionado'),
    ('Sentimental','Sentimental'),
    ('Confiado','Confiado'),
    ('Asombrado','Asombrado'),
    ('Angustiado','Angustiado'),
    ('Ansioso','Ansioso'),
    ('Triste','Triste'),
    ('Inquieto','Inquieto'),
    ('Preocupado','Preocupado'),
    ('Tenso','Tenso'),
    ('Apatico','Apático'),
    ('Aburrido','Aburrido'),
    ('Melancolico','Melancólico'),
    ('Nostalgico','Nostálgico'),
    ('Avergonzado','Avergonzado'),
    ('Furioso','Furioso'),
    ('De mal humor','De mal humor'),
    ('Inseguro','Inseguro'),
    ('Desesperado','Desesperado'),
    ('Infeliz','Infeliz'),
)

SINTOMAS_ALTERACION_GLICEMICA = (
    
    ('He sentido mucha sed','He sentido mucha sed'),
    ('He sentido mucha hambre','He sentido mucha hambre'),
    ('Me siento cansado siempre','Me siento cansado siempre'),
    ('He tenido vision borrosa','He tenido visión borrosa'),
    ('He sentido entumecimiento en mis pies y manos','He sentido entumecimiento en mis pies y manos'),
    ('He sentido hormigueo en mis pies y manos','He sentido hormigueo en mis pies y manos'),
    ('Estoy perdiendo peso sin proponermelo','Estoy perdiendo peso sin proponérmelo'),
    ('Estoy orinando con mayor frecuencia','Estoy orinando con mayor frecuencia'),
    ('Mis heridas o moretones tardan en sanar','Mis heridas o moretones tardan en sanar'),
    ('Mi respiracion ha estado profuna y rapida','Mi respiración ha estado profuna y rápida'),
    ('Siento mi boca y piel seca','Siento mi boca y piel seca'),
    ('Mi cara se enrojece','Mi cara se enrojece'),
    ('Mi aliento ha tenido olor a fruta','Mi aliento ha tenido olor a fruta'),
    ('He sentido nuseas','He sentido naúseas'),
    ('He vomitado','He vomitado'),
    ('Tengo incapacidad para retener los liquidos','Tengo incapacidad para retener los líquidos'),
    ('He sentido dolor de estomago','He sentido dolor de estómago'),
    ('He tenido infecciones frecuentes en piel, vejiga o encias','He tenido infecciones frecuentes en piel, vejiga o encías'),
    ('He sentido dolor de cabeza ','He sentido dolor de cabeza'),
    ('Me he sentido muy nervioso','Me he sentido muy nervioso'),
    ('Me he sentido con ansiedad','Me he sentido con ansiedad'),
    ('He sentido palpitaciones','He sentido palpitaciones'),
    ('He sentido temblores','He sentido temblores'),
    ('He sentido sudoracion fria','He sentido sudoración fría'),
    ('He sentido debilidad ','He sentido debilidad'),
    ('He sentido dificultad respiratoria','He sentido dificultad respiratoria'),
    ('He sentido fatiga','He sentido fatiga'),
    ('He sentido disminucion del apetito','He sentido disminución del apetito'),
    ('He sentido dolores y rigidez muscular','He sentido dolores y rigidez muscular'),
   
)
   
class SintomasGeneralesPaciente(models.Model):
    
    user = models.ForeignKey(User, null=True, blank=True)
    sintoma =  models.ForeignKey(SintomasGenerales, null=True, blank=True)
              
    class Meta:
		verbose_name = 'Sintomas'
		verbose_name_plural = 'Sintomas'
		
    def __unicode__(self):
		return self.sintoma
	
    @models.permalink
    def get_absolute_url(self):
		return ('listar_sintomas_paciente')
	
    @models.permalink
    def get_delete_url(self):
                return ('eliminar_sintomas_paciente')
    #code
    
class SintomasAlteracionGlicemicaPaciente(models.Model):
    
    user = models.ForeignKey(User, null=True, blank=True)
    sintoma = models.ForeignKey(SintomasAlteracionGlicemica, null=True, blank=True)
              
    class Meta:
		verbose_name = 'Sintomas Glicemicos'
		verbose_name_plural = 'Sintomas Glicemicos'
		
    def __unicode__(self):
		return self.sintoma
	
    @models.permalink
    def get_absolute_url(self):
		return('listar_sintomas_alteracion_glicemica_paciente')
	
    @models.permalink
    def get_delete_url(self):
                return ('eliminar_sintomas_alteracion_glicemica_paciente', [self.id, ])
    #code
    
class EstadosAnimoPaciente(models.Model):
    
    user = models.ForeignKey(User, null=True, blank=True)
    estado = models.ForeignKey(EstadosAnimo, null=True, blank=True)
              
    class Meta:
		verbose_name = 'Estado'
		verbose_name_plural = 'Estado'
		
    def __unicode__(self):
		return self.estado
	
    @models.permalink
    def get_absolute_url(self):
		return('listar_estado_animo_paciente')
	
    @models.permalink
    def get_delete_url(self):
                return ('eliminar_estado_animo_paciente', [self.id, ])
    #code


class Peso(models.Model):
    
    user = models.ForeignKey(User,null=True,blank=True)
    peso = models.SmallIntegerField("Peso",)
    fecha = models.DateField(unique=True)
    hora = models.CharField(max_length=30,null=True,blank=True)
    nota = models.TextField(null=True, blank=True)
    class Meta:
		verbose_name = 'Peso'
		verbose_name_plural = 'Peso'
		
    def __unicode__(self):
		return self.peso
	
    @models.permalink
    def get_absolute_url(self):
		return('listar_peso_paciente')
	
    @models.permalink
    def get_delete_url(self):
                return ('eliminar_peso_paciente', [self.id, ])
    #code
   

class Talla(models.Model):
    
    user = models.ForeignKey(User,null=True,blank=True)
    altura = models.SmallIntegerField("Altura en cm")
    fecha = models.DateField(unique=True)
    hora = models.CharField(max_length=30,null=True,blank=True)
    nota = models.TextField(null=True, blank=True)
    
    class Meta:
		verbose_name = 'Altura'
		verbose_name_plural = 'Altura'
		
    def __unicode__(self):
		return self.altura
	
    @models.permalink
    def get_absolute_url(self):
		return('listar_talla_paciente')
	
    @models.permalink
    def get_delete_url(self):
                return ('eliminar_talla_paciente', [self.id, ])
    #code
 
CONTEXTO_MEDICION = (
    
    ('Antes de dormir','Antes de dormir'),
    ('Antes de hacer ejercicio','Antes de hacer ejercicio'),
    ('Antes de la cena','Antes de la cena'),
    ('Antes de la comida','Antes de la comida'),
    ('Antes del almuerzo','Antes del almuerzo'),
    ('Antes del desayuno','Antes del desayuno'),
    ('Ayuno','Ayuno'),
    ('Despues de hacer ejercicio','Después de hacer ejercicio'),
    ('Despues de la cena','Después de la cena'),
    ('Despues de la comida','Después de la comida'),
    ('Despues del almuerzo','Después del almuerzo'),
    ('Despues del desayuno','Después del desayuno'),
    ('No en ayuno','No en ayuno'),
    ('Omitir','Omitir'),
   
)

TIPO = (
    ('Plasma','Plasma'),
    ('Sangre completa', 'Sangre completa'),
)
    
class Glucemia(models.Model):
    user = models.ForeignKey(User,null=True,blank=True)
    medicion = models.SmallIntegerField("Medición")
    contexto_medicion = models.ForeignKey(ContextoMedicion, null=True, blank=True)
    tipo = models.ForeignKey(TipoSangre, null=True, blank=True)
    fecha = models.DateField(unique=True)
    hora = models.CharField(max_length=30,null=True,blank=True)
    nota = models.TextField(null=True, blank=True)
    
    class Meta:
		verbose_name = 'Medicion'
		verbose_name_plural = 'Medicion'
		
    def __unicode__(self):
		return self.medicion
	
    @models.permalink
    def get_absolute_url(self):
		return('listar_gluco_paciente')
	
    @models.permalink
    def get_delete_url(self):
                return ('eliminar_gluco_paciente', [self.id, ])
    #code
    
class Hemoglobina(models.Model):
    user = models.ForeignKey(User,null=True,blank=True)
    porcentaje = models.DecimalField(max_digits=10, decimal_places=2);
    
    class Meta:
		verbose_name = 'Porcentaje'
		verbose_name_plural = 'Porcentaje'
		
    def __unicode__(self):
		return self.porcentaje
	
    @models.permalink
    def get_absolute_url(self):
		return('listar_hemoglobina_paciente')
	
    @models.permalink
    def get_delete_url(self):
                return ('eliminar_hemoglobina_paciente', [self.id, ])
    #code
 
class Colesterol(models.Model):
    user = models.ForeignKey(User,null=True,blank=True)
    ldl = models.DecimalField("LDL",max_digits=10, decimal_places=2,null=True,blank=True);
    hdl = models.DecimalField("HDL",max_digits=10, decimal_places=2,null=True,blank=True);
    trigliceridos = models.DecimalField("Triglicéridos",max_digits=10, decimal_places=2,null=True,blank=True);
    colesterol_total = models.DecimalField("Colesterol Total",max_digits=10, decimal_places=2,null=True,blank=True);
    fecha = models.DateField(unique=True)
    hora = models.CharField(max_length=30,null=True,blank=True)
    nota = models.TextField(null=True, blank=True)
    class Meta:
		verbose_name = 'Colesterol'
		verbose_name_plural = 'Colesterol'
		
    def __unicode__(self):
		return self.estado
	
    @models.permalink
    def get_absolute_url(self):
		return('listar_colesterol_paciente')
	
    @models.permalink
    def get_delete_url(self):
                return ('eliminar_colesterol_paciente', [self.id, ])
    #code   

LATIDO = (
    
    ('Si','Si'),
    ('No','No'),
    ('No sabe','No sabe'),
)

class Presion(models.Model):
    user = models.ForeignKey(User,null=True,blank=True)
    sistolica = models.SmallIntegerField("Sistólica (número superior)")
    diastolica = models.SmallIntegerField("Diastólica (número inferior)")
    pulso = models.SmallIntegerField("Pulso (latidos por minuto)",null=True,blank=True);
    latido_irregular = models.ForeignKey(Latido, null=True, blank=True)
    fecha = models.DateField(unique=True)
    hora = models.CharField(max_length=30,null=True,blank=True)
    nota = models.TextField(null=True, blank=True)
    class Meta:
		verbose_name = 'Presion arterial'
		verbose_name_plural = 'Presion arterial'
		
    def __unicode__(self):
		return self.sistolica
	
    @models.permalink
    def get_absolute_url(self):
		return('listar_presion_paciente')
	
    @models.permalink
    def get_delete_url(self):
                return ('eliminar_presion_paciente', [self.id, ])
    #code
 
class RutinaEjercicio(models.Model):
    user = models.ForeignKey(User,null=True,blank=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField("Descripción",max_length=150,null=True,blank=True)
    duracion = models.SmallIntegerField("Duración",null=True,blank=True)
    distancia = models.SmallIntegerField(null=True,blank=True)
    num_pasos = models.SmallIntegerField("Número de pasos",null=True,blank=True)
    calorias_quemadas = models.SmallIntegerField("Calorías quemadas",null=True,blank=True)
    fecha = models.DateField(unique=True)
    hora = models.CharField(max_length=30,null=True,blank=True)
    nota = models.TextField(null=True, blank=True)
    class Meta:
		verbose_name = 'Rutinas de Ejercicio'
		verbose_name_plural = 'Rutinas de Ejercicio'
		
    def __unicode__(self):
		return self.nombre
	
    @models.permalink
    def get_absolute_url(self):
		return('listar_ejercicio_paciente')
	
    @models.permalink
    def get_delete_url(self):
                return ('eliminar_ejercicio_paciente', [self.id, ])
    #code   

TIPO_COMIDA = (
    ('Almuerzo','Almuerzo'),
    ('Cena','Cena'),
    ('Desayuno','Desayuno'),
    ('Merienda','Merienda'),
)
class RutinaAlimentacion(models.Model):
    user = models.ForeignKey(User,null=True,blank=True)
    nombre = models.CharField(max_length=100)
    tipo_comida = models.ForeignKey(TipoComida, null=True, blank=True)
    tamanio_porcion = models.SmallIntegerField("Tamaño de la porción",null=True,blank=True)
    cantidad_porcion = models.SmallIntegerField("Cantidad porción",null=True,blank=True)
    calorias = models.SmallIntegerField("Calorías",null=True,blank=True)
    fecha = models.DateField(unique=True)
    hora = models.CharField(max_length=30,null=True,blank=True)
    nota = models.TextField(null=True, blank=True)
    class Meta:
		verbose_name = 'Rutinas de Alimentacion'
		verbose_name_plural = 'Rutinas de Alimentacion'
		
    def __unicode__(self):
		return self.nombre
	
    @models.permalink
    def get_absolute_url(self):
		return('listar_alimentacion_paciente')
	
    @models.permalink
    def get_delete_url(self):
                return ('eliminar_alimentacion_paciente', [self.id, ])
    #code
  
TIPO_CONCENTRACION = (
    
    ('Microgramos(mcg)','Microgramos(mcg)'),
    ('Miliequivalente(meq)','Miliequivalente(meq)'),
    ('Miliequivalente por mililitro(meq/ml)','Miliequivalente por mililitro(meq/ml)'),
    ('Miligramo(mg)','Miligramo(mg)'),
    ('Miligramo por mililitro(mg/ml)','Miligramo por mililitro(mg/ml)'),
    ('Mililitro(ml)','Mililitro(ml)'),
    ('Porcentaje(%)','Porcentaje(%)'),
    ('Unidad(u)','Unidad(u)'),
    ('Unidad internacional(ui)','Unidad internacional(ui)'),
    ('Unidades formadoras de colonias por mililitro(ufc/ml)','Unidades formadoras de colonias por mililitro(ufc/ml)'),
    ('Unidades por mililitro(u/ml)','Unidades por mililitro(u/ml)'),
)

TIPO_DE_DOSIS = (
    
    ('Almohadillas','Almohadillas'),
    ('Aplicador','Aplicador'),
    ('Barras','Barras'),
    ('Bolsas','Bolsas'),
    ('Capsulas','Cápsulas'),
    ('Comprimidos','Comprimidos'),
    ('Cucharadas','Cucharadas'),
    ('Cucharaditas','Cucharaditas'),
    ('Dosis','Dosis'),
    ('Dosis de inhalador','Dosis de inhalador'),
    ('Gotas','Gotas'),
    ('Goteros','Goteros'),
    ('Gramos(g)','Gramos(g)'),
    ('Inhalaciones','Inhalaciones'),
    ('Inyecciones','Inyecciones'),
    ('Jeringa','Jeringa'),
    ('Medidas','Medidas'),
    ('Microgramos(mcg)','Microgramos(mcg)'),
    ('Miligramos(mg)','Miligramos(mg)'),
    ('Mililitros(ml)','Mililitros(ml)'),
    ('Paquetes','Paquetes'),
    ('Parches','Parches'),
    ('Pastillas','Pastillas'),
    ('Porcentaje(%)','Porcentaje(%)'),
    ('Supositorios','Supositorios'),
    ('Unidades(U)','Unidades(U)'),
    ('Vaporizaciones','Vaporizaciones'),
)

MODO_ADMIN = (
    
    ('A traves de la piel','A través de la piel'),
    ('A traves de una sonda nasogastrica','A través de una sonda nasogástrica'),
    ('Bajo la lengua','Bajo la lengua'),
    ('En el oido','En el oído'),
    ('En el ojo','En el ojo'),
    ('En la nariz(vaporizaciones/notas)','En la nariz(vaporizaciones/notas)'),
    ('Inhalado','Inhalado'),
    ('Por inyeccion','Por inyección'),
    ('Por la boca','Por la boca'),
    ('Por una via intravenosa','Por una vía intravenosa'),
    ('Rectal','Rectal'),
    ('Vaginal','Vaginal'),
   
)


class Medicamento(models.Model):
    user = models.ForeignKey(User,null=True,blank=True)
    nombre = models.CharField(max_length=100)
    concentracion = models.SmallIntegerField("Concentración",max_length=100,null=True,blank=True)
    tipo_concentracion = models.ForeignKey(TipoConcentracion, null=True, blank=True)
    dosis = models.SmallIntegerField(max_length=100,null=True,blank=True)
    tipo_dosis = models.ForeignKey(TipoDosis, null=True, blank=True)
    modo_admin = models.ForeignKey(ModoAdministracion, null=True, blank=True)
    frecuencia_admin = models.CharField("Frecuencia de administración",max_length=100,null=True,blank=True)
    motivo_admin = models.CharField("Motivo de administración",max_length=100,null=True,blank=True)
    fecha_inicio = models.DateField(unique=True, null=True, blank=True)
    fecha_final = models.DateField(unique=True, null=True, blank=True)
    nota = models.TextField(null=True, blank=True)
    class Meta:
		verbose_name = 'Medicamento'
		verbose_name_plural = 'Medicamento'
		
    def __unicode__(self):
		return self.nombre
	
    @models.permalink
    def get_absolute_url(self):
		return('listar_medicamento_paciente')
	
    @models.permalink
    def get_delete_url(self):
                return ('eliminar_medicamento_paciente', [self.id, ])
    #code
    
class Terapia (models.Model):
    user = models.ForeignKey(User,null=True,blank=True)
    nombre = models.CharField(max_length=100)
    class Meta:
		verbose_name = 'Terapia'
		verbose_name_plural = 'Terapia'
		
    def __unicode__(self):
		return self.nombre
	
    @models.permalink
    def get_absolute_url(self):
		return('listar_terapia_paciente')
	
    @models.permalink
    def get_delete_url(self):
                return ('eliminar_terapia_paciente', [self.id, ])
    #code
    
    
MARCA = (
    
    ('Alto','Alto'),
    ('Anormal','Anormal'),
    ('Bajo','Bajo'),
    ('Critico','Crítico'),
    ('Indeterminado','Indeterminado'),
    ('Normal','Normal'),
)
  
class ResultadosLab(models.Model):
    user = models.ForeignKey(User,null=True,blank=True)
    nombre_analisis = models.CharField("Nombre del análisis",max_length=50)
    fecha = models.DateField(unique=True, null=True, blank=True)
    resultado = models.SmallIntegerField(max_length=100,null=True,blank=True)
    marca = models.ForeignKey(Marca, null=True, blank=True)
    nota = models.TextField(null=True, blank=True)
    class Meta:
		verbose_name = 'Resultados Laboratorio'
		verbose_name_plural = 'Resultados Laboratorio'
		
    def __unicode__(self):
		return self.nombre_analisis
	
    @models.permalink
    def get_absolute_url(self):
		return('listar_resultado_lab_paciente')
	
    @models.permalink
    def get_delete_url(self):
                return ('eliminar_resultado_lab_paciente', [self.id, ])
    #code
    
class Cita(models.Model):
    user = models.ForeignKey(User,null=True,blank=True)
    proveedor = models.CharField(max_length=100,null=True, blank=True)
    proposito = models.CharField("Propósito",max_length=100,null=True, blank=True)
    nombre_especialista = models.CharField(max_length=100,null=True, blank=True)
    especialidad = models.CharField(max_length=100,null=True, blank=True)
    fecha = models.DateTimeField(unique=True, null=True, blank=True)
    hora = models.CharField(max_length=30,null=True,blank=True)
    nota = models.TextField(null=True, blank=True)
    class Meta:
		verbose_name = 'Cita'
		verbose_name_plural = 'Cita'
		
    def __unicode__(self):
		return self.proveedor
	
    @models.permalink
    def get_absolute_url(self):
		return('listar_cita_paciente')
	
    @models.permalink
    def get_delete_url(self):
                return ('eliminar_cita_paciente', [self.id, ])
    #code
    
class ResumenClinico(models.Model):
    user = models.ForeignKey(User,null=True,blank=True)
    resumen = models.TextField(null=True, blank=True)
    class Meta:
		verbose_name = 'Resumen Clinico'
		verbose_name_plural = 'Resumen Clinico'
		
    def __unicode__(self):
		return self.resumen
	
    @models.permalink
    def get_absolute_url(self):
		return('listar_resumenclinico_paciente')
	
    @models.permalink
    def get_delete_url(self):
                return ('eliminar_resumenclinico_paciente', [self.id, ])
    #code
  
ESTADO_ENFERMEDAD = (
    
    ('Actual: actualmente tengo esto','Actual: actualmente tengo esto'),
    ('Intermitente: va y viene','Intermitente: va y viene'),
    ('Pasado: ya no tengo esto','Pasado: ya no tengo esto'),
    
    )
    
class Enfermedad(models.Model):
    user = models.ForeignKey(User,null=True,blank=True)
    nombre = models.CharField(max_length=100, null=True,blank=True)
    estado = models.ForeignKey(EstadoEnfermedad, null=True, blank=True)
    fecha_inicio = models.DateTimeField(unique=True, null=True, blank=True)
    fecha_final = models.DateTimeField(unique=True, null=True, blank=True)
    evolucion = models.CharField("Evolución",max_length=100,null=True,blank=True)
    actual = models.BooleanField(default=False)
    nota = models.TextField(null=True, blank=True)
    
    class Meta:
		verbose_name = 'Enfermedad'
		verbose_name_plural = 'Enfermedad'
		
    def __unicode__(self):
		return self.nombre
	
    @models.permalink
    def get_absolute_url(self):
		return('listar_enfermedad_paciente')
	
    @models.permalink
    def get_delete_url(self):
                return ('eliminar_enfermedad_paciente', [self.id, ])
    #code
   
    
class Cirugia(models.Model):
    user = models.ForeignKey(User,null=True,blank=True)
    nombre = models.CharField(max_length=100)
    fecha = models.DateTimeField(unique=True)
    ubicacion_cuerpo = models.CharField("Ubicación en el cuerpo",max_length=100,null=True,blank=True)
    proveedor = models.CharField("Nombre especialista",max_length=100,null=True,blank=True)
    nota = models.TextField(null=True, blank=True)

    class Meta:
		verbose_name = 'Cirugia'
		verbose_name_plural = 'Cirugia'
		
    def __unicode__(self):
		return self.nombre
	
    @models.permalink
    def get_absolute_url(self):
		return('listar_cirugia_paciente')
	
    @models.permalink
    def get_delete_url(self):
                return ('eliminar_cirugia_paciente', [self.id, ])
    #code
 
   
class AntecedentesFamiliares(models.Model):
    user = models.ForeignKey(User,null=True,blank=True)
    relacion = models.ForeignKey(RelacionFamiliar, null=True, blank=True)
    nombre_familiar = models.CharField(max_length=100)
    enfermedad = models.CharField(max_length=100)
    fecha_inicio = models.DateField(null=True, blank=True)
    fecha_final = models.DateField(null=True, blank=True)
    estado = models.ForeignKey(EstadoEnfermedad, null=True, blank=True)
    como_finalizo = models.CharField(max_length=100,null=True,blank=True)
    nota = models.TextField(null=True, blank=True)
    

    class Meta:
		verbose_name = 'Antecedentes Familiares'
		verbose_name_plural = 'Antecedentes Familiares'
		
    def __unicode__(self):
		return self.nombre
	
    @models.permalink
    def get_absolute_url(self):
		return('listar_familiar_paciente')
	
    @models.permalink
    def get_delete_url(self):
                return ('eliminar_familiar_paciente', [self.id, ])

    #code
 
ESTADO_BEBEDOR = (
    
    ('Social','Social'),
    ('Ocasional','Ocasional'),
    ('Frecuente','Frecuente'),
    
    )
 
class Toxico(models.Model):
    user = models.ForeignKey(User,null=True,blank=True)
    fumador = models.BooleanField(default=False)
    num_cigarrillos = models.SmallIntegerField(max_length=100, null=True, blank=True)
    num_anios_fumador = models.SmallIntegerField(max_length=100, null=True, blank=True)
    bebedor = models.BooleanField(default=False)
    tipo_bebedor = models.CharField(max_length=100,null=True,blank=True,choices=ESTADO_BEBEDOR)
    drogadicto = models.BooleanField(default=False)
    tipo_droga = models.CharField(max_length=100)

    class Meta:
		verbose_name = 'Toxicos'
		verbose_name_plural = 'Toxicos'
		
    def __unicode__(self):
		return self.fumador
	
    @models.permalink
    def get_absolute_url(self):
		return('listar_toxicos_paciente')
	
    @models.permalink
    def get_delete_url(self):
                return ('eliminar_toxicos_paciente', [self.id, ])
    #code
    
 
TIPO_ALERGIAS = (
    
    ('Alimento','Alimento'),
    ('Ambiental','Ambiental'),
    ('Animal','Animal'),
    ('Vegetal','Vegetal'),
    
    )
 
class Alergia(models.Model):
    user = models.ForeignKey(User,null=True,blank=True)
    nombre = models.CharField(max_length=100, null=True, blank=True)
    reaccion = models.ForeignKey(ReaccionAlergia, null=True, blank=True)
    tipo = models.CharField(max_length=100, null=True, blank=True, choices=TIPO_ALERGIAS)
    fecha_inicio = models.DateTimeField(unique=True, null=True, blank=True)
    nota = models.TextField(null=True, blank=True)

    class Meta:
		verbose_name = 'Alergia'
		verbose_name_plural = 'Alergia'
		
    def __unicode__(self):
		return self.nombre
	
    @models.permalink
    def get_absolute_url(self):
		return('listar_alergias_paciente')
	
    @models.permalink
    def get_delete_url(self):
                return ('eliminar_alergias_paciente', [self.id, ])
    #code
    

class Inmunizacion(models.Model):
    user = models.ForeignKey(User,null=True,blank=True)
    nombre = models.CharField(max_length=100, null=True, blank=True)
    fecha_recepcion = models.DateTimeField(unique=True, null=True, blank=True)
    num_secuencia = models.SmallIntegerField(max_length=100, null=True, blank=True)
    efectos_secundarios = models.CharField(max_length=100)
    nota = models.TextField(null=True, blank=True)

    class Meta:
		verbose_name = 'Inmunizacion'
		verbose_name_plural = 'Inmunizacion'
		
    def __unicode__(self):
		return self.nombre
	
    @models.permalink
    def get_absolute_url(self):
		return('listar_inmunizacion_paciente')
	
    @models.permalink
    def get_delete_url(self):
                return ('eliminar_inmunizacion_paciente', [self.id, ])
    #code
    
    
 
class MedicamentoHistorial(models.Model):
    user = models.ForeignKey(User,null=True,blank=True)
    nombre = models.CharField(max_length=100, null=True, blank=True)
    motivo = models.CharField(max_length=100, null=True, blank=True)
    fecha_inicio = models.DateTimeField(unique=True, null=True, blank=True)
    fecha_fin = models.DateTimeField(unique=True, null=True, blank=True)
    nota = models.TextField(null=True, blank=True)

    class Meta:
		verbose_name = 'Medicamento'
		verbose_name_plural = 'Medicamento'
		
    def __unicode__(self):
		return self.nombre
	
    @models.permalink
    def get_absolute_url(self):
		return('listar_medicamento_historial_paciente')
	
    @models.permalink
    def get_delete_url(self):
                return ('eliminar_medicamento_historial_paciente', [self.id, ])
    #code
    
class GinecoHistorial(models.Model):
    user = models.ForeignKey(User,null=True,blank=True)
    edad_primera_menstruacion = models.SmallIntegerField(null=True, blank=True)
    edad_menupausia = models.SmallIntegerField(null=True, blank=True)
    edad_inicio_vida_sexual = models.SmallIntegerField(null=True, blank=True)
    num_embarazos = models.SmallIntegerField(null=True, blank=True)
    num_partos_vaginales = models.SmallIntegerField(null=True, blank=True)
    num_abortos = models.SmallIntegerField(null=True, blank=True)
    num_hijos_vivos = models.SmallIntegerField(null=True, blank=True)
    num_cesareas = models.SmallIntegerField(null=True, blank=True)
    num_embarazos_ectopicos = models.SmallIntegerField(null=True, blank=True)
    sangrados_vaginales = models.BooleanField(default=False)
    causas_sangrados_vaginales = models.CharField(max_length=100)
    duracion_sangrados_vaginales = models.CharField(max_length=100)
    
    class Meta:
		verbose_name = 'Historial Ginecologico'
		verbose_name_plural = 'Historial Ginecologico'
		
    def __unicode__(self):
		return self.edad_primera_menstruacion
	
    @models.permalink
    def get_absolute_url(self):
		return('listar_gineco_historial_paciente')
	
    @models.permalink
    def get_delete_url(self):
                return ('eliminar_gineco_historial_paciente', [self.id, ])
    #code
  
  
TIPO_CICLOS_MENSTRUALES = (
    
    ('Regulares','Regulares'),
    ('Regulares','Regualares'),

    )


TIPO_ANTICONCEPTIVOS = (
    
    ('Orales','Orales'),
    ('Preservativos','Preservativos'),
    ('Implantes','Implantes'),
    ('Ligaduras','Ligaduras'),
    ('Espermicidas','Espermicidas'),
    ('Ritmo','Ritmo'),
    ('Otros','Otros'),
     
    )


class GinecoDiario(models.Model):
    user = models.ForeignKey(User,null=True,blank=True)
    ciclos_menstruales = models.CharField(max_length=100, null=True, blank=True, choices=TIPO_CICLOS_MENSTRUALES)
    duracion_ciclos = models.SmallIntegerField(null=True, blank=True)
    anticonceptivo = models.BooleanField(default=False)
    tipo_anticonceptivos = models.CharField(max_length=100,null=True, blank=True, choices=TIPO_ANTICONCEPTIVOS)
    tiempo_uso_anticonceptivos = models.SmallIntegerField(null=True, blank=True)
    resultado_citologia = models.CharField(max_length=100)
    resultado_mamografia = models.CharField(max_length=100)
    fecha_ultima_mestruacion = models.DateTimeField(unique=True, null=True, blank=True)
    fecha_ultima_citologia = models.DateTimeField(unique=True, null=True, blank=True)
    fecha_ultima_mamografia = models.DateTimeField(unique=True, null=True, blank=True)
     
    class Meta:
		verbose_name = 'Diario Ginecologico'
		verbose_name_plural = 'Diario Ginecologico'
		
    def __unicode__(self):
		return self.edad_primera_menstruacion
	
    @models.permalink
    def get_absolute_url(self):
		return('listar_gineco_diario_paciente')
	
    @models.permalink
    def get_delete_url(self):
                return ('eliminar_gineco_diario_paciente', [self.id, ])
    #code
    
    
class ClubMedico(models.Model):
    user = models.ForeignKey(User,null=True,blank=True)
    nombre_club = models.CharField(max_length=100)
  
    class Meta:
		verbose_name = 'Club Medico'
		verbose_name_plural = 'Club Medico'
		
    def __unicode__(self):
		return self.edad_primera_menstruacion
	
    @models.permalink
    def get_absolute_url(self):
		return('listar_club_paciente')
	
    @models.permalink
    def get_delete_url(self):
                return ('eliminar_club_paciente', [self.id, ])
    #code
    

    
User.perfilbasicopaciente = property(lambda u: PerfilBasico.objects.get_or_create(user=u)[0])
User.contactospaciente = property(lambda u: ContactosBasico.objects.get_or_create(user=u)[0])
User.socialespaciente = property(lambda u: RedesSociales.objects.get_or_create(user=u)[0])
