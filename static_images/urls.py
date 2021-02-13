from django.urls import path
# 引入views.py
from . import views

app_name = 'static_images'

urlpatterns = [
    # 动画页面
    path('auto_images/', views.love_images, name='auto_images'),
]
