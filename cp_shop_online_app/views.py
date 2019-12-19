from django.shortcuts import render
from django.http import HttpResponse


def main_page(request):
    return render(request, 'cp_shop_online_app/main.html')
