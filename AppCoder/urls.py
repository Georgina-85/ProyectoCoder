from django.urls import path
from AppWeb.views import profesores, curso, inicio, entregables, estudiantes, buscar, busquedaCamada 
#from AppWeb.views import cursoFormulario, profesorFormulario
from AppWeb import views


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('curso/', views.curso, name='curso'),
    path('profesores/', views.profesores, name='profesores'),
    path('estudiantes/', views.estudiantes, name='estudiantes'),
    path('entregables/', views.entregables, name='entregables'),
    #path('cursoFormulario/', views.cursoFormulario, name='cursoFormulario'),
    #path('profesorFormulario/', profesorFormulario, name='profesorFormulario'),
    path('busquedaCamada/', busquedaCamada, name='busquedaCamada'),
    path('buscar/', buscar, name='buscar'),
] 


