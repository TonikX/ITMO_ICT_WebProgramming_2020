from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class HumanSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Human
        fields = '__all__'


class NewHumanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Human
        fields = '__all__'


class DogsSerializer(serializers.ModelSerializer):
    dog_owner = HumanSerializer(read_only=True)

    class Meta:
        model = Dogs
        fields = '__all__'


class NewDogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dogs
        fields = '__all__'


class FundersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funders
        fields = '__all__'


class ExpertsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experts
        fields = '__all__'


class RingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rings
        fields = '__all__'


class ShowsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shows
        fields = '__all__'


class RecordsSerializer(serializers.ModelSerializer):
    record_show = ShowsSerializer(read_only=True)
    record_dog = DogsSerializer(read_only=True)

    class Meta:
        model = Records
        fields = '__all__'


class NewRecordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Records
        fields = ['record_show', 'record_dog']


class ActsSerializer(serializers.ModelSerializer):
    act_show = ShowsSerializer(read_only=True)
    act_dog = DogsSerializer(read_only=True)
    act_ring = RingsSerializer(read_only=True)

    class Meta:
        model = Acts
        fields = '__all__'


class NewActsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Acts
        fields = '__all__'


class SponsorsSerializer(serializers.ModelSerializer):
    sponsor_funder = FundersSerializer(read_only=True)
    sponsor_show = ShowsSerializer(read_only=True)

    class Meta:
        model = Sponsors
        fields = '__all__'


class NewSponsorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsors
        fields = '__all__'


class JudgingsSerializer(serializers.ModelSerializer):
    judging_show = ShowsSerializer(read_only=True)
    judging_expert = ExpertsSerializer(read_only=True)
    judging_ring = RingsSerializer(read_only=True)

    class Meta:
        model = Judgings
        fields = '__all__'


class NewJudgingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Judgings
        fields = ['judging_show', 'judging_expert', 'judging_ring']
