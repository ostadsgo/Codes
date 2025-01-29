from django.shortcuts import render, get_object_or_404
from .models import *
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db.models import Avg
from cart.models import *
from kavenegar import *
from .models import *
from django.db.models import Q
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
import requests
from django.contrib.auth import update_session_auth_hash
from random import randint
import ghasedakpack
from django.contrib.auth.decorators import login_required


def home(request):
    category = Category.objects.filter(sub_cat=False)
    return render(request, 'home/home.html', {'category': category})


def all_product(request, slug=None, id=None):
    form = SearchForm()
    products = product.objects.all()
    category = Category.objects.filter(sub_cat=False)
    if 'search' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            data = form.cleaned_data['search']
            products = products.filter(Q(name__contains=data))
    if slug and id:
        data = get_object_or_404(Category, slug=slug, id=id)
        products = products.filter(Category=data)
    return render(request, 'home/product.html', {'products': products, 'category': category, 'form': form})


def product_detail(request, id):
    Product = get_object_or_404(product, id=id)
    images = Image.objects.filter(Product_id=id)
    reply_form = ReplyForm()
    cart_form = CartForm()
    comment_form = CommentForm()
    comment = Comment.objects.filter(Product_id=id, is_reply=False)
    similar = Product.tags.similar_objects()[:3]
    is_like = False
    if Product.like.filter(id=request.user.id).exists():
        is_like = True
    is_unlike = False
    if Product.unlike.filter(id=request.user.id).exists():
        is_unlike = True
    if Product.status != 'None':
        if request.method == 'POST':
            variant = Variants.objects.filter(product_variant_id=id)
            var_id = request.POST.get('select')
          #  var_id = 1
            Variantso = Variants.objects.get(id=var_id)
         #   Variantso = 3
        else:
            variant = Variants.objects.filter(product_variant_id=id)
            Variantso = Variants.objects.get(id=1)
        context = {'product': Product, 'variant': variant, 'variants': Variantso, 'similar': similar,
                   'is_like': is_like, 'is_unlike': is_unlike, 'comment_form': comment_form, 'comment': comment,
                   'reply_form': reply_form, 'images': images, 'cart_form': cart_form}
        return render(request, 'home/detail.html', context)
    else:
        return render(request, 'home/detail.html',
                      {'product': Product, 'similar': similar, 'is_like': is_like, 'is_unlike': is_unlike,
                       'comment_form': comment_form, 'comment': comment, 'reply_form': reply_form, 'images': images,
                       'cart_form': cart_form})


def product_like(request, id):
    url = request.META.get('HTTP_REFERER')
    Product = get_object_or_404(product, id=id)
    is_like = False
    if Product.like.filter(id=request.user.id).exists():
        Product.like.remove(request.user)
        is_like = False
        messages.success(request, 'remove', 'success')
    else:
        Product.like.add(request.user)
        is_like = True
        messages.success(request, 'تشکر از لایک شما', 'success')
    return redirect(url)


def product_unlike(request, id):
    url = request.META.get('HTTP_REFERER')
    Product = get_object_or_404(product, id=id)
    Product.unlike.add(request.user)
    messages.success(request, 'mamnon', 'success')
    return redirect(url)


def product_comment(request, id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            data = comment_form.cleaned_data
            Comment.objects.create(comment=data['comment'], rate=data['rate'], user_id=request.user.id, Product_id=id,
                                   is_reply=False)
            messages.success(request, 'تشکر از شما', 'dark')
            return redirect(url)


def product_reply(request, id, comment_id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        reply_form = ReplyForm(request.POST)
        if reply_form.is_valid():
            data = reply_form.cleaned_data
            Comment.objects.create(comment=data['comment'], user_id=request.user.id, Product_id=id, reply_id=comment_id,
                                   is_reply=True)
            messages.success(request, 'تشکر از reply شما', 'dark')
            return redirect(url)


def comment_like(request, id):
    url = request.META.get('HTTP_REFERER')
    comment = Comment.objects.get(id=id)
    if comment.comment_like.filter(id=request.user.id).exists():
        comment.comment_like.remove(request.user)
    else:
        comment.comment_like.add(request.user)
        messages.success(request, 'تشکر از like comment شما', 'warning')
    return redirect(url)


def product_search(request):
    products = product.objects.all()
    #   if request == 'POST':
    form = SearchForm(request.POST)
    if form.is_valid():
        data = form.cleaned_data['search']
        if data.isdigit():
            products = products.filter(Q(discounting__exact=data) | Q(unit_price__exact=data))
        else:
            products = products.filter(Q(name__contains=data))

        return render(request, 'home/product.html', {'products': products, 'form': form})
