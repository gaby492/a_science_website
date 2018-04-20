from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=300) #Name of the project
    team_leader = models.CharField(max_length=250) #Leader of the team
    content = models.TextField() #One field for the content of the project


    ##This function will return additional information when looking for data
    def __str__(self):
        return self.name + ' - ' + self.team_leader


class Image(models.Model): #This table will contain the content of the projects
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=400)   #Name or location of the image

