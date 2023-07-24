from django.db import models

# Create your models here.
class Todo(models.Model):
    task= models.TextField(max_length=1000)
    
    def __str__(self):
        return str(self.task)
