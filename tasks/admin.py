from django.contrib import admin
from tasks.models import *

# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'deadline', 'status']
    list_display_links = ['title']
    list_editable = ['deadline', 'status']
    list_filter = ['status']
