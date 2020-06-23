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

    def fill_quest(self, instance, tasks, penalty_times):
        for penalty_time in penalty_times:
            PenaltyTime.objects.create(quest=instance, **penalty_time)
        for task in tasks:
            answers = task.pop('answers')
            tips = task.pop('tips')
            task_instance = Task.objects.create(quest=instance, **task)
            for answer in answers:
                Answer.objects.create(task=task_instance, **answer)
            for tip in tips:
                Tip.objects.create(task=task_instance, **tip)

    def create(self, validated_data):
        tasks = validated_data.pop('tasks')
        penalty_times = validated_data.pop('penalty_times')
        quest_instance = Quest.objects.create(**validated_data)
        self.fill_quest(quest_instance, tasks=tasks, penalty_times=penalty_times)
        return quest_instance

    def update(self, instance, validated_data):
        tasks = validated_data.pop('tasks')
        penalty_times = validated_data.pop('penalty_times')
        instance.penalty_times.all().delete()
        instance.tasks.all().delete()
        self.fill_quest(instance, tasks=tasks, penalty_times=penalty_times)
        return super().update(instance, validated_data)

    def validate(self, attrs):
        penalty_times = len(attrs['penalty_times'])
        for answer in attrs['tasks']:
            if len(answer['tips']) != penalty_times:
                raise serializers.ValidationError("Number of tips must be equal to number of penalty times")
        return attrs


class QuestListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quest
        fields = ['id', 'title', 'place', 'start_time', 'duration']
