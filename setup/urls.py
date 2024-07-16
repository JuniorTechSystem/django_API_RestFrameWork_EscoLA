from django.contrib import admin
from django.urls import path, include
from escola.views import AlunosViewSet, CursoViewSet, MatriculaViewSet, ListaMatriculasAluno, ListaAlunosMatriculados
from rest_framework import routers

router = routers.DefaultRouter()
router.register('alunos', AlunosViewSet, basename='Alunos')
router.register('cursos', CursoViewSet, basename='Cursos')
router.register('matriculas', MatriculaViewSet, basename='Matriculas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls) ),
    path('aluno/<int:pk>/matriculas/', ListaMatriculasAluno.as_view()  ),
    path('curso/<int:pk>/matriculas/', ListaAlunosMatriculados.as_view())

]
