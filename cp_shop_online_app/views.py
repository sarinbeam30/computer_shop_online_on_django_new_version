from django.shortcuts import render
from django.http import HttpResponse
from .models import All_notebook_product_page
from django.shortcuts import get_object_or_404

def all_notebook_product_page(request):
    all_notebook_product_page = All_notebook_product_page.objects.all()
    product_count = All_notebook_product_page.objects.count()
    context = {'all_notebook_product_page': all_notebook_product_page, 'product_count': product_count}
    return render(request, 'web_page/all-notebook-product-page.html', context)

def main_page(request):
    all_notebook_product_page = All_notebook_product_page.objects.all()
    golden_product =  All_notebook_product_page.objects.all()[:3]
    context = {'all_notebook_product_page': all_notebook_product_page, 'golden_product':golden_product}
    return render(request, 'web_page/main.html', context)

def promotion_page(request):
    all_notebook_product_page = All_notebook_product_page.objects.all()
    product_count = All_notebook_product_page.objects.count()
    context = {'all_notebook_product_page': all_notebook_product_page, 'product_count': product_count}
    return render(request, 'web_page/promotion-page.html', context)

def product_detail_page(request,slug):
    # SLUG
    text = "products/" +slug + "/"
    # print("TEXT : " + text)
    # print("SLUG : " + slug)
    product = get_object_or_404(All_notebook_product_page, slug=text)

    all_notebook_product_page = All_notebook_product_page.objects.all()
    context = {'all_notebook_product_page': all_notebook_product_page, 'product':product}
    return render(request, 'web_page/product-detail-page.html', context)


# products/apple-macbook-120-m312ghz8gb256gbspace-gray-tha/
# products/dell-notebook-xps-9380-w56701606thw10-silver/