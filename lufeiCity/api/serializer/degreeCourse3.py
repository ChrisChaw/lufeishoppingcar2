from rest_framework import serializers

class DegreeCourseSerializer3(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    model = serializers.SerializerMethodField()

    def get_model(self,obj):
        li = []
        for item in obj.course_set.all():
            li.append(item.name)
        return li