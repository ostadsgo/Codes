from django.shortcuts import render, get_object_or_404
from .models import *
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db.models import Avg
from cart.models import *
from kavenegar import *
from .models import *
from django.db.models import Q
from order.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
import requests
from django.contrib.auth import update_session_auth_hash
from random import randint
import ghasedakpack
from django.contrib.auth.decorators import login_required


def cart_detail(request):
    cart = Cart.objects.filter(user_id=request.user.id)
    user = request.user
    form = OrderForm()
    total = 0
    for p in cart:
        if p.product.status != 'None':
            total += p.variant.total_price * p.quantity
        else:
            total += p.product.total_price * p.quantity
    return render(request, 'cart/cart.html', {'cart': cart, 'total': total, 'form': form,'user':user})


@login_required(login_url='accounts:login')
def add_cart(request, id):
    url = request.META.get('HTTP_REFERER')
    Product = product.objects.get(id=id)
    if Product.status != 'NONE':
        var_id = request.POST.get('select')
        data = Cart.objects.filter(user_id=request.user.id, product_id=id,variant_id=var_id)
        if data:
            check = 'yes'
        else:
            check = 'no'
    else:
        data = Cart.objects.filter(user_id=request.user.id, product_id=id)
        if data:
            check = 'yes'
        else:
            check = 'no'
    if request.method == 'POST':
        form = CartForm(request.POST)
        var_id = request.POST.get('select')
        if form.is_valid():
            info = form.cleaned_data['quantity']
            if check == 'yes':
                if Product.status != 'None':
                    #var_id = request.POST.get('select')
                    shop = Cart.objects.get(user_id=request.user.id, product_id=id, variant_id=var_id)
                else:
                    shop = Cart.objects.get(user_id=request.user.id, product_id=id)
                shop.quantity += info
                shop.save()
            else:
                #var_id = request.POST.get('select')
                Cart.objects.create(user_id=request.user.id, product_id=id, variant_id=var_id, quantity=info)
        return redirect(url)


@login_required(login_url='accounts:login')
def remove_cart(request, id):
    url = request.META.get('HTTP_REFERER')
    Cart.objects.filter(id=id).delete()
    return redirect(url)

# Product =product.objects.id(id)
