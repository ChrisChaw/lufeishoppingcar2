from rest_framework import serializers

class CourseSerializer3(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    level = serializers.CharField(source='get_level_display')
    why_study = serializers.CharField(source='coursedetail.why_study')
    what_to_study_brief = serializers.CharField(source='coursedetail.what_to_study_brief')
    recommend_courses = serializers.CharField(source='coursedetail.recommend_courses.all')
    # asked_question = serializers.CharField(source='asked_question.all')
    CourseOutline = serializers.CharField(source='coursedetail.courseoutline_set.all')
    # CourseChapter = serializers.CharField(source='coursechapters')
    demo = serializers.SerializerMethodField()

    def get_demo(self,obj):
        data=obj.coursedetail.why_study
        return data