from django.contrib import admin
from .models import Projects, Technology, skills

@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'link']
    search_fields = ['id', 'name']
    filter_horizontal = ('technologies',)  # ✅ кортеж с запятой
    ordering = ['id']

@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):  # ✅ другое имя
    list_display = ['id', 'name']
    search_fields = ['id', 'name']
    ordering = ['id']

@admin.register(skills)
class SkillsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'level']
    ordering = ['id']