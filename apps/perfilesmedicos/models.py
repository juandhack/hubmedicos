import os, sys
# -*- encoding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class Pais(models.Model):
    nombre = models.CharField(max_length = 140)
    
    def __unicode__(self):
        return self.nombre

class Dpto(models.Model):
	nombre = models.CharField(max_length = 140)
	
	def __unicode__(self):
		return self.nombre
	
class Ciudad(models.Model):
	nombre = models.CharField(max_length = 140)
	
	def __unicode__(self):
		return self.nombre


class Especialidad(models.Model):
	nombre = models.CharField(max_length = 140)
	
	def __unicode__(self):
		return self.nombre
	    
class CategoriaPR(models.Model):
	nombre = models.CharField(max_length = 140)
	
	def __unicode__(self):
	    return self.nombre
	
class RolMedico(models.Model):
	nombre = models.CharField(max_length = 140)
	
	def __unicode__(self):
	    return self.nombre
        

class ClubMedico(models.Model):

    nombre_club = models.CharField(max_length=100)		
    def __unicode__(self):
		return self.nombre_club  
	
    
class ClubMedicoSubscripcion(models.Model):
    user = models.ForeignKey(User)
    club = models.ForeignKey(ClubMedico)
    rol = models.ForeignKey(RolMedico, null=True, blank=True)
    
    def __unicode__(self):
	    return self.medico


class Perfiles(models.Model):
	user = models.OneToOneField(User)
	dni = models.CharField(max_length=20)
	nombres = models.CharField(max_length=255, null=True, blank=True)
	apellidos = models.CharField(max_length=255, null=True, blank=True)
	acerca_de = models.TextField("Extracto Personal",null=True, blank=True)
	tipo_usuario = models.CharField(max_length=1,null=True,blank=True)
	imagen = models.ImageField("Tu foto",upload_to='pictures',null=True,blank=True)
	def __unicode__(self):
		return self.dni
	
KIND_PAIS = (
   ('Colombia','Colombia'),
)

KIND_ESPECIALIDAD = (
   ('Cardiologia','Cardiología'),
   ('Anestesiologia','Anestesiología'),
   ('Cirugia cardiovascular','Cirugía cardiovascular'),
   ('Dermatologia','Dermatología'),
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

class Contactos(models.Model):

	user = models.OneToOneField(User)
	pais = models.ForeignKey(Pais, null=True, blank=True)
	dpto = models.ForeignKey(Dpto, null=True, blank=True)
	ciudad = models.ForeignKey(Ciudad, null=True, blank=True)
	telefono = models.CharField("Teléfono",max_length=25, null=True, blank=True)
	celular = models.CharField(max_length=30, null=True, blank=True)
	correo = models.EmailField(blank=True, null=True)

	def __unicode__(self):
	     return u'%s %s' % (self.dpto, self.ciudad)



class RedesSociales(models.Model):
	user = models.OneToOneField(User)
	blog = models.CharField(max_length=200, null=True, blank=True)
	twitter = models.CharField(max_length=200, null=True, blank=True)
	facebook = models.CharField(max_length=200, null=True, blank=True)
	linkedin = models.CharField(max_length=200, null=True, blank=True)
	you_tube = models.CharField(max_length=200, null=True, blank=True)
    


class PerfilProfesional(models.Model):
	user = models.ForeignKey(User, null=True, blank=True)
	organizacion = models.CharField("Nombre Entidad",max_length=255, null=True, blank=True)
	especialidad = models.ForeignKey(Especialidad, null=True, blank=True)
	cargo = models.CharField(max_length=255, null=True, blank=True)
	numregistroprof = models.CharField("Registro Profesional",max_length=255, null=True, blank=True)
	funcionesrealizadas = models.TextField("Funciones Realizadas",null=True, blank=True)
	anioinicio = models.DateField("Año Inicio",null=True, blank=True)
	aniofin = models.DateField("Año Finalización",null=True, blank=True)
	class Meta:
		verbose_name = 'Profesional'
		verbose_name_plural = 'Profesional'
		
	def __unicode__(self):
		return self.organizacion
	
        @models.permalink
	def get_absolute_url(self):
		return('listar_info_profesional')


class PerfilAcademico(models.Model):
	user = models.ForeignKey(User, null=True, blank=True)
	institucion = models.CharField("Universidad",max_length=255, null=True, blank=True)
	titulo = models.CharField("Título",max_length=255, null=True, blank=True)
	logros = models.TextField(null=True, blank=True)
	anioinicio = models.DateField("Año Inicio",null=True, blank=True)
	aniofin = models.DateField("Año Finalización",null=True, blank=True)
	
	class Meta:
		verbose_name = 'Academico'
		verbose_name_plural = 'Academico'
		
	def __unicode__(self):
		return self.logros
	
        @models.permalink
	def get_absolute_url(self):
		return('listar_info_academica')
	
class PreguntasRespuestas(models.Model):
	user = models.ForeignKey(User, null=True, blank=True)
	pregunta = models.TextField("Ingresa la pregunta",null=True,blank=True)
	respuesta = models.TextField("Ingresa la respuesta",null=True,blank=True)
	categoria = models.ForeignKey(CategoriaPR, null=True, blank=True)
        
        class Meta:
		verbose_name = 'Pregunta'
		verbose_name_plural = 'Pregunta'
		
	def __unicode__(self):
		return self.pregunta
	
        @models.permalink
	def get_absolute_url(self):
		return('listar_preguntas')
	
        @models.permalink
        def get_delete_url(self):
                return ('eliminar_pregunta', [self.id, ])
      #code

class Servicios(models.Model):
	user = models.ForeignKey(User, null=True, blank=True)
	organizacion = models.CharField("Entidad de Salud",max_length=255, null=True, blank=True)
	especialidad = models.CharField(max_length=255, null=True, blank=True, choices=KIND_ESPECIALIDAD)
	descripcion = models.TextField("Descripción",null=True,blank=True)
	direccion = models.CharField("Dirección",max_length=255, null=True, blank=True)
	pais = models.CharField("País",max_length=30, null=True, blank=True, choices=KIND_PAIS)
	dpto = models.CharField("Departamento",max_length=30, null=True, blank=True, choices=KIND_DPTO)
	telefono = models.CharField("Teléfono",max_length=25, null=True, blank=True)
	celular = models.CharField(max_length=30, null=True, blank=True)
	correo = models.EmailField(blank=True, null=True)
	blog = models.CharField("Sitio Web",max_length=255, null=True, blank=True)
	
	class Meta:
		verbose_name = 'Servicios'
		verbose_name_plural = 'Servicios'
		
	def __unicode__(self):
		return self.organizacion
	
        @models.permalink
	def get_absolute_url(self):
		return('listar_info_servicios')
	
        @models.permalink
        def get_delete_url(self):
                return ('eliminar_info_servicios', [self.id, ])
         

User.perfiles = property(lambda u: Perfiles.objects.get_or_create(user=u)[0])
User.contactos = property(lambda u: Contactos.objects.get_or_create(user=u)[0])
User.sociales = property(lambda u: RedesSociales.objects.get_or_create(user=u)[0])
#User.profesional = property(lambda u: PerfilProfesional.objects.get_or_create(user=u)[0])
#User.academico = property(lambda u: PerfilAcademico.objects.get_or_create(user=u)[0])
#User.consultas = property(lambda u: PreguntasRespuestas.objects.get_or_create(user=u)[0])





