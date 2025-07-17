from django.urls import path
from .views import ProjectsViews, SkillsViews

urlpatterns = [
    path('projects/', ProjectsViews.as_view(), name='projects-list'),
    path('skills/', SkillsViews.as_view(), name='skills-list'),
]