from django.contrib.auth import get_user_model
from rest_framework import serializers
# from ..models.user import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'password')
