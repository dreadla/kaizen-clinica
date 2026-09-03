from django.db import models


class Paciente(models.Model):
    rut = models.CharField(max_length=12, unique=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    telefono = models.CharField(max_length=20)
    correo = models.EmailField()

    def __str__(self):
        return self.nombre + " " + self.apellido


class Medico(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    especialidad = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre


class Cita(models.Model):
    paciente = models.ForeignKey(
        Paciente,
        on_delete=models.CASCADE
    )

    medico = models.ForeignKey(
        Medico,
        on_delete=models.CASCADE
    )

    fecha = models.DateField()
    hora = models.TimeField()
    estado = models.CharField(max_length=30)
    motivo = models.TextField()


class Tratamiento(models.Model):
    paciente = models.ForeignKey(
        Paciente,
        on_delete=models.CASCADE
    )

    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()