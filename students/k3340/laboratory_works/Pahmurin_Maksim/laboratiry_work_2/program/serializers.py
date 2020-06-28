from rest_framework import serializers
from .models import *


class GroupListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"


class StudentListSerializer(serializers.ModelSerializer):
    group = GroupListSerializer(many=False, required=True)

    class Meta:
        model = Students
        fields = "__all__"


class StudentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = "__all__"

class TeacherListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teachers
        fields = "__all__"


class SubjectListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subjects
        fields = "__all__"



class SheduleSerializer(serializers.ModelSerializer):
    teacher = TeacherListSerializer(many=False, required=False)
    subject = SubjectListSerializer(many=False, required=False)
    group = GroupListSerializer(many=False, required=False)
    class Meta:
        model = Shedule
        fields = "__all__"


class SheduleCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shedule
        fields = "__all__"

class RecordListSerializer(serializers.ModelSerializer):
    student = StudentListSerializer(many=False, required=False)
    subject = SubjectListSerializer(many=False, required=False)

    class Meta:
        model = Rating
        fields = "__all__"


class RecordCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = "__all__"


