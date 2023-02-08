from django.db import models

# Create your models here.

class Student(models.Model):
    roll = models.IntegerField()
    name = models.CharField(max_length=30)
    marks = models.FloatField()
    mail = models.EmailField()
    phone = models.CharField(max_length=10)
