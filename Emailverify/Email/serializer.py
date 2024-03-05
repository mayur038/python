from rest_framework import serializers
from .models import Custom_user


class Registerserializer(serializers.ModelSerializer):
    class Meta:
        model = Custom_user
        fields = ['Phone','Email']
    
    def create(self, validated_data):

        user = Custom_user.objects.create(Username = validated_data['Username'],
                                          Email = validated_data['Email']
                                          ,Phone=validated_data['Phone'],
                                          Password = validated_data['Password'] 
                                          )
                                          
        user.save()
        return user