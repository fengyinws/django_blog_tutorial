from django.urls import path
# 引入views.py
from . import views

app_name = 'static_images'

urlpatterns = [
    # 动画页面
    path('wyp/', views.love_images, name='auto_images'),
    path('tree/', views.love_tree, name='love_tree'),
]
