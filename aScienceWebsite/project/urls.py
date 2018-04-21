from django.urls import path
from . import views

app_name = 'project'

urlpatterns = [
    # /project
    path('', views.index, name='index'),


    # /project/<project_id>/
    path('<int:project_id>', views.detail, name='detail'),

    # /project/<project_id>/favorite
    #path('<int:project_id>/favorite', views.favorite, name='favorite'),

]