from django.db import models

# Create your models here.
class Features(models.Model):
    name=models.CharField(max_length=100,default='null name')
    detail=models.CharField(max_length=200,default='null details')