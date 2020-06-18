from django.contrib import admin
#importamos las clases desde los modelos
from .models import Roles, DatosUser, Habilidades, DetaRoles, Rates

# Register your models here.
class RoleModel(admin.ModelAdmin):
    list_display = ["RoleName"]
    class Meta:
        model = Roles
admin.site.register(Roles)

class DatoUserModel(admin.ModelAdmin):
    list_display = ["userDNI"]
    class Meta:
        model = DatosUser
admin.site.register(DatosUser)
    
class HabilidadesModel(admin.ModelAdmin):
    list_display = ["NombHabil"]
    class Meta:
        model = Habilidades
admin.site.register(Habilidades)
    
class DetaRolesModel(admin.ModelAdmin):
    list_display = ["idUser"]
    class Meta:
        model = DetaRoles
admin.site.register(DetaRoles)
    
class RateModel(admin.ModelAdmin):
    list_display = ["idUser"]
    class Meta:
        model = Rates
admin.site.register(Rates)