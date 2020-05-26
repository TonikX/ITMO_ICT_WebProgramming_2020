from rest_framework import serializers

from quests.models import Quest, Task, Answer


class AnswerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'


class AnswerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'
        read_only_fields = ['task']


class TaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class TaskDetailSerializer(serializers.ModelSerializer):
    answers = AnswerDetailSerializer(many=True, required=False)

    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ['quest', 'answers']


class TaskListSerializer(serializers.ModelSerializer):
    answers = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = ['answers', 'content']

    def get_answers(self, obj):
        return [answer.answer for answer in obj.answers.all()]


class QuestDetailSerializer(serializers.ModelSerializer):
    tasks = TaskListSerializer(many=True, required=False)

    class Meta:
        model = Quest
        fields = '__all__'
        read_only_fields = ['tasks', 'answers']


class QuestListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quest
        fields = ['id', 'title', 'place', 'start_time', 'duration']
