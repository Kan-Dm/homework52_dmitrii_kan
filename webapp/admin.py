from django.contrib import admin
from webapp.models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'status', 'due_date']
    list_display_links = ['id', 'description']
    list_filter = ['status']
    search_fields = ['description', 'status']
    fields = ['description', 'status', 'due_date']
    readonly_fields = ['due_date']
