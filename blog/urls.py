from django.urls import path
from . import views


"""Assigning view post_list to root URL"""
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('work/<int:pk>/edit/', views.work_edit, name='work_edit'),
    path('education/<int:pk>/edit/', views.edu_edit, name='edu_edit'),
    path('skills/<int:pk>/edit/', views.skills_edit, name='skills_edit'),
    path('extra/<int:pk>/edit/', views.extra_edit, name='extra_edit'),
]
