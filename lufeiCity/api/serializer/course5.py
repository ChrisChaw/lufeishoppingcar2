from rest_framework import serializers

class CourseSerializer5(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    CourseOutline = serializers.CharField(source='coursedetail.courseoutline_set.all')