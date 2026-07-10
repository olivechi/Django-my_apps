from django.contrib import admin
from .models import Task
# Register your models here.
admin.site.register(Task)
class Taskadmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed')
    search_fields = ('title')
    search_filter = ('completed')