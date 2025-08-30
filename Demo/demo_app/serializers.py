from rest_framework import serializers
from .models import *

# class RegisterSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = Registration 
#         fields = '__all__'

# class StudentSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = StudentLogin 
#         fields = '__all__'

# MyUser Model

class MyUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = '__all__'

        extra_kwargs = {
            'password': {'write_only': True}  # password API response me kabhi na dikhaye
        }

    # create method serializer class ke andar likhna hai, Meta ke andar nahi
   
        
    def create(self, validated_data):
      user = MyUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', '')     
      )
      return user

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)

        password = validated_data.get('password', None)
        if password:
            instance.set_password(password)  # password ko hash karna zaruri hai
        instance.save()
        return instance
