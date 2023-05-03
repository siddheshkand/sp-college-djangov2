from django.contrib import admin
from todo.models import Todo
# Register your models here.
# admin.site.register(Todo)

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'task',
        'complete'
    ]
    list_editable =  [
        'task',
        'complete'
    ]
