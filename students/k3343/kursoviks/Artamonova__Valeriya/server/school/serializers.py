from rest_framework import serializers
from .models import Teacher,Timetable,Klass,Pupil,Cabinet,Subject, Grade


class TeacherSerializer(serializers.ModelSerializer):
    """Список учителей"""
    class Meta:
        model = Teacher
        fields = ("id", "last_name", "first_name", "second_name", "teaching_period")


class TeacherAddSerializer(serializers.ModelSerializer):
    """Добавление учителя"""
    class Meta:
        model = Teacher
        fields = "__all__"


class PupilSerializer(serializers.ModelSerializer):
    """Список учеников"""
    class Meta:
        model = Pupil
        fields = ("id", "last_name", "first_name", "second_name")


class GradeCreateSerializer(serializers.ModelSerializer):
    """Добавление оценки"""
    class Meta:
        model = Grade
        fields = "__all__"


class GradeSerializer(serializers.ModelSerializer):
    """Вывод оценок"""
    subject = serializers.SlugRelatedField(slug_field="subject", read_only=True)

    class Meta:
        model = Grade
        fields = "__all__"


class PupilDetailSerializer(serializers.ModelSerializer):
    """Досье ученика"""
    klass = serializers.SlugRelatedField(slug_field = "number", read_only=True)
    grades = GradeSerializer(many=True)

    class Meta:
        model = Pupil
        fields = "__all__"


class PupilAddSerializer(serializers.ModelSerializer):
    """Добавление ученика"""
    class Meta:
        model = Pupil
        fields = "__all__"


class TimetableAddSerializer(serializers.ModelSerializer):
    """Добавление расписания"""
    class Meta:
        model = Timetable
        fields = "__all__"


class TimetableSerializer(serializers.ModelSerializer):
    """Вывод расписания"""
    subject_name = serializers.SlugRelatedField(slug_field="subject", read_only=True)
    cabinet_number = serializers.SlugRelatedField(slug_field="number", read_only=True)
    teacher_name = serializers.SlugRelatedField(slug_field="last_name", read_only=True)
    klass_name = serializers.SlugRelatedField(slug_field="number", read_only=True)

    class Meta:
        model = Timetable
        fields = "__all__"


class KlassSerializer(serializers.ModelSerializer):
    """Список классов"""
    teacher = serializers.SlugRelatedField(slug_field="last_name", read_only=True)
    class Meta:
        model = Klass
        fields = "__all__"


class KlassAddSerializer(serializers.ModelSerializer):
    """Добавление класса"""
    class Meta:
        model = Klass
        fields = "__all__"


class KlassDetailSerializer(serializers.ModelSerializer):
    """Описание класса"""
    teacher = serializers.SlugRelatedField(slug_field="last_name", read_only=True)
    pupils = PupilSerializer(many=True)
    timetable = TimetableSerializer(many=True)
    class Meta:
        model = Klass
        fields = "__all__"


class SubjectSerializer(serializers.ModelSerializer):
    """Список предметов"""
    class Meta:
        model = Subject
        fields = "__all__"


class CabinetSerializer(serializers.ModelSerializer):
    """Список кабинетов"""
    teacher = serializers.SlugRelatedField(slug_field="last_name", read_only=True)

    class Meta:
        model = Cabinet
        fields = "__all__"


class TeacherDetailSerializer(serializers.ModelSerializer):
    """Досье учителя"""
    subject = serializers.SlugRelatedField(slug_field="subject", read_only=True)
    klass = KlassSerializer(many=True)
    cabinet = CabinetSerializer(many=True)

    class Meta:
        model = Teacher
        fields = "__all__"