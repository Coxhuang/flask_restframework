from flask import Flask
from flask_restplus import Api
from init.app_init import config_obj
app = Flask(__name__)
api = Api(app)



def register_url(app):
    """
    注册url
    :param app:
    :return:
    """
    from urls import urlpatterns
    for foo in urlpatterns:
        namespace = foo[0] # 命名卡空间
        app_url = foo[1] # 一级路由
        api_url = foo[2].urlpatterns[0][0] # 二级路由
        app_view = foo[2].urlpatterns[0][1] # 类视图
        if api_url[0] != "/": # 如果二级路由前缀不是以 '/' 开头, 补上 '/'
            api_url = "".join(("/",api_url))
        user_namespace = api.namespace(namespace, path=app_url)  # 一级路由
        user_namespace.add_resource(app_view, api_url) # 二级路由

    return None

def create_app():
    """
    工厂模式创建APP
    """

    register_url(app) # 注册url
    config_obj.set_mysql_config(app)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(
        port=20514,
        debug=True,
    )
