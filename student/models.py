from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10)
    address = models.TextField()
    aadhar_card = models.CharField(max_length=12)
    college = models.CharField(max_length=100)
    email = models.EmailField()
    profile_picture = models.ImageField(upload_to='student_images')


class MetaFields(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    views = models.IntegerField(default=0)
    class Meta:
        abstract = True

class StudentBlog(MetaFields):
    name = models.CharField(max_length=50)
    description = models.TextField()


class TeacherBlog(MetaFields):
    name = models.CharField(max_length=50)
    description = models.TextField()


class ParentsBlog(MetaFields):
    name = models.CharField(max_length=50)
    description = models.TextField()

