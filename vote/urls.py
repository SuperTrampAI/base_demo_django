# -*- coding: utf-8 -*-
# @Time    : 2020/3/8 18:14
# @Author  : Marko Li 'lxh800109@gmail.com'
# @Site    : 
# @File    : urls.py
# @Software: PyCharm
# __create_data__=2020/3/8 18:14
# @Description: add Description
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from vote import views

urlpatterns = [
    path('teachers/', views.show_teachers, name='teachers'),
    path('subject/', views.show_subjects, name='subjects'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('captcha/', views.get_captcha, name='captcha'),
    path('logout/', views.logout, name='logout'),
    path('teachers_data/', views.get_teachers_data),
    path('echarts_teacher/', views.echarts_teacher),
    url(r'^export/xls/$', views.export_teachers_xls, name='export_teachers_xls'),
]
