# -*- coding: utf-8 -*-
"""
@Time ： 2020/5/15 15:19
@Auth ： Minhang
@File ：global_enums.py
@IDE  ：PyCharm
"""
from enum import Enum


class EnumBase(Enum):

    pass

class GlobalEnum(EnumBase):

    pass


class MysqlEnum(EnumBase):
    """MySQL配置文件"""

    USERNAME_DEV = "root" # 开发环境
    PASSWORD_DEV = "root"
    HOST_DEV = "127.0.0.1"
    PORT_DEV = 3006
    NAME_DEV = "flask_db"

    USERNAME_TEST = "root" # 测试环境
    PASSWORD_TEST = "root"
    HOST_TEST = "127.0.0.1"
    PORT_TEST = 3006
    NAME_TEST = "flask_db"

    USERNAME_PROD = "root" # 生产环境
    PASSWORD_PROD = "root"
    HOST_PROD = "127.0.0.1"
    PORT_PROD = 3006
    NAME_PROD = "flask_db"



