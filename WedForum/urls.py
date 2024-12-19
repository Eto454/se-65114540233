from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_login, name='login'),  # หน้า Login
    path('chat/', views.chat_page, name='chat_page'),  # หน้า Chat
]
