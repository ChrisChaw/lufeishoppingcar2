from django.shortcuts import HttpResponse

from rest_framework.views import APIView
from rest_framework.versioning import URLPathVersioning
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.viewsets import ViewSetMixin

from api.utils.response import BaseResponse
from api.models import CourseCategory,CourseSubCategory,\
    DegreeCourse,Teacher,Scholarship,Course,CourseDetail,OftenAskedQuestion,\
    CourseOutline,CourseChapter,CourseSection
from api.serializer.degreeCourse import DegreeCourseSerializer
from api.serializer.degreeCourse2 import DegreeCourseSerializer2
from api.serializer.degreeCourse3 import DegreeCourseSerializer3
from api.serializer.course2 import CourseSerializer2
from api.serializer.course3 import CourseSerializer3
from api.serializer.course4 import CourseSerializer4
from api.serializer.course5 import CourseSerializer5
from api.serializer.course6 import CourseSerializer6
from api.serializer.course7 import CourseSerializer7,CourseModelSerializer7
class CourseView(APIView):
    def get(self,request,*args,**kwargs):
        result = ''
        if request.version == 'v1':
            result = 'v1'
        else:
            result = '其他'
        return HttpResponse(result)


class DegreeCourseView(APIView):

    def get(self,request,*args,**kwargs):
        ret = BaseResponse()
        try:
             # 从数据库获取数据
             queryset = DegreeCourse.objects.all()

             # 分页
             page = PageNumberPagination()
             degree_list = page.paginate_queryset(queryset,request,self)

             # 分页之后的结果执行序列化
             ser = DegreeCourseSerializer(instance=degree_list,many=True)

             ret.data = ser.data

        except Exception as e:
            ret.code = 1001
            ret.error = '获取数据失败'

        return Response(ret.dict)

# a.查看所有学位课并打印学位课名称以及授课老师
# degree_list = DegreeCourse.objects.all().values('name', 'teachers__name')
# queryset = DegreeCourse.objects.all()
# for row in queryset:
#     row.name,row.teachers.all()

class DegreeCourseView2(APIView):
    def get(self,request,*args,**kwargs):
        ret = BaseResponse()
        try:
            # 从数据库取值
            queryset = DegreeCourse.objects.all()
            print(111,queryset)
            #分页
            page = PageNumberPagination()
            degree_list = page.paginate_queryset(queryset,request,self)
            print(222,degree_list)
            #分页之后序列化
            ser = DegreeCourseSerializer2(instance=degree_list,many=True)
            print(ser)

            ret.data = ser.data

        except Exception as e:
            ret.code = 1001
            ret.error = '获取数据失败'

        return Response(ret.dict)
# b.查看所有学位课并打印学位课名称以及学位课的奖学金
# c_obj=DegreeCourse.objects.all()
# for i in c_obj:
#     print(i.name)
#     print(i.degreecourse_price_policy.all().values('price'))

# degree_list = DegreeCourse.objects.all()
# for row in degree_list:
#     print(row.name)
#     scholarships = row.scholarship_set.all()
#     for item in scholarships:
#         print('------>',item.time_percent,item.value)

class CourseView2(APIView):

    def get(self,request,*args,**kwargs):
        ret = BaseResponse()

        try:
            queryset = Course.objects.all()

            page = PageNumberPagination()
            course_list=page.paginate_queryset(queryset,request,self)

            ser = CourseSerializer2(instance=course_list,many=True)

            ret.data = ser.data
        except Exception as e:
            ret.code = 1001
            ret.error = '获取数据失败'

        return Response(ret.dict)
# c. 展示所有的专题课
# c_obj=Course.objects.filter(degree_course__isnull=True)
# print(c_obj)

class DegreeCourseView3(APIView):
    def get(self,request,*args,**kwargs):
        ret = BaseResponse()
        try:
            # queryset = DegreeCourse.objects.filter(你的过滤条件有错误)
            queryset = DegreeCourse.objects.filter(id=1)
            page = PageNumberPagination()
            degree_list = page.paginate_queryset(queryset,request,self)
            print(222,degree_list)

            ser = DegreeCourseSerializer3(instance=degree_list,many=True)
            print(222,ser)
            ret.data = ser.data

        except Exception as e:
            ret.code = 1001
            ret.error = '获取数据失败'

        return Response(ret.dict)
# d. 查看id=1的学位课对应的所有模块名称
# a_obj=DegreeCourse.objects.filter(id=1).values('course__name')
# print(a_obj)

# obj = DegreeCourse.objects.get(id=1)
# course_list = obj.course_set.all()
# print(course_list)
#
# course_list = Course.objects.filter(degree_course_id=1)
# print(course_list)
#

