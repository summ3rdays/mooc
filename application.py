# -*- coding: utf-8 -*-

from flask import Flask
from flask_peewee.db import Database
from flask_peewee.rest import RestAPI

from models import init_models
from services.pw_api import init_api
from ui.admin import init_admin
import local_settings


def create_app():
    app = Flask(__name__)  # Создаем экземпляр класса Flask-приложения
    app.url_map.strict_slashes = local_settings.TRAILING_SLASH  # Указываем игнорирововать слеша в конце url
    app.config.from_object(local_settings)  # Передаём остальные настройки в приложение
    return app


APP = create_app()  # Инициируем приложение

DB = Database(APP)  # Инициируем работу с БД. Тут же создаюётся таблицы, если их нет в БД.
#init_models(DB)

API = RestAPI(APP)  # Инициируем RestAPI от peewee
init_api(API)

ADMIN = init_admin(APP, DB)  # Инициируем Админку


import ui.root  # Импортируем view для главной страницы


# Api на flask_restful и роуты для API
#from flask_restful import Api

#api = Api(APP)


#from services.product import GetProducts, AddProduct, DeleteProduct, UpdateProduct
#api.add_resource(GetProducts, '/product/get')
#api.add_resource(AddProduct, '/product/add/<int:category_id>')
#api.add_resource(DeleteProduct, '/product/delete/<int:product_id>')
#api.add_resource(UpdateProduct, '/product/update/<int:product_id>')

#from services.categories import AddCategory, GetCategories
#api.add_resource(AddCategory, '/category/add/<string:category_name>')
#api.add_resource(GetCategories, '/category/get')
