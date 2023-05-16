from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
    username=models.CharField(max_length=100)
    address=models. TextField()
    profile_pic=models.ImageField()
    
