from django.db import models

class Propietario(models.Model):
    nombre = models.CharField(max_length=50)
    numero_apartamento = models.CharField(max_length=3)
    telefono = models.CharField(max_length=9)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.nombre} (Apt. {self.numero_apartamento})"

class Vehiculo(models.Model):
    propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE, related_name='vehiculos')
    matricula = models.CharField(max_length=6, unique=True)
    marca = models.CharField(max_length=25)
    modelo = models.CharField(max_length=25)
    color = models.CharField(max_length=25)

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.matricula})"

class Registro(models.Model):
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE, related_name='registros')
    fecha_hora_entrada = models.DateTimeField(auto_now_add=True)
    fecha_hora_salida = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Registro de {self.vehiculo.matricula} - Entrada: {self.fecha_hora_entrada} - Salida: {self.fecha_hora_salida or 'No registrado'}"
