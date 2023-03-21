from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import Curso, Estudiantes, Profesor, Entregable


# Create your views here.
'''
def guardar_curso(request, camada):
    curso = Curso(nombre="Python", camada=camada)
    curso.save()
    return HttpResponse("Usuario creado exitosamente")
'''
# Ver los cursos guardados
def cursos(request):
    all_cursos = Curso.objects.all()
    context = {
        "cursos": all_cursos
    }
    return render(request, "AppCoder/cursos.html", context=context)



# Crear un curso, con guardado de datos
def crear_curso(request, nombre, camada):
    save_curso = Curso(nombre=nombre, camada=int(camada))
    save_curso.save()
    context = {
        "nombre": nombre
    }
    return render(request, "AppCoder/save_curso.html", context)




def estudiantes(request):
    return render(request, "base.html")


def profesores(request):
    return render(request, "base.html")
