from rest_framework import serializers
from .models import *
from django.contrib.auth import get_user_model
User = get_user_model()


class Registerserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['phone','password']
    
    def create(self, validated_data):

        user = User.objects.create(phone=validated_data['phone'])
        user.set_password(validated_data['password'])
        user.save()
        return user

class subjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = subjects
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    subject = subjectSerializer()
    class Meta:
        model = Student
        fields = '__all__'
        # depth = 1

    def validate(self, data):
        if data['marks'] < 22:
            raise serializers.ValidationError({'error':'qwewq'})
        
        return data