# -*- coding: utf-8 -*-
"""
@Time ： 2020/5/15 10:12
@Auth ： Minhang
@File ：urls.py
@IDE  ：PyCharm
"""

from app_user.api_layer.user.create_user_view import HelloWorld


urlpatterns = [
    ("create-user/",HelloWorld)
]

