from lufeiCity import settings

from rest_framework.views import APIView
from rest_framework.viewsets import ViewSetMixin
from rest_framework.response import Response

from api.models import CourseCategory, CourseSubCategory, \
    DegreeCourse, Teacher, Scholarship, Course, CourseDetail, OftenAskedQuestion, \
    CourseOutline, CourseChapter, CourseSection

from api.utils.response import BaseResponse
import json

import redis

CONN = redis.Redis(host='192.168.11.161', port=6379)

USER_ID = 1


class ShoppingCarView(ViewSetMixin, APIView):

    def list(self, request, *args, **kwargs):
        '''查看购物车信息'''
        ret = {'code': 1000, 'data': None, 'error': None}

        try:
            shopping_car_course_list = []
            pattern = settings.LUFFY_SHOPPING_CAR % (USER_ID, '*',)

            user_key_list = CONN.keys(pattern)
            for key in user_key_list:
                temp = {
                    'id': CONN.hget(key, 'id').decode('utf-8'),
                    'name': CONN.hget(key, 'name').decode('utf-8'),
                    'img': CONN.hget(key, 'img').decode('utf-8'),
                    'default_price_id': CONN.hget(key, 'default_price_id').decode('utf-8'),
                    'price_policy_dict': json.loads(CONN.hget(key, 'price_policy_dict').decode('utf-8'))
                }

                shopping_car_course_list.append(temp)

            ret['data'] = shopping_car_course_list

        except Exception as e:
            ret['code'] = 1001
            ret['error'] = '获取不到购物车的数据'

        return Response(ret)

        return Response('ok')

    def create(self, request, *args, **kwargs):
        res = {'code': 1000, 'data': None, 'error': None}
        """
                1. 接受用户选中的课程ID和价格策略ID
                2. 判断合法性
                    - 课程是否存在？
                    - 价格策略是否合法？
                3. 把商品和价格策略信息放入购物车 SHOPPING_CAR

                注意：用户ID=1
                """
        # 1. 接收用户选中的课程ID和价格策略ID
        course_id = request.data.get('courseid')
        policy_id = request.data.get('policyid')  # policy_id时随便自定义的变量名

        # 2.判断课程是否存在？
        course = Course.objects.filter(id=course_id).first()
        print(course)
        if not course:
            return Response({'code': 1001, 'error': '课程不存在'})

        # 判断价格策略是否匹配
        price_policy_queryset = course.price_policy.all()
        price_policy_dict = {}

        print(price_policy_queryset)

        for item in price_policy_queryset:
            tmp = {
                'id': item.id,
                'price': item.price,
                'valid_period': item.valid_period,
                'valid_period_display': item.get_valid_period_display()
            }
            price_policy_dict[item.id] = tmp

        if policy_id not in price_policy_dict:
            return Response({'code': 1001, 'error': '价格策略不匹配'})

        # 3.
        # 把商品和价格策略信息放入购物车
        # SHOPPING_CAR
        # 购物车中要放：
        # 课程ID
        # 课程名称
        # 课程图片
        # 默认选中的价格策略
        # 所有价格策略
        # 注意：用户ID = 1

        key = "shopping_car_%s_%s" % (USER_ID, course_id,)

        CONN.hset(key, 'id', course_id)
        CONN.hset(key, 'name', course.name)
        CONN.hset(key, 'img', course.course_img)
        CONN.hset(key, 'default_price_policy', policy_id)
        CONN.hset(key, 'price_policy_dict', price_policy_dict)

        CONN.expire(key, 10)
        return Response({'code': 1000, 'data': '购买课程成功'})

    def destroy(self, request, *args, **kwargs):
        '''删除购物车中的某个课程'''
        response = BaseResponse()
        try:
            courseid = request.GET.get('courseid')
            key = settings.LUFFY_SHOPPING_CAR % (USER_ID, courseid)

            CONN.delete(key)

            response.data = '删除成功'

        except Exception as e:
            response.code = 1001
            response.error = '删除失败'

        return Response(response.dict)

    def update(self, request, *args, **kwargs):

        response = BaseResponse()

        try:
            courseid = request.data.get('courseid')
            policy_id = str(request.data.get('policyid')) if request.data.get('policyid') else None

            key = settings.LUFFY_SHOPPING_CAR % (USER_ID, courseid,)

            if not CONN.exists(key):
                response.code = 1001
                response.error = '课程不存在'
                return Response(response.dict)

            price_policy_dict = json.loads(CONN.hget(key, 'price_policy_dict'))
            if policy_id not in price_policy_dict:
                response.code = 1001
                response.error = '价格策略不存在'
                return Response(response.dict)

            CONN.hset(set, 'default_price_id', policy_id)  # 修改价格id 即修改价格策略
            CONN.expire(10)
            response.data = '修改成功'
        except Exception as e:
            response.code = 1001
            response.error = '修改失败'
        return Response(response.dict)
