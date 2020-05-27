from django.contrib import admin
#importamos las clases desde los modelos

from .models import Roles, DatosUser, HabilUser, DetaRoles, Rates


#registro del modelo de roles
class Rolemodel(admin.ModelAdmin):
	list_display=["Rolename"]
	list_display_links=["Rolename"]
	list_filter=["Rolename"]

	class Meta:
		model =Roles
admin.site.register(Roles)


#registro del modelo DatosUser

class DatosUserModel(admin.ModelAdmin):
	list_display=["nomUser"]

	class Meta:
		model=DatosUser
admin.site.register(DatosUser)



#registro del modelo de habilidades de usuario
class HabilUserModel(admin.ModelAdmin):
	list_display=["NombreHabil"]


	class Meta:
		model=HabilUser
admin.site.register(HabilUser)

#registro del modelo de detalles de roles de usuario
class DetaRolesModel(admin.ModelAdmin):
	list_display=["estaRol"]

	class Meta:
		model=DetaRoles
admin.site.register(DetaRoles)


#registro del modelo de rates de usuario 

class RatesModel(admin.ModelAdmin):
	list_display=["pcrHabil"]

	class Meta:
		model=Rates
admin.site.register(Rates)
