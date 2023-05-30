from django.contrib import admin
from student.models import Student,StudentBlog
# Register your models here.
admin.site.register(Student)
# admin.site.register(StudentBlog)



@admin.register(StudentBlog)
class StudentBlogAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'description',
        'created_at',
        'updated_at',
    ]
