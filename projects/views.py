from rest_framework import generics
from .models import Projects, skills
from .serializers import ProjectsSerializer, SkillsSerializer

class ProjectsViews(generics.ListAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer

class SkillsViews(generics.ListAPIView):
    queryset = skills.objects.all()
    serializer_class = SkillsSerializer