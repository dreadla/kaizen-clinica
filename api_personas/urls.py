from django.urls import path
from . import views


urlpatterns = [

    path('', views.inicio, name="inicio"),

    path('pacientes/', views.pacientes, name="pacientes"),

    path('medicos/', views.medicos, name="medicos"),

    path('citas/', views.citas, name="citas"),

]