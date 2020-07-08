from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ClubOwnerSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClubOwner
        fields = '__all__'


class ClubSerializer(serializers.ModelSerializer):
    owner = ClubOwnerSerializer(read_only=True)

    class Meta:
        model = Club
        fields = '__all__'


class NewClimberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Climber
        fields = '__all__'


class ClimberSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Climber
        fields = '__all__'


class AddClimberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Climber
        fields = '__all__'


class MountainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mountain
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class ClimbingSerializer(serializers.ModelSerializer):
    climber = ClimberSerializer(read_only=True)
    group = GroupSerializer(read_only=True)
    mountain = MountainSerializer(read_only=True)

    class Meta:
        model = Climbing
        fields = '__all__'
