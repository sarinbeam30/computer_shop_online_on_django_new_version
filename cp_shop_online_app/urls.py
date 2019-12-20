from django.urls import path
from django.contrib import admin
from . import views

app_name = 'cp_shop_online_app'
urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('all_notebook_product_page/', views.all_notebook_product_page, name='all_notebook_product_page'),
    path('promotion_page/', views.promotion_page, name='promotion_page'),

    path('products/<slug:slug>/', views.product_detail_page, name='product_detail_page'),
    path('promotion_page/products/<slug:slug>/', views.product_detail_page, name='product_detail_page'),
    path('all_notebook_product_page/products/<slug:slug>/', views.product_detail_page, name='product_detail_page'),
]