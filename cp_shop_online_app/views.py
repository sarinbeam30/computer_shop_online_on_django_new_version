from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import All_notebook_product_page, Order, OrderItem
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import Register_Form, Login_Form
from django.utils import timezone
from django.views.generic import ListView, DetailView, TemplateView


def all_notebook_product_page(request):
    all_notebook_product_page = All_notebook_product_page.objects.all()
    product_count = All_notebook_product_page.objects.count()
    context = {'all_notebook_product_page': all_notebook_product_page,
               'product_count': product_count}
    return render(request, 'web_page/all-notebook-product-page.html', context)


def main_page(request):
    all_notebook_product_page = All_notebook_product_page.objects.all()
    golden_product = All_notebook_product_page.objects.all()[:3]
    context = {'all_notebook_product_page': all_notebook_product_page,
               'golden_product': golden_product}
    return render(request, 'web_page/main.html', context)


def promotion_page(request):
    all_notebook_product_page = All_notebook_product_page.objects.all()
    product_count = All_notebook_product_page.objects.count()
    context = {'all_notebook_product_page': all_notebook_product_page,
               'product_count': product_count}
    return render(request, 'web_page/promotion-page.html', context)


def product_detail_page(request, slug):
    # SLUG
    text = "products/" + slug + "/"
    # print("TEXT : " + text)
    # print("SLUG : " + slug)
    product = get_object_or_404(All_notebook_product_page, slug=text)

    all_notebook_product_page = All_notebook_product_page.objects.all()
    context = {
        'all_notebook_product_page': all_notebook_product_page, 'product': product}
    return render(request, 'web_page/product-detail-page.html', context)


# products/apple-macbook-120-m312ghz8gb256gbspace-gray-tha/
# products/dell-notebook-xps-9380-w56701606thw10-silver/

class HomeView(ListView):
    model = All_notebook_product_page
    # paginate_by = 10
    template_name = "web_page/main.html"
    # queryset = All_notebook_product_page.objects.all()
	# context_object_name ='items'
   

class ItemDetailView(DetailView):
    model = All_notebook_product_page
    template_name = "product-detail-page.html"


def register_page(request):
    if request.method == 'POST':
        form = Register_Form(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('cp_shop_online_app:main_page')
    else:
        form = Register_Form()
    return render(request, 'web_page/register-page.html', {'form': form})


def login_page(request):
    if request.method == 'POST':
        print('MA YOUNG')
        form = Login_Form(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            # print('KO CHECK NOI : ',user)
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('cp_shop_online_app:main_page')
    else:
        form = Login_Form()
    return render(request, 'web_page/login-page.html', {'form': form})


@login_required
def logout_page(request):
    if request.method == 'POST':
        logout(request)
        # print('LOGOUT LEAW NA : ', request)
        return redirect('cp_shop_online_app:main_page')


#  ---------------- CART ----------------------

@login_required
def add_to_cart(request, slug):
    # check if the item is available
    item = get_object_or_404(All_notebook_product_page, slug=slug)
    # chack if the item is in the order
    order_item, created = OrderItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False
    )

    # check if the order item is completed
    order_qs = Order.objects.filter(user=request.user, ordered=False)
   
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "This item quantity was updated.")
            return redirect("cp_shop_online_app:main_page" ,slug = slug)
        else:
            order.items.add(order_item)
            messages.info(request, "This item was added to your cart.")
            return redirect("cp_shop_online_app:main_page" , slug=slug)
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(
            user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request, "This item was added to your cart.")
        return redirect("cp_shop_online_app:main_page", slug=slug)

#------------------- SEARCH -----------------------
#SEARCH
from django.views.generic import ListView
from .models import All_notebook_product_page
from django.db.models import Q, Count

class SearchResultsView(ListView):
    model = All_notebook_product_page
    template_name = 'web_page/search-results-page.html'
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = All_notebook_product_page.objects.filter(
            Q(brand__icontains=query)
        )
        return object_list
    
    def count_queryset(self):
        count = Count(All_notebook_product_page.objects.filter(
            Q(brand__icontains=query)
        ))
        return count


# @login_required
# def remove_from_cart(request, slug):
#     item = get_object_or_404(All_notebook_product_page, slug=slug)
#     order_qs = Order.objects.filter(
#         user=request.user,
#         ordered=False
#     )
#     if order_qs.exists():
#         order = order_qs[0]
#         # check if the order item is in the order
#         if order.items.filter(item__slug=item.slug).exists():
#             order_item = OrderItem.objects.filter(
#                 item=item,
#                 user=request.user,
#                 ordered=False
#             )[0]
#             order.items.remove(order_item)
#             messages.info(request, "This item was removed from your cart.")
#             return redirect("cp_shop_online_app:add-to-cart", slug=slug)
#         else:
#             messages.info(request, "This item was not in your cart")
#             return redirect("cp_shop_online_app:add-to-cart", slug=slug)
#     else:
#         messages.info(request, "You do not have an active order")
#         return redirect("cp_shop_online_app:add-to-cart", slug=slug)


# @login_required
# def remove_single_item_from_cart(request, slug):
#     item = get_object_or_404(All_notebook_product_page, slug=slug)
#     order_qs = Order.objects.filter(
#         user=request.user,
#         ordered=False
#     )
#     if order_qs.exists():
#         order = order_qs[0]
#         # check if the order item is in the order
#         if order.items.filter(item__slug=item.slug).exists():
#             order_item = OrderItem.objects.filter(
#                 item=item,
#                 user=request.user,
#                 ordered=False
#             )[0]
#             if order_item.quantity > 1:
#                 order_item.quantity -= 1
#                 order_item.save()
#             else:
#                 order.items.remove(order_item)
#             messages.info(request, "This item quantity was updated.")
#             return redirect("cp_shop_online_app:add-to-cart", slug=slug)
#         else:
#             messages.info(request, "This item was not in your cart")
#             return redirect("cp_shop_online_app:add-to-cart", slug=slug)
#     else:
#         messages.info(request, "You do not have an active order")
#         return redirect("cp_shop_online_app:add-to-cart", slug=slug)
