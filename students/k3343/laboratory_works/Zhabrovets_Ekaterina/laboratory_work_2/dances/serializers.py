from rest_framework import serializers
from .models import *


class ParticipantsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = '__all__'


class ChoreographersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choreographer
        fields = '__all__'


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class HallSerializer(serializers.ModelSerializer):
    school = LocationSerializer()

    class Meta:
        model = Hall
        fields = ('id', 'name', 'cost', 'capacity', 'school')


class WorkshopSerializer(serializers.ModelSerializer):
    participants = ParticipantsSerializer(many=True)
    place = HallSerializer()
    choreographer = ChoreographersSerializer(many=True)

    class Meta:
        model = Workshop
        fields = ('id', 'name', 'place', 'date', 'time', 'duration', 'participants', 'choreographer')


class WorkshopAddSerializer(serializers.ModelSerializer):

    class Meta:
        model = Workshop
        fields = ('id', 'name', 'place', 'date', 'time', 'duration', 'info')