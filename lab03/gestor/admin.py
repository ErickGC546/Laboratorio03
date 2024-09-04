from django.contrib import admin
from .models import Propietario, Vehiculo, Registro

@admin.register(Propietario)
class PropietarioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'numero_apartamento', 'telefono', 'email')
    search_fields = ('nombre', 'numero_apartamento', 'email')

@admin.register(Vehiculo)
class VehiculoAdmin(admin.ModelAdmin):
    list_display = ('matricula', 'marca', 'modelo', 'color', 'propietario')
    search_fields = ('matricula', 'marca', 'modelo')
    list_filter = ('marca', 'color')

@admin.register(Registro)
class RegistroAdmin(admin.ModelAdmin):
    list_display = ('vehiculo', 'fecha_hora_entrada', 'fecha_hora_salida')
    search_fields = ('vehiculo__matricula',)
    list_filter = ('fecha_hora_entrada', 'fecha_hora_salida')