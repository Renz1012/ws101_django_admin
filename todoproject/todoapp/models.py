from django.db import models

# Create your models here.
class Todo(models.Model):
    carmodel = models.CharField(max_length=100)
    price= models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    available = models.BooleanField(default=False)