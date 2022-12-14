"""projects URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from landingpage import views 
# from .views import forms

# from .views import Forms, StudentList, StudentDetail, StudentUpdate, StudentDelete

app_name = "landingpage"
urlpatterns = [
    path('home', views.home, name = 'home'),
    path('resume', views.resume, name = 'resume'),
    # path('forms', Forms.as_view(), name = 'forms'),
    # path('list', StudentList.as_view(), name = 'list'),
    # path('<pk>/detail', StudentDetail.as_view(), name = 'detail'),
    # path('<pk>/update', StudentUpdate.as_view(), name = 'update'),
    # path('<pk>/delete', StudentDelete.as_view(), name = 'delete'),
    
    
    
]
