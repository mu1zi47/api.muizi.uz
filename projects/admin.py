from django.contrib import admin
from .models import Projects, Technology, skills
from modeltranslation.admin import TranslationAdmin


@admin.register(Projects)
class ProjectsAdmin(TranslationAdmin):
    list_display = ['id', 'name', 'link']
    search_fields = ['id', 'name']
    filter_horizontal = ('technologies',)  # ✅ кортеж с запятой
    ordering = ['id']

@admin.register(Technology)
class TechnologyAdmin(TranslationAdmin):  # ✅ другое имя
    list_display = ['id', 'name']
    search_fields = ['id', 'name']
    ordering = ['id']

@admin.register(skills)
class SkillsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'level', 'link']
    ordering = ['id']