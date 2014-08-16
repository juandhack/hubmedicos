import os, sys
# -*- encoding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class Perfiles(models.Model):
	user = models.OneToOneField(User)
	dni = models.CharField(max_length=20)
	nombres = models.CharField(max_length=255, null=True, blank=True)
	apellidos = models.CharField(max_length=255, null=True, blank=True)
	acerca_de = models.TextField("Extracto Personal",null=True, blank=True)
	tipo_usuario = models.CharField(max_length=1,null=True,blank=True)

	def __unicode__(self):
		return self.dni

KIND_DPTO = (
   ('Amazonas','Amazonas'),
    ('Antioquia','Antioquia'),
	('Atlantico','Atlantico'),
	('Bolivar','Bolivar'),
	('Boyacá','Boyacá'),
	('Caldas','Caldas'),
	('Caquetá','Caquetá'),
	('Casanare','Casanare'),
	('Cauca','Cauca'),
	('Cesar','Cesar'),
	('Chocó','Chocó'),
	('Córdoba','Córdoba'),
	('Cundinamarca','Cundinamarca'),
	('Guainía','Guainía'),
	('Guaviare','Guaviare'),
	('Huila','Huila'),
	('La Guajira','La Guajira'),
	('Magdalena','Magdalena'),
	('Meta','Meta'),
	('Nariño','Nariño'),
	('Norte de Santander','Norte de Santander'),
	('Putumayo','Putumayo'),
	('Quindio','Quindio'),
	('Risaralda','Risaralda'),
	('San Andres y Providencia','San Andres y Providencia'),
	('Santander','Santander'),
	('Sucre','Sucre'),
	('Tolima','Tolima'),
	('Valle','Valle'),
	('Vaupés','Vaupés'),
	('Vichada','Vichada'),
)

KIND_CIUDAD = (
	('Leticia','Leticia'),
    ('Medellín',u'Medellín'),
    ('Arauca','Arauca'),
	('Barranquilla','Barranquilla'),
	('Cartgena','Cartgena'),
	('Tunja','Tunja'),
	('Manizales','Manizales'),
	('Florencia','Florencia'),
	('Yopal','Yopal'),
	('Popayán','Popayán'),
	('Valledupar','Valledupar'),
	('Quibdó','Quibdó'),
	('Montería','Montería'),
	('Bogotá',u'Bogotá'),
	('Puerto Inírida','Puerto Inírida'),
	('San José del Guaviare','San José del Guaviare'),
	('Neiva','Neiva'),
	('Riohacha','Riohacha'),
	('Santa Marta','Santa Marta'),
	('Villavicencio','Villavicencio'),
	('Pasto','Pasto'),
	('Cúcuta','Cúcuta'),
	('Mocoa','Mocoa'),
	('Armenia','Armenia'),
	('Pereira','Pereira'),
	('San Andres','San Andres'),
	('Bucaramanga','Bucaramanga'),
	('Sincelejo','Sincelejo'),
	('Ibagué','Ibagué'),
	('Cali','Cali'),
	('Mitú','Mitú'),
	('Puerto Carreño','Puerto Carreño,')
)

class Contactos(models.Model):

	user = models.OneToOneField(User)
	dpto = models.CharField("Departamento",max_length=30, null=True, blank=True, choices=KIND_DPTO)
	ciudad = models.CharField(max_length=30, null=True, blank=True, choices=KIND_CIUDAD)
	telefono = models.CharField("Tel",max_length=25, null=True, blank=True)
	celular = models.CharField(max_length=30, null=True, blank=True)
	correo = models.EmailField(blank=True, null=True)

	def __unicode__(self):
	     return u'%s %s' % (self.dpto, self.ciudad)



class RedesSociales(models.Model):
	user = models.OneToOneField(User)
	blog = models.CharField(max_length=255, null=True, blank=True)
	twitter = models.CharField(max_length=20, null=True, blank=True)
	facebook = models.CharField(max_length=30, null=True, blank=True)
	linkedin = models.CharField(max_length=30, null=True, blank=True)
	you_tube = models.CharField(max_length=30, null=True, blank=True)
    
   

class PerfilProfesional(models.Model):
	user = models.ForeignKey(User)
	organizacion = models.CharField("Nombre Entidad",max_length=255, null=True, blank=True)
	especialidad = models.CharField(max_length=255, null=True, blank=True)
	cargo = models.CharField(max_length=255, null=True, blank=True)
	aniosejercidos = models.CharField("Tiempo Ejercido",max_length=255, null=True, blank=True)
	numregistroprof = models.CharField("Registro Profesional",max_length=255, null=True, blank=True)
	funcionesrealizadas = models.TextField("Funciones Realizadas",null=True, blank=True)


class PerfilAcademico(models.Model):
	user = models.ForeignKey(User)
	institucion = models.CharField("Universidad",max_length=255, null=True, blank=True)
	titulo = models.CharField("Titulo",max_length=255, null=True, blank=True)
	logros = models.TextField(null=True, blank=True)



User.perfiles = property(lambda u: Perfiles.objects.get_or_create(user=u)[0])
User.contactos = property(lambda u: Contactos.objects.get_or_create(user=u)[0])
User.sociales = property(lambda u: RedesSociales.objects.get_or_create(user=u)[0])
User.profesional = property(lambda u: PerfilProfesional.objects.get_or_create(user=u)[0])
User.academico = property(lambda u: PerfilAcademico.objects.get_or_create(user=u)[0])


	


