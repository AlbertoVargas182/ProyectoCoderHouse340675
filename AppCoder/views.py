from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render, redirect
from AppCoder.forms import CursoForm, BusquedaCursoForm
from AppCoder.models import Curso, Estudiantes, Profesor, Entregable



'''
def guardar_curso(request, camada):
    curso = Curso(nombre="Python", camada=camada)
    curso.save()
    return HttpResponse("Usuario creado exitosamente")
'''
def busqueda_curso(request):
    # Mostrar los datos filtrados
    mi_formulario = BusquedaCursoForm(request.GET)
    if mi_formulario.is_valid():
        informacion = mi_formulario.cleaned_data
        cursos_filtrados = Curso.objects.filter(nombre__icontains=informacion['nombre'])
        context = {
            "cursos": cursos_filtrados,
        }
    
        return render(request, "AppCoder/busqueda_curso.html", context=context)







# Ver los cursos guardados
def cursos(request):

    if request.method == "POST":
        mi_formulario = CursoForm(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            curso_save = Curso(
                nombre=informacion['nombre'],
                camada=informacion['camada']
            )
            curso_save.save()
        


    all_cursos = Curso.objects.all()
    context = {
        "cursos": all_cursos,
        "form": CursoForm(),
        "form_busqueda": BusquedaCursoForm(),
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
