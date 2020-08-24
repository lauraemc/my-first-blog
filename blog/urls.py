﻿from django.urls import path
from . import views


"""Assigning view post_list to root URL"""
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]
