from django.urls import path
from AppCoder.views import cursos, estudiantes, profesores, crear_curso

urlpatterns = [
    path('cursos', cursos),
    path('curso/<nombre>/<camda>', crear_curso),
    path('estudiantes', estudiantes),
    path('profesores', profesores ),
]

