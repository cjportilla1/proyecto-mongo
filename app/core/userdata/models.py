from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField
from .genero import Generos


# Create your models here. 
#crear la estructura de la aplicacion en el  modelo de datos:

class Roles(models.Model):
    RoleName = models.CharField(max_length = 50)
    
    class Meta:
        verbose_name = "Roles de usuario"
        verbose_name_plural = "perfiles"

    
    #creo la funcion para llamar atributo:
    def __str__(self):
        return self.RoleName
    
    
class DatosUser(models.Model):
    userDNI = models.CharField(max_length = 20, verbose_name= "Identificacion")
    NombUser = models.CharField(max_length = 255, null=True, verbose_name= "Nombres")
    ApeUser = models.CharField(max_length = 255, null=True, verbose_name= "Apellidos")
    ProfeUser = models.CharField(max_length = 70, null=True, verbose_name= "Profesion")
    fotoUser = models.ImageField(default='user.png', verbose_name = "Foto de perfil", upload_to="images/perfiles")
    teleUser = models.CharField(max_length = 20, verbose_name= "Numero de Telefono")
    GeneUser = models.CharField(max_length = 20, null=True, choices = Generos, default = "Otro", verbose_name= "Genero")
    creado = models.DateTimeField(auto_now_add = True, null=True, verbose_name= "Creado el")
    modificado = models.DateTimeField(auto_now_add = True, null=True, verbose_name= "Modificado el")
    
    class Meta:
        verbose_name = "Datos del usuario"
        verbose_name_plural = "Informacion"   
         
    def __unicode__(self):
        return self.userDNI

class Habilidades(models.Model):
    NombHabil = models.CharField(max_length = 155, verbose_name= "Competencia")
    DescHabil = models.TextField(verbose_name= "Descripcion de la habilidad" )
    prof = models.CharField(max_length = 200, null= True, verbose_name = "Profesion")
    class Meta:
        verbose_name = "Habilidades de usuario"
        verbose_name_plural = "Competencias"
    
    def __str__(self):
        return self.NombHabil

class DetaRoles(models.Model):
    idRole = models.ForeignKey(Roles, on_delete = models.CASCADE, verbose_name = "Identificador de Rol")
    idUser = models.ForeignKey(DatosUser, on_delete = models.CASCADE)
    addUser = models.DateTimeField(auto_now_add = True, null=True)
    udtUser = models.DateTimeField(auto_now = True)
    estaRol = models.CharField(max_length = 10)
    
    class Meta:
        verbose_name = "Roles de usuario"
        verbose_name_plural = "Roles"
        
    def __unicode__(self):
        return self.idUser

class Rates(models.Model):
    idHabil = models.ForeignKey(Habilidades, on_delete= models.CASCADE) 
    idUser = models.ForeignKey(DatosUser, on_delete = models.CASCADE)   
    porcentaje = models.DecimalField(max_digits = 2, decimal_places = 1)
    udtHabil = models.DateTimeField(auto_now = True)
    
    class Meta:
        verbose_name = "Porcentaje de nivel de habilidad"
        verbose_name_plural = "Niveles de usuario"
    
    def __unicode__(self):
        return self.idUser
    