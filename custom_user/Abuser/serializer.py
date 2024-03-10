from rest_framework import serializers
from .models import *
from django.contrib.auth import get_user_model
User = get_user_model()
    

class Registerserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
    
    def create(self, validated_data):

        user = User.objects.create(Email=validated_data['Email'],Phone=validated_data['Phone'])
        user.set_password(validated_data['password'])
        user.save()
        return user