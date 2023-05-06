from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10)
    address = models.TextField()
    aadhar_card = models.CharField(max_length=12)
    college = models.CharField(max_length=100)
    email = models.EmailField()
    profile_picture = models.ImageField()