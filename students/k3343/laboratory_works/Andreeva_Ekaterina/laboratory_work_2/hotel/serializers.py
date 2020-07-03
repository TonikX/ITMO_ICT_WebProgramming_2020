from rest_framework import serializers
from .models import Floor, RoomType, Room, Resident, Servant, Cleaning


class RoomTypeSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Тип Комнаты"""

    class Meta:
        model = RoomType
        fields = "__all__"


class RoomSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Комната"""
    room_type = serializers.SlugRelatedField(slug_field="room_type", read_only=True)
    floor = serializers.SlugRelatedField(slug_field="floor_number", read_only=True)

    class Meta:
        model = Room
        fields = "__all__"


class FloorSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Этаж"""
    rooms = RoomSerializer(many=True)

    class Meta:
        model = Floor
        fields = "__all__"


class ResidentSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Проживающий"""
    room = serializers.SlugRelatedField(slug_field="room_number", read_only=True)

    class Meta:
        model = Resident
        fields = "__all__"


class ResidentCreateSerializer(serializers.ModelSerializer):
    """Сериализатор для создания новой записи в модели Проживающий"""
    class Meta:
        model = Resident
        fields = "__all__"


class ServantSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Служащий"""

    class Meta:
        model = Servant
        fields = "__all__"


class CleaningSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Уборка"""
    floor = serializers.SlugRelatedField(slug_field="floor_number", read_only=True)
    servant = serializers.SlugRelatedField(slug_field="fio", read_only=True)

    class Meta:
        model = Cleaning
        fields = "__all__"


class CleaningCreateSerializer(serializers.ModelSerializer):
    """Сериализатор для создания новой записи в модели Уборка"""
    class Meta:
        model = Cleaning
        fields = "__all__"