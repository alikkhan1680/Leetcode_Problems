from rest_framework import serializers
from .models import User, Student, Product
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

