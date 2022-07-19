from django.urls import include, path

app_name = "PROJECTS"

from . import views as PROJECTS_VIEWS

urlpatterns = [ path('home/',PROJECTS_VIEWS.home,name='projects_home'),
				path('new_project/',PROJECTS_VIEWS.new_project,name='new_project'),
				path('project_details/<int:pk>/',PROJECTS_VIEWS.project_details,name='project_details'),
				
]
