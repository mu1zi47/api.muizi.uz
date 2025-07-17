from django.contrib import admin
from .models import Message

@admin.register(Message)
class messageAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'telegramUser']
    search_fields = ['name', 'telegramUser']
    ordering = ['id']