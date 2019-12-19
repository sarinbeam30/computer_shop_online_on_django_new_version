from django.urls import path
from django.contrib import admin
from . import views

app_name = 'cp_shop_online_app'
urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('products/<slug:slug>/', views.product_detail_page, name='product_detail_page'),
    
]