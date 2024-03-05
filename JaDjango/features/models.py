from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class ExportCSV(models.Model):
    ExportFile=models.FileField(upload_to="excel",default='null')

# class cuser(AbstractUser):
#     username = models.CharField(max_length=200,unique = True)
#     Phone = models.CharField(max_length=11,unique= True)
#     Email = models.EmailField()
#     user_profile= models.ImageField(upload_to="profile")

#     USERNAME_FIELD = 'Phone'
#     REQUIRED_FIELDS = []