"""sinto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from OutsouceInspection import views
from django.conf import settings
from django.conf.urls.static import *

urlpatterns = [
     path('admin/', admin.site.urls),
     path('', views.login),
     path('login/', views.login),
     path('login/<int:p_id>/',views.index),
     path('index/', views.index),
     path('Product/', views.Product),
     path('Product_Count/', views.Product_Count),
     path('Location_mn/', views.Location_mn),
     path('Location_sr/', views.Location_sr),
     path('Seller_page/', views.Seller_page),
     path('Seller_export/', views.Seller_export),
     path('Seller_his_page/',views.Seller_his_page),
     path('Custormer_MN/', views.Custormer_MN),
     path('Download/', views.dowload),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

