from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self , Phone,password=None,**extra_fields):
        if not Phone:
            raise ValueError("Phone number Required")

        # extra_fields['Email'] = self.normalize_email(extra_fields['Email'])
        user = self.model(Phone = Phone,**extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user
    def create_superuser(self, Phone, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        
        return self.create_user(Phone = Phone, password=password, **extra_fields)
