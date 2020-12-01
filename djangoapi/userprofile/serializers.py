from .models import UserProfile
from rest_framework import serializers

class UserProfileInputSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'firstName','lastName', 'password', 'email', 'token', 'coins', 'rank']

class UserProfileOutputSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'firstName','lastName', 'email', 'token', 'coins', 'rank']