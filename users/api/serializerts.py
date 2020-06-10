from rest_framework import serializers

from users.models import User


class QuestMakerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        return User.objects.create_quest_maker(
            username=validated_data['username'],
            password=validated_data['password']
        )


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'is_quest_maker']
        read_only_fields = ['username', 'password']

    def create(self, validated_data):
        return User.objects.create_team()
