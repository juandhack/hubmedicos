import os, sys
# -*- encoding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from apps.perfilesmedicos.models import RedesSociales

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

class PerfilBasico(models.Model):
	user = models.OneToOneField(User)
	dni = models.CharField(max_length=20)
	nombres = models.CharField(max_length=255, null=True, blank=True)
	apellidos = models.CharField(max_length=255, null=True, blank=True)
	acerca_de = models.TextField("Extracto Personal",null=True, blank=True)
	sexo = models.CharField(max_length=1,null=True,blank=True, choices=KIND_SEXO)
        fecha_nacimiento = models.DateField(unique=True, null=True, blank=True)
        grupo_sanguineo = models.CharField("Grupo Sanguíneo",max_length=4,null=True,blank=True,choices=GRUPO_SANGUINEO)
	imagen = models.ImageField("Tu foto",upload_to='pictures',null=True,blank=True)
	def __unicode__(self):
		return self.dni
	
KIND_PAIS = (
   ('Colombia','Colombia'),
)


KIND_DPTO = (
        ('Amazonas','Amazonas'),
        ('Antioquia','Antioquia'),
	('Atlantico','Atlantico'),
	('Bolivar','Bolivar'),
	('Boyacá','Boyacá'),
	('Caldas','Caldas'),
	('Caqueta','Caquetá'),
	('Casanare','Casanare'),
	('Cauca','Cauca'),
	('Cesar','Cesar'),
	('Choco','Chocó'),
	('Cordoba','Córdoba'),
	('Cundinamarca','Cundinamarca'),
	('Guainia','Guainía'),
	('Guaviare','Guaviare'),
	('Huila','Huila'),
	('La Guajira','La Guajira'),
	('Magdalena','Magdalena'),
	('Meta','Meta'),
	('Narino','Nariño'),
	('Norte de Santander','Norte de Santander'),
	('Putumayo','Putumayo'),
	('Quindio','Quindio'),
	('Risaralda','Risaralda'),
	('San Andres y Providencia','San Andres y Providencia'),
	('Santander','Santander'),
	('Sucre','Sucre'),
	('Tolima','Tolima'),
	('Valle','Valle'),
	('Vaupes','Vaupés'),
	('Vichada','Vichada'),
)

KIND_CIUDAD = (
	('Leticia','Leticia'),
        ('Medellin',u'Medellín'),
        ('Arauca','Arauca'),
	('Barranquilla','Barranquilla'),
	('Cartagena','Cartgena'),
	('Tunja','Tunja'),
	('Manizales','Manizales'),
	('Florencia','Florencia'),
	('Yopal','Yopal'),
	('Popayan','Popayán'),
	('Valledupar','Valledupar'),
	('Quibdo','Quibdó'),
	('Monteria','Montería'),
	('Bogota',u'Bogotá'),
	('Puerto Inirida','Puerto Inírida'),
	('San Jose del Guaviare','San José del Guaviare'),
	('Neiva','Neiva'),
	('Riohacha','Riohacha'),
	('Santa Marta','Santa Marta'),
	('Villavicencio','Villavicencio'),
	('Pasto','Pasto'),
	('Cucuta','Cúcuta'),
	('Mocoa','Mocoa'),
	('Armenia','Armenia'),
	('Pereira','Pereira'),
	('San Andres','San Andres'),
	('Bucaramanga','Bucaramanga'),
	('Sincelejo','Sincelejo'),
	('Ibague','Ibagué'),
	('Cali','Cali'),
	('Mitu','Mitú'),
	('Puerto Carreno','Puerto Carreño'),
)


class ContactosBasico(models.Model):

	user = models.OneToOneField(User)
	pais = models.CharField("País",max_length=30, null=True, blank=True, choices=KIND_PAIS)
	dpto = models.CharField("Departamento",max_length=30, null=True, blank=True, choices=KIND_DPTO)
	ciudad = models.CharField("Ciudad",max_length=30, null=True, blank=True, choices=KIND_CIUDAD)
	telefono = models.CharField("Teléfono",max_length=25, null=True, blank=True)
	celular = models.CharField("Celular",max_length=30, null=True, blank=True)
	correo = models.EmailField("Correo",blank=True, null=True)

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
    ('Confiando','Confiado'),
    ('Ansioso','Ansioso'),
    ('Triste','Triste'),
    ('Sin energia','Sin energía'),
    ('Sin interes','Sin interés'),
    ('Con deseos de llorar','Con deseos de llorar'),
    ('Con ideas de muerte o suicidio','Con ideas de muerte o suicidio'),
    ('No puedo dormir','No puedo dormir'),
)

    
class SintomasGeneralesPaciente(models.Model):
    
    user = models.ForeignKey(User, null=True, blank=True)
    sintoma = models.CharField("Síntoma",max_length=50,null=True,blank=True,choices=SINTOMAS_GENERALES)
              
    class Meta:
		verbose_name = 'Sintomas'
		verbose_name_plural = 'Sintomas'
		
    def __unicode__(self):
		return self.sintoma
	
    @models.permalink
    def get_absolute_url(self):
		return('listar_sintomas_paciente')
	
    @models.permalink
    def get_delete_url(self):
                return ('eliminar_sintomas_paciente', [self.id, ])
    #code
    
class EstadosAnimoPaciente(models.Model):
    
    user = models.ForeignKey(User, null=True, blank=True)
    estado = models.CharField("Estado",max_length=50,null=True,blank=True,choices=ESTADO_ANIMO)
              
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

     

User.perfilbasicopaciente = property(lambda u: PerfilBasico.objects.get_or_create(user=u)[0])
User.contactospaciente = property(lambda u: ContactosBasico.objects.get_or_create(user=u)[0])
User.socialespaciente = property(lambda u: RedesSociales.objects.get_or_create(user=u)[0])
