from django.urls import path

from . import views

urlpatterns = [
    # /project
    path('', views.index, name='index'),


    # /project/71
    path('<int:project_id>', views.detail, name='detail'),

]