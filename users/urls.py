# -*- coding: utf-8 -*-
"""
@author: ZJ
@email: 1576094876@qq.com
@File : urls.py
@Site : 
@desc: 
@Created on: 2020/7/24 10:51
"""
from django.http import HttpResponse
from django.urls import path
from users.views import RegisterView
# 1.导入系统的logging
import logging
#2.创建获取日志器
logger = logging.getLogger("django")

def log_test(request):
    logger.info("测试log")
    return HttpResponse("test_log")


urlpatterns = [
    # 参数1：路由
    # 参数2：视图函数
    # 参数3：路由名，方便通过reverse来获取路由
    path('register/',RegisterView.as_view(),name ="register"),
    # path("",log_test)

]
