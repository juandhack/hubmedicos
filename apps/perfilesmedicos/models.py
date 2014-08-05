from django.db import models
from django.contrib.auth.models import User

class Perfiles(models.Model):
	usuario = models.OneToOneField(User)
	dni = models.CharField(max_length=20)
	nombres = models.CharField(max_length=255, null=True, blank=True)
	apellidos = models.CharField(max_length=255, null=True, blank=True)
	acercade = models.TextField(null=True, blank=True)
	tipousuario = models.CharField(max_length=1)
	
	
class Contactos(models.Model):
	usuario = models.OneToOneField(User)
	dpto = models.CharField(max_length=30, null=True, blank=True)
	ciudad = models.CharField(max_length=30, null=True, blank=True)
	telefono = models.CharField(max_length=25, null=True, blank=True)
	celular = models.CharField(max_length=30, null=True, blank=True)
	correo = models.EmailField(blank=True)


class RedesSociales(models.Model):
	usuario = models.OneToOneField(User)
	blog = models.CharField(max_length=255, null=True, blank=True)
	twitter = models.CharField(max_length=20, null=True, blank=True)
	facebook = models.CharField(max_length=30, null=True, blank=True)
	linkedin = models.CharField(max_length=30, null=True, blank=True)
	youtube = models.CharField(max_length=30, null=True, blank=True)
    
   

class PerfilProfesional(models.Model):
	usuario = models.ForeignKey(User)
	organizacion = models.CharField(max_length=255, null=True, blank=True)
	especialidad = models.CharField(max_length=255, null=True, blank=True)
	cargo = models.CharField(max_length=255, null=True, blank=True)
	aniosejercidos = models.CharField(max_length=255, null=True, blank=True)
	numregistroprof = models.CharField(max_length=255, null=True, blank=True)
	funcionesrealizadas = models.TextField(null=True, blank=True)


class PerfilAcademico(models.Model):
	usuario = models.ForeignKey(User)
	institucion = models.CharField(max_length=255, null=True, blank=True)
	titulo = models.CharField(max_length=255, null=True, blank=True)
	logros = models.TextField(null=True, blank=True)

	


