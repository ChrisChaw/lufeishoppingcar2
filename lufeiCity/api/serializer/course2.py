from rest_framework import serializers

class CourseSerializer2(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()