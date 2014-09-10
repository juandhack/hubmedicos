import os, sys
# -*- encoding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

KIND_SEXO = (
   ('Hombre','Hombre'),
   ('Mujer','Mujer'),
)

class PerfilBasico(models.Model):
	user = models.OneToOneField(User)
	dni = models.CharField(max_length=20)
	nombres = models.CharField(max_length=255, null=True, blank=True)
	apellidos = models.CharField(max_length=255, null=True, blank=True)
	acerca_de = models.TextField("Extracto Personal",null=True, blank=True)
	sexo = models.CharField(max_length=1,null=True,blank=True, choices=KIND_SEXO)
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
	('Puerto Carreno','Puerto Carreño,')
)


class ContactosBasico(models.Model):

	user = models.OneToOneField(User)
	pais = models.CharField("Pa?s",max_length=30, null=True, blank=True, choices=KIND_PAIS)
	dpto = models.CharField("Departamento",max_length=30, null=True, blank=True, choices=KIND_DPTO)
	ciudad = models.CharField(max_length=30, null=True, blank=True, choices=KIND_CIUDAD)
	telefono = models.CharField("Tel",max_length=25, null=True, blank=True)
	celular = models.CharField(max_length=30, null=True, blank=True)
	correo = models.EmailField(blank=True, null=True)

	def __unicode__(self):
	     return u'%s %s' % (self.dpto, self.ciudad)


    
   


         

User.perfiles = property(lambda u: PerfilesBasico.objects.get_or_create(user=u)[0])
User.contactos = property(lambda u: ContactosBasico.objects.get_or_create(user=u)[0])
User.sociales = property(lambda u: RedesSociales.objects.get_or_create(user=u)[0])
