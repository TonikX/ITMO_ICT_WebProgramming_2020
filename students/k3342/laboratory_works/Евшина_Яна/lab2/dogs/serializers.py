from rest_framework import serializers

from .models import Dog, Club, User, Show, \
    Registration, Ring, Perform, Grade


class DogListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dog
        fields = "__all__"


class ClubListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = "__all__"


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "phone_num", "town")


class ShowListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Show
        fields = "__all__"


class RegistrationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = "__all__"


class RingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ring
        fields = "__all__"


class PerformListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perform
        fields = "__all__"


class GradeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = "__all__"