class CourseView3(APIView):
    def get(self,request,*args,**kwargs):
        ret =BaseResponse()
        try:
            queryset = Course.objects.filter(id=1,degree_course__isnull=True)

            page = PageNumberPagination()
            course_list = page.paginate_queryset(queryset,request,self)

            ser = CourseSerializer3(instance=course_list,many=True)

            ret.data = ser.data

        except Exception as e:
            ret.code = 1001
            ret.error = '获取数据失败'

        return Response(ret.dict)
#  e.获取id = 1的专题课，并打印：课程名、级别(中文)、why_study、what_to_study_brief、所有recommend_courses
# c_obj =Course.objects.filter(id=1)
# print(c_obj.values('name'))
# print(c_obj.first().get_level_display())
# print(c_obj.values('coursedetail__why_study'))
# print(c_obj.values('coursedetail__what_to_study_brief'))
# print(c_obj.values('coursedetail__recommend_courses'))

# obj = Course.objects.get(id=1)
# print(obj.name)
# print(obj.brief)
# print(obj.get_level_display() )
# print(obj.coursedetail.hours )
# print(obj.coursedetail.why_study )
# print(obj.coursedetail.recommend_courses.all() )


class CourseView4(APIView):
    def get(self,request,*args,**kwargs):
        ret = BaseResponse()
        try:
            queryset = Course.objects.filter(id=1)
            page=PageNumberPagination()
            course_list = page.paginate_queryset(queryset,request,self)
            ser = CourseSerializer4(instance=course_list,many=True)
            ret.data=ser.data
        except Exception as e:
            ret.code = 1001
            ret.error = '获取数据失败'

        return Response(ret.dict)
# f.获取id = 1的专题课，并打印该课程相关的所有常见问题
# c_obj = Course.objects.filter(id=1).first()
# print(c_obj.asked_question.all().values('question'))

# obj = Course.objects.get(id=1)
# ask_list = obj.asked_question.all()
# for item in ask_list:
#     print(item.question,item.answer)

class CourseView5(APIView):
    def get(self,request,*args,**kwargs):
        ret = BaseResponse()
        try:
            queryset = Course.objects.filter(id=1)
            page=PageNumberPagination()
            course_list = page.paginate_queryset(queryset,request,self)
            ser = CourseSerializer5(instance=course_list,many=True)
            ret.data=ser.data
        except Exception as e:
            ret.code = 1001
            ret.error = '获取数据失败'

        return Response(ret.dict)
# g.获取id = 1的专题课，并打印该课程相关的课程大纲
# c_obj = Course.objects.filter(id=1)
# print(c_obj.values('coursedetail__courseoutline__title'))

# obj = Course.objects.get(id=1)
# outline_list = obj.coursedetail.courseoutline_set.all()
# for item in outline_list:
#     print(item.title,item.content)
#

class CourseView6(APIView):
    def get(self,request,*args,**kwargs):
        ret = BaseResponse()
        try:
            queryset = Course.objects.filter(id=1)
            page=PageNumberPagination()
            course_list = page.paginate_queryset(queryset,request,self)
            ser = CourseSerializer6(instance=course_list,many=True)
            ret.data=ser.data
        except Exception as e:
            ret.code = 1001
            ret.error = '获取数据失败'

        return Response(ret.dict)
# h.获取id = 1的专题课，并打印该课程相关的所有章节
# c_obj = Course.objects.filter(id=1)
# print(c_obj.values('coursechapters__name'))

# obj = Course.objects.get(id=1)
# chapter_list = obj.xxxxx.all() # 默认obj.表名_set.all()
# for item in chapter_list:
#     print(item.name)

class CourseView7(ViewSetMixin,APIView):
    def list(self,request,*args,**kwargs):
        ret = BaseResponse()

        try:
            queryset=Course.objects.all()
            # 分页
            page = PageNumberPagination()
            course_list = page.paginate_queryset(queryset, request, self)

            # 分页之后的结果执行序列化
            ser = CourseModelSerializer7(instance=course_list, many=True)

            ret.data = ser.data
        except Exception as e:
            ret.code = 500
            ret.error = '获取数据失败'

        return Response(ret.dict,headers={'Access-Control-Allow-Origin':'http://localhost:8080'})



    def retrieve(self, request, pk, *args, **kwargs):
        response = {'code': 1000, 'data': None, 'error': None}
        try:
            course = Course.objects.get(id=pk)
            ser = CourseModelSerializer7(instance=course)
            response['data'] = ser.data
        except Exception as e:
            response['code'] = 500
            response['error'] = '获取数据失败'
        return Response(response)












