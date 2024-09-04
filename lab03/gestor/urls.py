from django.urls import path
from . import views

urlpatterns = [
    path('registrar-propietario/', views.registrar_propietario, name='registrar_propietario'),
    path('registrar-vehiculo/', views.registrar_vehiculo, name='registrar_vehiculo'),
    path('registrar-ingreso/', views.registrar_ingreso, name='registrar_ingreso'),
    path('lista/', views.lista_propietarios, name='lista_propietarios'),
]