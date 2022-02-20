from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homePage, name="home"),
    path('about/', views.aboutPage, name="about"),
    path('projects', views.projectsPage, name="projects"),
    path('project/<str:pk>/', views.projectPage, name="project"),
    path('contact/', views.contactPage, name="contact"),
    path('add-project/', views.addProject, name="add-project"),
    path('editProject/<str:pk>/', views.editProject, name="edit-project"),
]