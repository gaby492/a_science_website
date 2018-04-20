from django.shortcuts import render
from django.http import HttpResponse
from .models import Project


# Create your views here.

def index(request):
    all_projects = Project.objects.all() #Stores the result of the db call
    context = {'all_projects': all_projects} #Information tha the template needs
    return render(request, 'project/index.html', context) #The HttpResponse is built in this render


def detail(request, project_id):
    return HttpResponse("<h2> Details for project id: " + str(project_id) + "</h2>")


