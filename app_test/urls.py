# -*- coding: utf-8 -*-
"""
@Time ： 2020/5/15 10:12
@Auth ： Minhang
@File ：urls.py
@IDE  ：PyCharm
"""

from app_test.api_layer.test.test_view import MyTest

urlpatterns = [
    ("test/",MyTest)
]

