from rest_framework import serializers
from .models import Teacher,Timetable,Nclass,Children,Room,Subject, Grade


class TeacherListSerializer(serializers.ModelSerializer):
    """Список учителей"""

    class Meta:
        model = Teacher
        fields = ("id", "surname", "name", "second_name", "teaching_period")


class TeacherAddSerializer(serializers.ModelSerializer):
    """Новый учитель"""

    class Meta:
        model = Teacher
        fields = "__all__"


class ChildrenListSerializer(serializers.ModelSerializer):
    """Список учеников"""

    class Meta:
        model = Children
        fields = ("id", "surname", "name", "second_name")


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


class ChildrenDetailSerializer(serializers.ModelSerializer):
    """Досье ученика"""
    nclass = serializers.SlugRelatedField(slug_field = "number", read_only=True)
    grades = GradeSerializer(many=True)

    class Meta:
        model = Children
        fields = "__all__"


class ChildrenAddSerializer(serializers.ModelSerializer):
    """Новый ученик"""

    class Meta:
        model = Children
        fields = "__all__"


class TimetableAddSerializer(serializers.ModelSerializer):
    """Добавление расписания"""

    class Meta:
        model = Timetable
        fields = "__all__"


class TimetableSerializer(serializers.ModelSerializer):
    """Вывод расписания"""
    subject_name = serializers.SlugRelatedField(slug_field="subject", read_only=True)
    room_number = serializers.SlugRelatedField(slug_field="number", read_only=True)
    teacher_name = serializers.SlugRelatedField(slug_field="surname", read_only=True)
    nclass_name = serializers.SlugRelatedField(slug_field="number", read_only=True)

    class Meta:
        model = Timetable
        fields = "__all__"


class NclassSerializer(serializers.ModelSerializer):
    """Список классов"""
    teacher = serializers.SlugRelatedField(slug_field = "surname", read_only=True)

    class Meta:
        model = Nclass
        fields = "__all__"


class NclassAddSerializer(serializers.ModelSerializer):
    """Новый класс"""

    class Meta:
        model = Nclass
        fields = "__all__"


class NclassDetailSerializer(serializers.ModelSerializer):
    """Информауия о классе"""
    teacher = serializers.SlugRelatedField(slug_field = "surname", read_only=True)
    children = ChildrenListSerializer(many=True)
    timetable = TimetableSerializer(many=True)

    class Meta:
        model = Nclass
        fields = "__all__"


class SubjectSerializer(serializers.ModelSerializer):
    """Список предметов"""

    class Meta:
        model = Subject
        fields = "__all__"


class RoomSerializer(serializers.ModelSerializer):
    """Список кабинетов"""
    teacher = serializers.SlugRelatedField(slug_field="surname", read_only=True)

    class Meta:
        model = Room
        fields = "__all__"
        
        
class TeacherDetailSerializer(serializers.ModelSerializer):
    """Учитель"""
    subject = serializers.SlugRelatedField(slug_field="subject", read_only=True)
    nclass = NclassSerializer(many=True)
    room = RoomSerializer(many=True)

    class Meta:
        model = Teacher
        fields = "__all__"
