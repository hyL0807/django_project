"""djangogame URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
import main.views
import main.services

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main.views.index, name='index'),
    path('page1/', main.views.page1, name='page1'),
    path('page2/', main.views.page2, name='page2'),
    
    #채팅 테스트
    path('page3/', main.views.page3, name='page3'),
    # path('process/', main.views.process_message, name='process_message')
    path('process/', main.services.process_message, name='process_message') # view.py 대신 services.py로
]
