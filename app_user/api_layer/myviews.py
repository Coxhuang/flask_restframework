# -*- coding: utf-8 -*-
"""
@Time ： 2020/5/14 19:10
@Auth ： Minhang
@File ：views.py
@IDE  ：PyCharm
"""

from flask_restplus import Resource
from flask import Blueprint

class HelloWorld(Resource):

    def get(self):
        return {'hello': 'eeee'}
