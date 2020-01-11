from django.urls import path
# 引入views.py
from . import views

app_name = 'robot_reply'

urlpatterns = [
    # 通知列表
    path('getreply/', views.get_reply, name='get_reply'),
    # path('update/', views.CommentNoticeUpdateView.as_view(), name='update'),
]
