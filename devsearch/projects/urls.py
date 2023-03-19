from django.urls import path
from . import views


def projects(request):
    return HttpResponse('Hallo Welt')

def project(request, pk):
    return HttpResponse('Einzelprojekt' + ' '+ str(pk))

urlpatterns = [
    path('', views.projects, name='projects'),
    path('project/<str:pk>/', views.project, name='project'),

]