from rest_framework import serializers

class DegreeCourseSerializer2(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    # scholarship__value = serializers.CharField(source='scholarship_set.all')
    scholarship = serializers.SerializerMethodField()

    '''下面的方法可以以value字段显示 不定义下面的方法不能以value字段显示'''
    def get_scholarship(self,obj):
        li = []
        for item in obj.scholarship_set.all():
            li.append(item.value)
        return li