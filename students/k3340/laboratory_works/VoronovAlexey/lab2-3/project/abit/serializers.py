from rest_framework import serializers
from abit import models

class Study_Program_Serialzer(serializers.ModelSerializer):
    class Meta:
        model = models.Study_Program
        fields = ['name', 'count']

class Study_Place_Serialzer(serializers.ModelSerializer):
    class Meta:
        model = models.Study_Place
        fields = ['name', 'place', 'type']

class Abitutient_Serialzer(serializers.ModelSerializer):
    study_place = Study_Place_Serialzer()
    study_program = Study_Program_Serialzer()

    class Meta:
        model = models.Abiturient
        fields = ['surname', 'name', 'secondname', 'document_type', 'document_number', 'study_place', 'study_date', 'award_type', 'study_type', 'contract_type', 'student_type', 'study_program', 'marks', 'accepted']