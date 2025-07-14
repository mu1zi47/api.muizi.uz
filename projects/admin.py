from django.contrib import admin
from .models import Projects

@admin.register(Projects)
class projectsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'link']
    search_fields = ['id', 'name']
    ordering = ['id']