from django.contrib import admin
from .models import Paciente, Medico, Cita, Tratamiento


@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = (
        'rut',
        'nombre',
        'apellido',
        'telefono',
        'correo'
    )


@admin.register(Medico)
class MedicoAdmin(admin.ModelAdmin):
    list_display = (
        'nombre',
        'apellido',
        'especialidad',
        'telefono'
    )


@admin.register(Cita)
class CitaAdmin(admin.ModelAdmin):
    list_display = (
        'paciente',
        'medico',
        'fecha',
        'hora',
        'estado'
    )


@admin.register(Tratamiento)
class TratamientoAdmin(admin.ModelAdmin):
    list_display = (
        'paciente',
        'fecha_inicio',
        'fecha_fin'
    )