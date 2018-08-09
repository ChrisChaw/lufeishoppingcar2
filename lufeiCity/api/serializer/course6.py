from rest_framework import serializers

class CourseSerializer6(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    CourseChapter = serializers.CharField(source='coursechapters')