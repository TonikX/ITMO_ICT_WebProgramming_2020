from rest_framework import serializers
from .models import Driver, Order, Client, Storage


class DriverListSerializer(serializers.ModelSerializer):
    """Список водителей"""

    class Meta:
        model = Driver
        fields = ("id", "name", "age", "image")


class DriverDetailSerializer(serializers.ModelSerializer):
    """Подробная информация о водителе"""

    class Meta:
        model = Driver
        fields = "__all__"


class OrderCreateSerializer(serializers.ModelSerializer):
    """Добавление заказа"""
    class Meta:
        model = Order
        fields = "__all__"


class OrderDetailSerializer(serializers.ModelSerializer):
    """Информация о заказе"""

    category = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)
    driver = serializers.SlugRelatedField(slug_field="name", read_only=True)
    client = serializers.SlugRelatedField(slug_field="name", read_only=True)
    data = serializers.DateField(format="%Y-%m-%d")

    class Meta:
        model = Order
        fields = "__all__"


class YoungClientSerializer(serializers.ModelSerializer):
    """Клиенты моложе 40 """

    class Meta:
        model = Client
        fields = ("name", "age")


class DriverOrderSerializer(serializers.ModelSerializer):
    """Заказы водителей"""

    category = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)
    driver = serializers.SlugRelatedField(slug_field="name", read_only=True)
    client = serializers.SlugRelatedField(slug_field="name", read_only=True)
    data = serializers.DateField(format="%Y-%m-%d")

    class Meta:
        model = Order
        fields = "__all__"


class WeekOrderSerializer(serializers.Serializer):
    """Заказы в каждый день недели"""
    percent = serializers.IntegerField()
    week_day = serializers.IntegerField(source='data__week_day')

    class Meta:
        model = Order
        fields = ("week_day", "percent")


class TopCategorySerializer(serializers.Serializer):
    """Топ 3 категории сдаваемого мусора"""
    amount = serializers.IntegerField()
    category = serializers.CharField(source='category__name')

    class Meta:
        model = Order
        fields = ("amount", "category")


class StorageSerializer(serializers.Serializer):
    amount = serializers.IntegerField()
    category = serializers.CharField(source='order__category')

    class Meta:
        model = Storage
        fields = ("amount", "category")


class TotalTrashSerializer(serializers.Serializer):
    """Отчет за месяц"""
    total_to_fabric = serializers.IntegerField()
    total_from_client = serializers.IntegerField()
    total_client = serializers.IntegerField()
    total_money = serializers.IntegerField()

    class Meta:
        fields = ("total_to_fabric", "total_from_client", "total_client", "total_money")


class StorageCreateOrderSerializer(serializers.ModelSerializer):
    """Добавление заказа на склад"""

    class Meta:
        model = Storage
        fields = '__all__'
