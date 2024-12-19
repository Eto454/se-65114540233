"""
URL configuration for CommunityForum project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from WedForum import views  # นำเข้า views จาก WedForum

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.user_login, name='login'),  # URL สำหรับหน้า login
    path('', views.user_login, name='home'),  # ทำให้ path ว่างเรียกหน้า login
    path('', include('WedForum.urls')),  # โหลด URL จาก WedForum
]