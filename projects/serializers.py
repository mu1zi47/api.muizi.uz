from rest_framework import serializers
from .models import Projects, Technology, skills

class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = ['id', 'name']

class ProjectsSerializer(serializers.ModelSerializer):
    technologies = TechnologySerializer(many=True, read_only=True)

    class Meta:
        model = Projects
        fields = '__all__'

class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = skills
        fields = '__all__'
