from rest_framework import serializers

from quests.models import Quest, Task, Answer, Tip, PenaltyTime


class PenaltyTimeDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PenaltyTime
        fields = '__all__'
        read_only_fields = ['quest']


class TipDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tip
        fields = '__all__'
        read_only_fields = ['task']


class TipListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tip
        fields = ['tip']


class AnswerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'
        read_only_fields = ['task']


class TaskDetailSerializer(serializers.ModelSerializer):
    answers = AnswerDetailSerializer(many=True, required=True)
    tips = TipDetailSerializer(many=True, required=True)

    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ['quest', 'answers', 'tips']


class QuestDetailSerializer(serializers.ModelSerializer):
    tasks = TaskDetailSerializer(many=True, required=True)
    penalty_times = PenaltyTimeDetailSerializer(many=True, required=True)

    class Meta:
        model = Quest
        fields = '__all__'

    def create(self, validated_data):
        tasks = validated_data.pop('tasks')
        penalty_times = validated_data.pop('penalty_times')
        quest_instance = Quest.objects.create(**validated_data)
        for penalty_time in penalty_times:
            PenaltyTime.objects.create(quest=quest_instance, **penalty_time)
        for task in tasks:
            task_instance = Task.objects.create(quest=quest_instance, **task)
            answers = tasks.pop('answers')
            for answer in answers:
                Answer.objects.create(task=task_instance, **answer)
            tips = tasks.pop('tips')
            for tip in tips:
                Tip.objects.create(task=task_instance, **tip)
        return quest_instance

    def update(self, instance, validated_data):
        tasks = validated_data.pop('tasks')
        penalty_times = validated_data.pop('penalty_times')
        instance.penalty_times.all().delete()
        for penalty_time in penalty_times:
            PenaltyTime.objects.create(quest=instance, **penalty_time)
        instance.tasks.all().delete()
        for task in tasks:
            task_instance = Task.objects.create(quest=instance, **task)
            answers = tasks.pop('answers')
            task.answers.all().delete()
            for answer in answers:
                Answer.objects.create(task=task_instance, **answer)
            tips = tasks.pop('tips')
            task.tips.all().delete()
            for tip in tips:
                Tip.objects.create(task=task_instance, **tip)
        return super().update(instance, validated_data)


class QuestListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quest
        fields = ['id', 'title', 'place', 'start_time', 'duration']
