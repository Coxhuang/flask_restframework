# -*- coding: utf-8 -*-
"""
@Time ： 2020/5/15 15:17
@Auth ： Minhang
@File ：app_init.py
@IDE  ：PyCharm
"""
import config as settings
from data.global_enums import MysqlEnum

class MyConfig(object):

    def __init__(self):
        self.__project_config_data_init()
    
    def __project_config_data_init(self):
        """
        根据环境, 生成对应的数据 
        :return: None 
        """
        
        evn = settings.EVN
        if evn == "dev": # 开发环境 
            self.mysql_username = MysqlEnum.USERNAME_DEV.value
            self.mysql_password = MysqlEnum.PASSWORD_DEV.value
            self.mysql_host = MysqlEnum.HOST_DEV.value
            self.mysql_port = MysqlEnum.PORT_DEV.value
            self.mysql_name = MysqlEnum.NAME_DEV.value

        elif evn == "prod": # 生产环境 
            self.mysql_username = MysqlEnum.USERNAME_PORD.value
            self.mysql_password = MysqlEnum.PASSWORD_PROD.value
            self.mysql_host = MysqlEnum.HOST_PROD.value
            self.mysql_port = MysqlEnum.PORT_PROD.value
            self.mysql_name = MysqlEnum.NAME_PROD.value
        
        else: # 测试环境 
            self.mysql_username = MysqlEnum.USERNAME_TEST.value
            self.mysql_password = MysqlEnum.PASSWORD_PROD.value
            self.mysql_host = MysqlEnum.HOST_PROD.value
            self.mysql_port = MysqlEnum.PORT_PROD.value
            self.mysql_name = MysqlEnum.NAME_PROD.value
        
        return None

    def set_mysql_config(self,app):
        app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://{}:{}@{}:{}/{}".format(
            self.mysql_username,
            self.mysql_password,
            self.mysql_host,
            self.mysql_port,
            self.mysql_name
        )

        # 配置flask配置对象中键：SQLALCHEMY_COMMIT_TEARDOWN,设置为True,应用会自动在每次请求结束后提交数据库中变动

        app.config['SQLALCHEMY_COMMIT_TEARDOWN'] = True
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
        app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

        return None


config_obj = MyConfig()