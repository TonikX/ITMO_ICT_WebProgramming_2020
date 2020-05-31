from rest_framework import serializers
from .models import UserProfile,Teacher,Timetable,Klass,Pupil,Cabinet,Subject, Grade


class TeacherSerializer(serializers.ModelSerializer):
    """Список учителей"""
    class Meta:
        model = Teacher
        fields = ("id", "last_name", "first_name", "second_name")


class TeacherDetailSerializer(serializers.ModelSerializer):
    """Досье учителя"""
    subject = serializers.SlugRelatedField(slug_field = "subject", read_only=True)
    class Meta:
        model = Teacher
        fields = "__all__"

class TeacherAddSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        fields = "__all__"


class PupilSerializer(serializers.ModelSerializer):
    """Список учителей"""
    class Meta:
        model = Pupil
        fields = ("id", "last_name", "first_name", "second_name")


class GradeCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Grade
        fields = "__all__"


class GradeSerializer(serializers.ModelSerializer):
    subject = serializers.SlugRelatedField(slug_field = "subject", read_only=True)
    class Meta:
        model = Grade
        fields = ("subject", "grade")


class PupilDetailSerializer(serializers.ModelSerializer):
    """Досье учителя"""
    klass = serializers.SlugRelatedField(slug_field = "number", read_only=True)
    grades = GradeSerializer(many=True)
    class Meta:
        model = Pupil
        fields = "__all__"


class PupilAddSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pupil
        fields = "__all__"


class TimetableAddSerializer(serializers.ModelSerializer):

    class Meta:
        model = Timetable
        fields = "__all__"


class TimetableSerializer(serializers.ModelSerializer):
    subject_name = serializers.SlugRelatedField(slug_field="subject", read_only=True)
    cabinet_number = serializers.SlugRelatedField(slug_field="number", read_only=True)
    teacher_name = serializers.SlugRelatedField(slug_field="last_name", read_only=True)
    klass_name = serializers.SlugRelatedField(slug_field="number", read_only=True)

    class Meta:
        model = Timetable
        fields = "__all__"


class KlassSerializer(serializers.ModelSerializer):
    """Досье учителя"""
    teacher = serializers.SlugRelatedField(slug_field="last_name", read_only=True)
    class Meta:
        model = Klass
        fields = "__all__"


class KlassAddSerializer(serializers.ModelSerializer):
    """Досье учителя"""
    class Meta:
        model = Klass
        fields = "__all__"


class KlassDetailSerializer(serializers.ModelSerializer):
    """Досье учителя"""
    teacher = serializers.SlugRelatedField(slug_field="last_name", read_only=True)
    pupils = PupilSerializer(many=True)
    class Meta:
        model = Klass
        fields = "__all__"


class SubjectSerializer(serializers.ModelSerializer):
    """Досье учителя"""
    class Meta:
        model = Subject
        fields = "__all__"


class CabinetSerializer(serializers.ModelSerializer):
    """Досье учителя"""
    teacher = serializers.SlugRelatedField(slug_field="last_name", read_only=True)

    class Meta:
        model = Cabinet
        fields = "__all__"