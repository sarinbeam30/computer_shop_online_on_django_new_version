from django.urls import path

from . import views

app_name = 'cp_shop_online_app'
urlpatterns = [
    path('', views.main_page, name='main_page'),
]