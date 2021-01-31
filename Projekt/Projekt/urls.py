"""Projekt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from anglomat import views

urlpatterns = [
    path('verbs', views.VerbList.as_view, name =views.VerbList.name),
    path('numerals', views.NumeralList.as_view, name =views.NumeralList.name),
    path('users/', views.UserList.as_view(), name =views.UserList.name),
    path('users/<int:pk>/', views.UserDetail.as_view(), name =views.UserDetail.name),
    path('', views.ApiRoot.as_view(), name=views.ApiRoot.name),
]

#urlpatterns += [ path('api-auth/', include('rest_framework.urls')), ]
