"""
URL configuration for SecondProject project.

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
from django.urls import path
from FirstApp import views
from SecondApp import views as v1;

urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome/', views.wishes),
    path('hello/', views.hello),
    path('students1/',v1.students1),
    path('students2/',v1.students2),
    path('wishes2/', views.wishes2),
    path('datetime/', views.datetimefunction),
    path('studdatetime/', views.student_datetime),



]
