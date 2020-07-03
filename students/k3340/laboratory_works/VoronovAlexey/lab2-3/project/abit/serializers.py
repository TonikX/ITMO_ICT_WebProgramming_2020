from rest_framework import serializers
from abit import models

class Study_Program_Serialzer(serializers.ModelSerializer):
    class Meta:
        model = models.Study_Program
        fields = ['name', 'count', 'id']

class Study_Place_Serialzer(serializers.ModelSerializer):
    class Meta:
        model = models.Study_Place
        fields = ['name', 'place', 'type', 'id']

class Abitutient_Serialzer_Get(serializers.ModelSerializer):
    study_place = Study_Place_Serialzer(read_only=True)
    study_program = Study_Program_Serialzer(read_only=True)

    class Meta:
        model = models.Abiturient
        fields = ['surname', 'name', 'secondname', 'document_type', 'document_number', 'study_place', 'study_date', 'award_type', 'study_type', 'contract_type', 'abit_type' ,'student_type', 'study_program', 'marks', 'accepted', 'id']


class Abitutient_Serialzer_Post(serializers.ModelSerializer):
    study_place = serializers.PrimaryKeyRelatedField(queryset=models.Study_Place.objects.all(), write_only=False)
    study_program = serializers.PrimaryKeyRelatedField(queryset=models.Study_Program.objects.all(), write_only=False)

    class Meta:
        model = models.Abiturient
        fields = ['surname', 'name', 'secondname', 'document_type', 'document_number', 'study_place', 'study_date', 'award_type', 'study_type', 'contract_type', 'abit_type' ,'student_type', 'study_program', 'marks', 'accepted', 'id']