# -*- coding: utf-8 -*-
# @Time     : 2019/5/18 16:21
# @Author   ：Wang Guosong
# @File     : urls.py
# @Software : PyCharm

from django.urls import path
from . import views

urlpatterns = [
    path('', views.msgproc),
]