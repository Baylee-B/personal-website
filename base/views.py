from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm

# Create your views here.

def homePage(request):
    return render(request, 'base/home.html')

def aboutPage(request):
    return render(request, 'base/about.html')

def projectsPage(request):
    projects = Project.objects.all()
    return render(request, 'base/projects.html', {'projects':projects})

def projectPage(request, pk):
    project = Project.objects.get(id=pk)
    return render(request, 'base/project.html', {'project':project})

def contactPage(request):
    return render(request, 'base/contact.html')

def addProject(request):
    form = ProjectForm()

    if request.method == 'POST': 
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {'form':form}
    return render(request, 'base/project_form.html', context)

def editProject(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST': 
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {'form':form}
    return render(request, 'base/project_form.html', context)