from django.shortcuts import render
from django.http import HttpResponse
from .models import All_notebook_product_page
from django.shortcuts import get_object_or_404

def main_page(request):
    all_notebook_product_page = All_notebook_product_page.objects.all()
    context = {'all_notebook_product_page': all_notebook_product_page}
    return render(request, 'web_page/main.html', context)

def product_detail_page(request,slug):
    text = "products/" +slug + "/"
    # print("TEXT : " + text)
    # print("SLUG : " + slug)

    product = get_object_or_404(All_notebook_product_page, slug=text)
    return render(request, 'web_page/product-detail-page.html',{'product': product})


# products/apple-macbook-120-m312ghz8gb256gbspace-gray-tha/

# products/dell-notebook-xps-9380-w56701606thw10-silver/