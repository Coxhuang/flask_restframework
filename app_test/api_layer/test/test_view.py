# -*- coding: utf-8 -*-
"""
@Time ： 2020/5/15 11:39
@Auth ： Minhang
@File ：create_user.py
@IDE  ：PyCharm
"""
from flask_restplus import Resource

class MyTest(Resource):

    def get(self):
        return {'MyTest': 'MyTest'}