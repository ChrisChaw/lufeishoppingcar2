from rest_framework import serializers

class DegreeCourseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    teacher__name = serializers.CharField(source='teachers.all')