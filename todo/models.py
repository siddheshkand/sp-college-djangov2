from django.db import models

# Create your models here.
class Todo(models.Model):
    # date time
    # task (description)
    # priority
    # complete 
    task = models.CharField(max_length=255)
    complete = models.BooleanField(default=False)
