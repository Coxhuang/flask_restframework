# -*- coding: utf-8 -*-
"""
@Time ： 2020/5/14 19:10
@Auth ： Minhang
@File ：urls.py
@IDE  ：PyCharm
"""
from app_user import urls as user_urls
from app_test import urls as test_urls

urlpatterns = [
    ("User","/api/user/",user_urls),
    ("Test","/api/test/",test_urls),
]