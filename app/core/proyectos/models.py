from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField

#importar modelos de otras apps
from userdata.models import DatosUser
# Create your models here.

class TipoDocu(models.Model):
	nomTiDo = models.CharField(max_length=50, verbose_name="Tipo de documento")
