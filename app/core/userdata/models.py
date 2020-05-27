from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField
from .generos import Generos

# Create your models here.



#modelo de la tabla roles:
class Roles(models.Model):
	RoleName = models.CharField(max_length = 50)


#poner nombres meta a cada clase
	class Meta:
		verbose_name:"perfil de usuario"
		verbose_name_plural="perfiles"


	#se crea la funcion para llamar atributos
	def _str_(self):
		return self.RoleName


	#crear los demas modelos para la aplicacion datos user:
	#modelo de la tabla DatosUser
class DatosUser(models.Model):
	userDNI = models.CharField(max_length=20 , verbose_name="Numero Id")
	fotoUser = models.ImageField(default='user.png' , verbose_name="Foto de perfil",upload_to='img/perfiles')
	teleUser = models.CharField(max_length=20 , verbose_name="Telefono")
	nombUser = models.CharField(max_length=256 , null=True , verbose_name="Nombres")
	apelUser = models.CharField(max_length=256 , null=True,verbose_name="Apellidos")
	profUser= models.CharField(max_length=100 , null=True,verbose_name="Profesion")
	geneUser = models.CharField(max_length=20 , choices=Generos , default="Otro" , verbose_name="Genero")
	adddata = models.DateTimeField(auto_now_add = True , null=True)
	modifyat = models.DateTimeField(auto_now_add = True , null=True)



#nombres meta a cada clase
	class Meta:
		verbose_name:"Datos de usuario"
		verbose_name_plural:"Informacion"

	#funcion de seleccion:
	def _str_(self):
		return self.userDNI


#modelo de la tabla habilidades:
class HabilUser(models.Model):
	NombHabil = models.CharField(max_length = 100,verbose_name="Habilidad")
	DescHabil = models.TextField(max_length = 2000,verbose_name="Descripcion de la habilidad")

#nombres meta de la clase
	class Meta:
		verbose_name:"Habilidades de usuario"
		verbose_name_plural:"Competencias"

	#funcion de la seleccion
	def _str_(self):
		return self.NombHabil


#agregamos los modelos de detalle:
class DetaRoles(models.Model):
	idRole=models.ForeignKey(Roles, on_delete = models.CASCADE,verbose_name="identificador de rol")
	idUser=models.ForeignKey(DatosUser,on_delete=models.CASCADE)
	addUser=models.DateTimeField(auto_now_add=True,auto_now=False)
	udtuser=models.CharField(max_length=10)

	#nombres meta de la clase
	class Meta:
		verbose_name:"Roles de usuario"
		verbose_name_plural:"Roles"

#funcion de mostrar
def _str_(self):
	return self.idUser


#tabla Rates:
class Rates(models.Model):
	idHabil=models.ForeignKey(HabilUser,on_delete=models.CASCADE)
	idUser = models.ForeignKey(DatosUser, on_delete = models.CASCADE)
	pcrHabil=models.DecimalField(max_digits=2,decimal_places=1) #99,9
	udtHabil=models.DateTimeField(auto_now=True)


	#nombres meta de la clase
	class Meta:
		verbose_name:"Nivel de habilidad"
		verbose_name_plural:"Niveles de usuario"


	#funcion para evocar:

def _str_(self):
	return self.idUser