from rest_framework import serializers
from school.models import Subject, Room, Teacher, Pupil, Class, Assessment, Timetable


class SubjectSerializers(serializers.ModelSerializer):

    class Meta:
        model = Subject
        fields = ('name', 'sub_type')


class TeacherSerializers(serializers.ModelSerializer):

    #subjects = SubjectSerializers()
    class Meta:
        model = Teacher
        fields = ('name', 'gender', 'experience', 'room', 'subjects', 'class')


class RoomSerializers(serializers.ModelSerializer):

    subject = SubjectSerializers()
    teacher = TeacherSerializers()
    class Meta:
        model = Room
        fields = ('number', 'floor', 'subject', 'teacher')


class ClassSerializers(serializers.ModelSerializer):

    guiding_teacher = TeacherSerializers()
    class Meta:
        model = Class
        fields = ('name', 'guiding_teacher')


class PupilSerializers(serializers.ModelSerializer):

    study_class = ClassSerializers()
    class Meta:
        model = Pupil
        fields = ('name', 'gender', 'study_class')


class AssessmentSerializers(serializers.ModelSerializer):

    subject = SubjectSerializers()
    pupil = PupilSerializers()
    class Meta:
        model = Assessment
        fields = ('term', 'grade', 'pupil', 'subject')


class TimetableSerializers(serializers.ModelSerializer):

    study_class = ClassSerializers()
    subject = SubjectSerializers()
    room = RoomSerializers()
    teacher = TeacherSerializers()
    class Meta:
        model = Timetable
        fields = ('day_of_week', 'study_class', 'lesson_num', 'subject', 'room', 'teacher')
