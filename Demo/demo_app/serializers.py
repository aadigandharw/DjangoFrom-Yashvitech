from rest_framework import serializers
from .models import *

class RegisterSerializers(serializers.ModelSerializer):
    class Meta:
        model = Registration 
        fields = '__all__'

class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = StudentLogin 
        fields = '__all__'