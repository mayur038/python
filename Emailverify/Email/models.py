from django.db import models
from django.core import mail
from django.db.models import signals

from django.dispatch import receiver
# Create your models here.
class Custom_user(models.Model):
    username = models.TextField(max_length=50,default=None,unique=True)
    Email = models.CharField(max_length=50,primary_key = True)
    phone = models.CharField(max_length=10)
    password = models.CharField(max_length = 20)
    E_varify = models.BooleanField(default=False)
    Key = models.CharField(max_length = 6,default = 000000)



# @receiver(post_save,sender=Custom_user)
# def send_mail_token(sender,instance,created,**kwargs):
#     try:
#         send_mail(n  )
#     except Exception as e:
#         print(e)