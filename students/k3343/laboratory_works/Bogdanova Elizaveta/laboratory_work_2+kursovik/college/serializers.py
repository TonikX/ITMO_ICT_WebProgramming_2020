from rest_framework import serializers
from .models import Faculty, Specialty, Enrollee, Application,EGE, EgeSubject, Attestat, AttestatSubject


class AttestatSubjectSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Дисциплина аттестата"""
    class Meta:
        model = AttestatSubject
        fields = "__all__"


class AttestatSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Аттестат"""
    enrollee = serializers.SlugRelatedField(slug_field="fio", read_only=True)
    marks = AttestatSubjectSerializer(many=True)

    class Meta:
        model = Attestat
        fields = "__all__"


class AttestatCreateSerializer(serializers.ModelSerializer):
    """Сериализатор для добавления нового аттестата """

    class Meta:
        model = Attestat
        fields = "__all__"


class EgeSubjectSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Дисциплина ЕГЭ"""

    class Meta:
        model = EgeSubject
        fields = "__all__"


class EgeSerializer(serializers.ModelSerializer):
    """Сериализатор для модели ЕГЭ"""
    enrollee = serializers.SlugRelatedField(slug_field="fio", read_only=True)
    marks = EgeSubjectSerializer(many=True)

    class Meta:
        model = EGE
        fields = "__all__"


class EgeCreateSerializer(serializers.ModelSerializer):
    """Сериализатор для добавления нового сертификата ЕГЭ"""

    class Meta:
        model = EGE
        fields = "__all__"


class ApplicationSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Заявка"""
    enrollee = serializers.SlugRelatedField(slug_field="fio", read_only=True)
    specialty = serializers.SlugRelatedField(slug_field="name", read_only=True)
    faculty = serializers.SlugRelatedField(slug_field="name", read_only=True)

    class Meta:
        model = Application
        fields = "__all__"


class ApplicationCreateSerializer(serializers.ModelSerializer):
    """Сериализатор для добавления новой заявки """
    class Meta:
        model = Application
        fields = "__all__"


class EnrolleeSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Абитуриент"""
    class Meta:
        model = Enrollee
        fields = "__all__"


class EnrolleeDetailSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Абитуриент"""
    apps = ApplicationSerializer(many=True)

    class Meta:
        model = Enrollee
        fields = "__all__"


class SpecialtySerializer(serializers.ModelSerializer):
    """Сериализатор для модели Специальность"""
    class Meta:
        model = Specialty
        fields = "__all__"


class FacultySerializer(serializers.ModelSerializer):
    """Сериализатор для модели Факультет"""
    specialties = SpecialtySerializer(many=True)

    class Meta:
        model = Faculty
        fields = "__all__"

