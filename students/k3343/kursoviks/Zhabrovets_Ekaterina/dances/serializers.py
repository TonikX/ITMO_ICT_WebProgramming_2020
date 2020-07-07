from rest_framework import serializers
from .models import *
import datetime

class WorkshopAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workshop
        fields = ('id', 'name', 'place', 'date', 'time', 'duration', 'price', 'info')


class StyleSerializer(serializers.ModelSerializer):
    class Meta:
        model = DanceStyle
        fields = '__all__'


class ChoreographersSerializer(serializers.ModelSerializer):
    style = StyleSerializer()

    class Meta:
        model = User
        fields = ('id', 'full_name', 'style')


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class HallSerializer(serializers.ModelSerializer):
    school = LocationSerializer()

    class Meta:
        model = Hall
        fields = ('id', 'name', 'cost', 'capacity', 'school')


class ParticipantsSerializer(serializers.ModelSerializer):
    style = StyleSerializer()

    class Meta:
        model = User
        fields = ('id', 'full_name', 'style', 'email', 'telephone', 'birth_date', 'country', 'is_teacher', 'is_superuser', 'biography')

class ParticipantUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('full_name', 'email', 'telephone', 'country', 'biography')

class ParticipantUpdateNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('full_name')

class WorkshopSerializer(serializers.ModelSerializer):
    participants = ParticipantsSerializer(many=True)
    place = HallSerializer()
    choreographer = ChoreographersSerializer(many=True)

    class Meta:
        model = Workshop
        fields = ('id', 'name', 'place', 'date', 'time', 'duration', 'price', 'participants', 'choreographer')


class QuerySerializer(serializers.ModelSerializer):
    user = ParticipantsSerializer()
    workshop = WorkshopSerializer()

    class Meta:
        model = QueryForParticipance
        fields = ('id', 'user', 'workshop', 'approved')

class FeedbackSerializer(serializers.ModelSerializer):
    user = ParticipantsSerializer()
    workshop = WorkshopSerializer()

    class Meta:
        model = Feedback
        fields = ('user', 'workshop', 'created', 'rating', 'text')

class QueriesAll(serializers.BaseSerializer):
    def to_representation(self, instance):
        choreographers = [list(c.values())[0] for c in instance.workshop.choreographer.values('full_name')]
        return {
            'id_query': instance.id,
            'full_name': instance.user.full_name,
            'workshop_name': instance.workshop.name,
            'workshop_date': instance.workshop.date,
            'workshop_price': instance.workshop.price,
            'workshop_style': instance.workshop.choreographer.all()[0].style.name,
            'workshop_sсhool': instance.workshop.place.school.name,
            'workshop_choreographers': choreographers
        }

class RatingSerializer(serializers.BaseSerializer):
    def to_representation(self, instance):
        today = str(datetime.date.today())
        wsh_count = Workshop.objects.filter(participants=instance, date__lt=today).count()
        return {
            'id': instance.id,
            'full_name': instance.full_name,
            'wsh_count': wsh_count
        }