from django.shortcuts import render, redirect
from .models import *
from cart.models import *
from django.contrib import messages

from django.http import HttpResponse

def order_detail(request, order_id):
    order = Order.objects.get(id=order_id)
    return render(request, 'order/order.html', {'order': order})
@login_required(login_url='accounts:login')
def order_create(request):
    if request.method == 'POST':
        print(request.POST)

        form = OrderForm(request.POST)
        if form.is_valid():


            data = form.cleaned_data
            order = Order.objects.create(user_id=request.user.id, email=data['email'], f_name=data['f_name'],
                                         l_name=data['l_name'], address=data['address'])
            cart = Cart.objects.filter(user_id=request.user.id)
            for c in cart:
                ItemOrder.objects.create(order_id=order.id, user_id=request.user.id, product_id=c.product.id,
                                         variant_id=c.variant_id, quantity=c.quantity)
            # Cart.objects.filter(user_id=request.user.id).delete()
            messages.success(request, 'order is ok', 'success')
            return redirect('order:order_detail', order.id)
    else:
        return HttpResponse("<h1>method get</h1>")