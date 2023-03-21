from django.db import models

# Create your models here.

# Clase curso
class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField(max_length=100)

    def __str__(self):
        return f"Curso: {self.nombre}, Camada: {self.camada}"

# Clase estudiantes
class Estudiantes(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()

# Clase profesor
class Profesor(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    profesion = models.CharField(max_length=40)

    def __str__(self):
        return f"Profesor: {self.nombre} {self.apellido}"

# Clase entregable
class Entregable(models.Model):
    nombre = models.CharField(max_length=40)
    fecha_de_entrega = models.DateField()
    entregado = models.BooleanField()




