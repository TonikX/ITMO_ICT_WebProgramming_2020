from rest_framework import serializers
from alpinism.models import *


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('id', 'country_name')


class ClubSerializer(serializers.ModelSerializer):
    country = CountrySerializer()

    class Meta:
        model = Club
        fields = ('id', 'club_name', 'country', 'city', 'contact_person', 'email', 'telephone')


class ClubPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = ('id', 'club_name', 'country', 'city', 'contact_person', 'email', 'telephone')


class MountainSerializer(serializers.ModelSerializer):
    country = CountrySerializer()

    class Meta:
        model = Mountain
        fields = ('id', 'mountain_name', 'country', 'region', 'height')


class MountainPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mountain
        fields = ('id', 'mountain_name', 'country', 'region', 'height')


class AlpinistSerializer(serializers.ModelSerializer):
    club_name = ClubPostSerializer()

    class Meta:
        model = Alpinist
        fields = ('id', 'name', 'birth_date', 'club_name', 'telephone', 'email', 'address')


class AlpinistPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alpinist
        fields = ('id', 'name', 'birth_date', 'club_name', 'telephone', 'email', 'address')


class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alpinist
        fields = ('id', 'name')


class GroupSerializer(serializers.ModelSerializer):
    participant = ParticipantSerializer(many=True)

    class Meta:
        model = Group
        fields = ('id', 'group_code', 'participant', 'contact_person', 'email', 'telephone', 'group_success')


class GroupPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'group_code', 'participant', 'contact_person', 'email', 'telephone', 'group_success')


class IndSuccessSerializer(serializers.ModelSerializer):
    group = GroupPostSerializer()
    participant = AlpinistPostSerializer()

    class Meta:
        model = IndSuccess
        fields = ('id', 'group', 'participant', 'individual_success')


class IndSuccessPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndSuccess
        fields = ('id', 'group', 'participant', 'individual_success')


class AscentSerializer(serializers.ModelSerializer):
    group = GroupPostSerializer()
    mountain = MountainPostSerializer()

    class Meta:
        model = Ascent
        fields = ('id', 'ascent_code', 'group', 'mountain', 'duration',
                  'complexity', 'ascent_height', 'start_date', 'end_date')


class AscentPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ascent
        fields = ('id', 'ascent_code', 'group', 'mountain', 'duration',
                  'complexity', 'ascent_height', 'start_date', 'end_date')


class EmergencySerializer(serializers.ModelSerializer):
    participant = AlpinistPostSerializer()
    ascent = AscentPostSerializer()

    class Meta:
        model = Emergency
        fields = ('id', 'participant', 'ascent', 'date', 'situation', 'commentary')


class EmergencyPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emergency
        fields = ('id', 'participant', 'ascent', 'date', 'situation', 'commentary')

