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
from django.urls import path

from anglomat import views

urlpatterns = [
    path('', views.ApiRoot.as_view(), name=views.ApiRoot.name),
    path('klienci/', views.KlientList.as_view(), name=views.KlientList.name),
    path('klienci/<int:pk>', views.KlientDetail.as_view(), name=views.KlientDetail.name),
    path('auta', views.AutoList.as_view(), name=views.AutoList.name),
    path('auta/<int:pk>', views.AutoDetail.as_view(), name=views.AutoDetail.name),
    path('naprawy/', views.NaprawaList.as_view(), name=views.NaprawaList.name),
    path('naprawy/<int:pk>', views.NaprawaDetail.as_view(), name=views.NaprawaDetail.name),
]

# urlpatterns += [ path('api-auth/', include('rest_framework.urls')), ]
