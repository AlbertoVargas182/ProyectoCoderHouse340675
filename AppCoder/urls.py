from django.urls import path
from AppCoder.views import cursos, estudiantes, profesores, crear_curso

urlpatterns = [
    path('cursos', cursos, name="AppCoderCursos"),
    path('buscar_curso', busqueda_curso, name="AppCoderBuscarCurso"),
    path('curso/<nombre>/<camda>', crear_curso, name="AppCoderCurso"),
    path('estudiantes', estudiantes, name="AppCoderEstudiantes"),
    path('profesores', profesores, name="AppCoderProfesores"),
]

