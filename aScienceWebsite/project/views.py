from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Project, Image


# Create your views here.

def index(request):
    all_projects = Project.objects.all() #Stores the result of the db call
    context = {'all_projects': all_projects} #Information tha the template needs
    return  render(request, 'project/index.html', context) #The HttpResponse is built in this render


def detail(request, project_id):
    #project = Project.objects.get(pk=project_id)
    project = get_object_or_404(Project, pk=project_id)
    return render(request, 'project/detail.html', {'project': project})

def favorite(request, project_id):
    #project = Project.objects.get(pk=project_id)
    project = get_object_or_404(Project, pk=project_id)
    return render(request, 'project/detail.html', {'project': project})


