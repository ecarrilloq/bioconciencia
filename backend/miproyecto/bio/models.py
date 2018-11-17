from django.db import models

# Create your models here.
class Perfil(models.Model):
	Nombre = models.CharField(max_length=200)
	IdEstado = models.BooleanField()
	
class TipoVivienda(models.Model):
	Tipo = models.CharField(max_length=200)
	
class Localidad(models.Model):
	Nombre = models.CharField(max_length=200)
	
class Barrio(models.Model):
	Nombre = models.CharField(max_length=200)
	IdLocalidad = models.ForeignKey(Localidad, on_delete = models.CASCADE) 
	
class Direccion(models.Model):
	Nombre = models.CharField(max_length=200)
	IdBarrio = models.ForeignKey(Barrio, on_delete = models.CASCADE) 
	IdTipoVivienda = models.ForeignKey(TipoVivienda, on_delete = models.CASCADE) 

class Usuario(models.Model):
	UserName = models.CharField(max_length=200)
	Nombre = models.CharField(max_length=200)
	Apellido = models.CharField(max_length=200)
	FechaNacimiento = models.DateTimeField()
	EstadoId = models.BooleanField()
	#IdPerfil = models.ForeignKey(Perfil, on_delete = models.CASCADE)
	#IdDireccion = models.ForeignKey(Direccion, on_delete = models.CASCADE)
	
class Denuncia(models.Model):
	Descripcion = models.CharField(max_length=200)
	Observacion = models.CharField(max_length=200)
	Imagen = models.ImageField()
	EstadoDenuncia = models.IntegerField()
	Georeferencia = models.CharField(max_length=1000, null=True)
	IdUsuario = models.ForeignKey(Usuario, on_delete = models.CASCADE)

class Menu(models.Model):	
	Nombre = models.CharField(max_length=200)
	EstadoId = models.BooleanField()
	
class Loggin(models.Model):	
	FechaIngreso = models.DateTimeField()
	IdUsuario = models.ForeignKey(Usuario, on_delete = models.CASCADE)
	IdMenu = models.ForeignKey(Menu, on_delete = models.CASCADE)
	
class Juego(models.Model):	
	Fecha = models.DateTimeField()
	Puntos = models.IntegerField()
	IdUsuario = models.ForeignKey(Usuario, on_delete = models.CASCADE)
	
	