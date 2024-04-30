from rest_framework import serializers
from django.conf import settings
from .models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['name', 'profile_picture']
