from django.urls import path
from .views import ProjectsViews

urlpatterns = [
    path('projects/', ProjectsViews.as_view(), name='projects-list'),
]