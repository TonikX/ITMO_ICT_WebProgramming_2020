from rest_framework import serializers

from .models import *

class DoctorsSerializer(serializers.ModelSerializer):
    "Список докторов"

    class Meta:
        model = Doctor
        fields = "__all__"


class TransactionListSerializer(serializers.ModelSerializer):
    "Список транзакций"

    patients = serializers.SlugRelatedField(slug_field="surname", read_only=True)
    doctor = serializers.SlugRelatedField(slug_field="surname", read_only=True)

    class Meta:
        model = Transactions
        fields = "__all__"


class TransactionCreateSerializer(serializers.ModelSerializer):
    "Создание транзакций"

    class Meta:
        model = Transactions
        fields = "__all__"


class ClientsSerializer(serializers.ModelSerializer):
    "Список клиентов"

    class Meta:
        model = Patient
        fields = "__all__"


class MedicalrecordSerializer(serializers.ModelSerializer):

    patient = serializers.SlugRelatedField(slug_field="surname", read_only=True)

    class Meta:
        model = Medicalrecord
        fields = "__all__"



class MedicalrecordCreateSerializer(serializers.ModelSerializer):
    "Создание транзакций"

    class Meta:
        model = Medicalrecord
        fields = "__all__"


class CabinetSerializer(serializers.ModelSerializer):
    responsible = serializers.SlugRelatedField(slug_field="surname", read_only=True)

    class Meta:
        model = Cabinet
        fields = "__all__"

class CabinetCreateSerializer(serializers.ModelSerializer):
    "Создание транзакций"

    class Meta:
        model = Cabinet
        fields = "__all__"


class ReceptionSerializer(serializers.ModelSerializer):
    doctor = serializers.SlugRelatedField(slug_field="surname", read_only=True)
    patients = serializers.SlugRelatedField(slug_field="surname", read_only=True)

    class Meta:
        model = Reception
        fields = "__all__"


class ReceptionCreateSerializer(serializers.ModelSerializer):
    "Создание транзакций"

    class Meta:
        model = Reception
        fields = "__all__"


class ReviewsSerializer(serializers.ModelSerializer):
    reception = ReceptionSerializer()

    class Meta:
        model = Reviews
        fields = "__all__"


class ReviewsCreateSerializer(serializers.ModelSerializer):
    "Создание транзакций"

    class Meta:
        model = Reviews
        fields = "__all__"