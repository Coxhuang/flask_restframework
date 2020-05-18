# -*- coding: utf-8 -*-
"""
@Time ： 2020/5/15 14:03
@Auth ： Minhang
@File ：models.py
@IDE  ：PyCharm
"""

from utils.common.dbs.db import db as models

class UserProfile(models.Model):

    __tablename__ = 'app_user_userprofile' # 表名

    id = models.Column( # id
        models.Integer, # 整型
        primary_key=True, # 主键
        autoincrement=True, # 自增
    )
    username = models.Column( # 用户名
        models.String(150), # 字符串
        unique=True, # 唯一
    )
    password = models.Column(  # 密码
        models.String(150), # 字符串
    )
    email = models.Column(  # 邮箱
        models.String(150), # 字符串
        unique=True,
    )
    role = models.Column(  # 角色
        models.Integer, # 整型
        default = 2, # 默认值为2
    )
    phone = models.Column(  # 手机号码
        models.String(32),
        default="",
    )
    avatar = models.Column(  # 头像
        models.TEXT,
        default="",
    )

    def get_role_choices(self):
        """
        获取role字段含义
        :return: string
        """
        role_choice = {
            0:"超级管理员",
            1:"管理员",
            2:"普通用户",
        }

        return role_choice["role"]
