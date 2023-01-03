"""appssa URL Configuration

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
from django.views.generic import TemplateView
from django.urls import path
from . import views


urlpatterns = [
    #non-data
    path('', views.index, name='index'),
    path('sosik', views.sosik, name='sosik'),
    path('iljung', views.iljung, name='iljung'),
    path('yebe', views.yebe, name='yebe'),
    #path('privacy_policy', views.privacy_policy, name='privacy_policy'),
    #data
    #path('data/check_user', views.check_user, name='check_user'),
]