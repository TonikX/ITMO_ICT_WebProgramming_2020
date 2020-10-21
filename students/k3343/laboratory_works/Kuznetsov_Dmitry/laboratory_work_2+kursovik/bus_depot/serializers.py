from rest_framework import serializers
from .models import BusType, Bus, Driver, Route, Schedule, Journal


class BusCreateSerializer(serializers.ModelSerializer):
    """Сериализатор для создания новой записи в модели Автобус"""

    class Meta:
        model = Bus
        fields = "__all__"


class BusTypeSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Тип автобуса"""
    buses = BusCreateSerializer(many=True)

    class Meta:
        model = BusType
        fields = "__all__"


class BusSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Автобус"""
    bus_type = BusTypeSerializer(many=False)

    class Meta:
        model = Bus
        fields = "__all__"


class DriverSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Водитель"""

    class Meta:
        model = Driver
        fields = "__all__"


class RouteSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Маршрут"""

    class Meta:
        model = Route
        fields = "__all__"


class ScheduleSerializer(serializers.ModelSerializer):
    """Сериализатор для модели График работы"""
    driver = serializers.SlugRelatedField(slug_field='fio', read_only=True)
    bus = serializers.SlugRelatedField(slug_field='number', read_only=True)
    route = RouteSerializer(many=False)

    class Meta:
        model = Schedule
        fields = "__all__"


class ScheduleCreateSerializer(serializers.ModelSerializer):
    """Сериализатор для создания новой записи в модели График работы"""

    class Meta:
        model = Schedule
        fields = "__all__"


class JournalSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Журнал"""
    schedule = ScheduleSerializer(many=False)

    class Meta:
        model = Journal
        fields = "__all__"


class JournalCreateSerializer(serializers.ModelSerializer):
    """Сериализатор для создания новой записи в модели Журнал"""

    class Meta:
        model = Journal
        fields = "__all__"
