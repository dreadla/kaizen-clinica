from django.shortcuts import render


def inicio(request):
    return render(request, "api_personas/inicio.html")


def pacientes(request):
    return render(request, "api_personas/pacientes.html")


def medicos(request):
    return render(request, "api_personas/medicos.html")


def citas(request):
    return render(request, "api_personas/citas.html")


def tratamientos(request):
    return render(request, "api_personas/tratamientos.html")