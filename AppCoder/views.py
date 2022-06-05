from django.http import HttpResponse 
from django.shortcuts import render, HttpResponse
from django.template import loader
from AppCoder.models import Curso, Profesor
from AppCoder.forms import CursoFormulario, ProfesorFormulario


# Create your views here.
def inicio(request):
    return render(request, "AppCoder/inicio.html")
    

def curso(request):
    return render(request, "AppCoder/curso.html")

    
def profesores(request):
    return render(request, "AppCoder/profesores.html")

def estudiantes(request):
    return render(request, "AppCoder/estudiantes.html")

def entregables(request):
    return render(request, "AppCoder/entregables.html")

def cursoFormulario(request):
    if request.method == 'POST':
        miFormulario = CursoFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            nombre= informacion['curso']
            camada= informacion['camada']
            curso = Curso(nombre=nombre, camada=camada)
            curso.save()
        return render(request, "AppCoder/inicio.html")
    else:
        miFormulario = CursoFormulario()        
        
    return render(request, "AppCoder/cursoFormulario.html", {"miFormulario":miFormulario})    

def profesorFormulario(request):
  if request.method == 'POST':
    miFormulario = ProfesorFormulario(request.POST)
    if miFormulario.is_valid():
      informacion = miFormulario.cleaned_data
    nombre = informacion['nombre']
    apellido = informacion['apellido']
    email = informacion['email']
    profesion = informacion['profesion']

    profesor = Profesor(nombre=nombre, apellido=apellido, email=email, profesion=profesion)
    profesor.save()
    return render(request, 'AppCoder/inicio.html')
  else:
    miFormulario = ProfesorFormulario()
  return render(request, 'appCoder/profesorFormulario.html', {'miFormulario':miFormulario})


def busquedaCamada(request):
  return render(request, 'appCoder/busquedaCamada.html')

def buscar(request):
  # respuesta = f"Estoy buscando la comisión {request.GET['camada']}"
  if request.GET['camada']:
    camada = request.GET['camada']
    cursos = Curso.objects.filter(camada=camada)
    return render(request, 'appCoder/resultadosBusqueda.html', {'cursos':cursos, 'camada':camada})
  else:
    respuesta = "No se ha ingresado ninguna comisión"