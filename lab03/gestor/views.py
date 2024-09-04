from django.shortcuts import render, redirect
from .models import Propietario, Vehiculo, Registro
from .forms import PropietarioForm, VehiculoForm, RegistroForm

def lista_propietarios(request):
    propietarios = Propietario.objects.prefetch_related(
        'vehiculos__registros'
    )
    return render(request, 'lista_propietarios.html', {'propietarios': propietarios})

def registrar_propietario(request):
    if request.method == 'POST':
        form = PropietarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_propietarios')
    else:
        form = PropietarioForm()
    return render(request, 'registrar_propietario.html', {'form': form})

def registrar_vehiculo(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_vehiculos')
    else:
        form = VehiculoForm()
    return render(request, 'registrar_vehiculo.html', {'form': form})

def registrar_ingreso(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_registros')
    else:
        form = RegistroForm()
    return render(request, 'registrar_ingreso.html', {'form': form})
