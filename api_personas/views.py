from django.shortcuts import render
from .models import Paciente, Medico, Cita


def inicio(request):
    return render(request, "api_personas/inicio.html")


def pacientes(request):
    datos = Paciente.objects.all()
    return render(request, "api_personas/pacientes.html", {"pacientes": datos})


def medicos(request):
    datos = Medico.objects.all()
    return render(request, "api_personas/medicos.html", {"medicos": datos})


def citas(request):
    datos = Cita.objects.all()
    return render(request, "api_personas/citas.html", {"citas": datos})