from rest_framework import serializers

from quests.models import Quest, Task, Answer


class TaskDetailSerializer(serializers.ModelSerializer):
    answers = serializers.ListSerializer(required=True, child=serializers.CharField())

    class Meta:
        model = Task
        fields = ['answers', 'content', 'tip_1', 'tip_2', 'title']


class QuestDetailSerializer(serializers.ModelSerializer):
    tasks = TaskDetailSerializer(many=True, required=True)

    class Meta:
        model = Quest
        fields = '__all__'

    def recreate_tasks(self, instance, tasks):
        for task in tasks:
            answers = task.pop('answers')
            task_instance = Task.objects.create(quest=instance, **task)
            for answer in answers:
                Answer.objects.create(task=task_instance, answer=answer)

    def create(self, validated_data):
        tasks = validated_data.pop('tasks')
        quest_instance = Quest.objects.create(**validated_data)
        self.recreate_tasks(quest_instance, tasks=tasks)
        return quest_instance

    def update(self, instance, validated_data):
        tasks = validated_data.pop('tasks')
        instance.tasks.all().delete()
        self.recreate_tasks(instance, tasks=tasks)
        return super().update(instance, validated_data)


class QuestListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quest
        fields = ['id', 'title', 'place', 'start_time', 'duration']
