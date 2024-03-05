from django.db import models


class subjects(models.Model):
    subject=models.CharField(max_length=50,default='null')

# Create your models here.
class Student(models.Model):
    subject=models.ForeignKey(subjects,on_delete=models.CASCADE)
    name=models.CharField(max_length=100,default='null')
    marks=models.FloatField(default=0)
   
