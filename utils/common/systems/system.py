# -*- coding: utf-8 -*-
"""
@Time ： 2020/5/15 11:08
@Auth ： Minhang
@File ：system.py
@IDE  ：PyCharm
"""
import os

class MySystem(object):

    def __init__(self):
        self.root_path = self.get_project_path() # 获取项目根路径

    def get_project_path(self):
        """
        获取项目根路径
        :return: root_path
        """

        return os.path.dirname(__file__).split("utils")[0]

    def test(self):
        """
        测试
        :return:
        """
        self.get_project_path()

        return None

sys_obj = MySystem()

if __name__ == "__main__":
    sys_obj.test()
