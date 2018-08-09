from rest_framework import serializers

class CourseSerializer4(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    asked_question = serializers.CharField(source='asked_question.all')