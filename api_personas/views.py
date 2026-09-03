from django.shortcuts import render


def inicio(request):
    return render(request, "api_personas/inicio.html")