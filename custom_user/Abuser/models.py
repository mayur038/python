from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager
from django.db.models.signals  import post_save
from django.core.mail.backends.smtp import EmailBackend
from django.dispatch import receiver
from uuid import uuid4
from django.conf import settings
from django.contrib.auth import get_user_model
User = get_user_model()
class cuser(AbstractUser):
    username = None
    Phone = models.CharField(max_length=11, unique=True, default='null')
    user_profile = models.ImageField(upload_to="profile", default='null')
    verified = models.BooleanField(default=False)    
   
    Email = models.EmailField(unique=True,default=None)

    USERNAME_FIELD = 'Phone'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.Phone



@receiver(post_save,sender= User)
def send_mail(sender,instance,created,**kwargs):
    if created:
        try:
            subject = 'subject one'
            id = uuid4()
            message = "Hi click on message <a href='http://127.0.0.1:8000/{id}/'>{id}</a>"
            Email_from = settings.EMAIL_HOST_USER
            r_list = [instance.Email]
            send_mail(subject,message,Email_from,r_list)
        except Exception as e:
            print(e)