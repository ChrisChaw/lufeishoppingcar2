from django.shortcuts import render,HttpResponse

# Create your views here.
from api import models

def index(request):
#     a.查看所有学位课并打印学位课名称以及授课老师
#     queryset=models.DegreeCourse.objects.all()
#     for item in queryset:
#         print('#####')
#         print(item.name,item.teachers.all())
#         print('#####')

    # a = models.DegreeCourse.objects.all().values('name','teachers__name')
    # print(a)

#     b.查看所有学位课并打印学位课名称以及学位课的奖学金
    degree_course_obj2=models.DegreeCourse.objects.all()
    for item in degree_course_obj2:
        print(item.name,item.total_scholarship)
#     c.展示所有的专题课
#     models.Course.objects.filter(degree_course__isnull=True)
    course_obj1 = models.Course.objects.filter(degree_course__isnull=True)
    for item in course_obj1:
        print(item.name)
# d.查看id = 1的学位课对应的所有模块名称
    degree_course_obj3=models.Course.objects.filter(degree_course_id=1)
    for item in degree_course_obj3:
        print(item.name)
# e.获取id = 1的专题课，并打印：课程名、级别(中文)、why_study、what_to_study_brief、所有recommend_courses
    course_obj2=models.CourseDetail.objects.filter(course__id=1,course__degree_course__isnull=True)

    for item in course_obj2:
        print(88888)
        print(item.course.name,item.why_study,item.what_to_study_brief,item.recommend_courses.values('name'))
# f.获取id = 1的专题课，并打印该课程相关的所有常见问题
#     b = models.Course.objects.filter(id=1).first()
#     print(3333)
#     print(b.asked_question.all().values('question'))
#     print(4444)

    # obj=models.Course.objects.get(id=1)
    # ask_list=obj.asked_question.all()
    # print(2222)
    # print(ask_list)
    # print(8888)
    # for item in ask_list:
    #     print(item.question,item.answer)
# g.获取id = 1的专题课，并打印该课程相关的课程大纲
    course_res=models.CourseDetail.objects.filter(course_id=1).values("courseoutline__content")
    print(course_res)
# h.获取id = 1的专题课，并打印该课程相关的所有章节
    res=models.Course.objects.filter(id=1).values('coursechapters__summary')
    print(res)
# i.获取id = 1的专题课，并打印该课程相关的所有价格策略
#     ret=models.PricePolicy.objects.filter(object_id=1,content_type__model='course').values()
#     print(ret)
    c = models.Course.objects.filter(id=1).first()
    print(c.price_policy.all())

    return HttpResponse('OK')

