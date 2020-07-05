from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.core import exceptions
import django.contrib.auth.password_validation as validators

from .models import Dog, Club, User, Show, \
    Registration, Ring, Perform, Grade


User = get_user_model()


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'last_name')
        extra_kwargs = {'password': {'write_only': True}}

    def validate_password(self, password):
        errors = {}

        try:
            validators.validate_password(password=password)
        except exceptions.ValidationError as e:
            errors['messages'] = list(e.messages)

        if errors:
            raise serializers.ValidationError(errors)

        return password

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


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
        fields = ("id", "username", "first_name", "last_name", "phone_num", "town")


class ShowListSerializer(serializers.ModelSerializer):
    allowed_dogs = serializers.ListField(
        child=serializers.IntegerField(),
        required=False,
    )

    class Meta:
        model = Show
        fields = ("id", "show_name", "show_town", "type", "start_date", "end_date", "allowed_dogs")

    def __init__(self, *args, **kwargs):
        self._allowed_dogs_by_show = kwargs.pop('allowed_dogs_by_show', None)

        super(ShowListSerializer, self).__init__(*args, **kwargs)

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        allowed_dogs = self._allowed_dogs_by_show.get(ret['id'], None)

        if allowed_dogs is not None:
            ret['allowed_dogs'] = allowed_dogs

        return ret

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
    dog = serializers.SerializerMethodField()
    dog_id = serializers.SerializerMethodField()

    def get_dog_id(self, obj):
        return obj.perform.dog.id

    def get_dog(self, obj):
        return obj.perform.dog.dog_name

    class Meta:
        model = Grade
        fields = ("expert", "perform", "points1", "points2", "points3", "dog", "dog_id")

