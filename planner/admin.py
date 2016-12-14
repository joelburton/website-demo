from django.contrib import admin

from planner.models import Project, Task


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    """Admin view for project."""

    list_display = ['id', 'title', 'total_hours']
    list_display_links = ['id', 'title']


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    """Admin view for task."""

    list_display = ['id', 'title', 'project', 'hours', 'done']
    list_display_links = ['id', 'title']

    list_filter = ['project', 'done']

    search_fields = ['id', 'title']
