from django.db import models
from django.contrib.auth.models import User
from home.models import *
from django.forms import ModelForm

class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    create = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)
    email = models.EmailField()
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    def __str__(self):
        return self.user.username
    def get_price(self):
        total = sum(i.price for i in self.order_item.all())
        return total


class ItemOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE,related_name='order_item')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    variant = models.ForeignKey(Variants, on_delete=models.CASCADE,null=True,blank=True)
    quantity = models.PositiveIntegerField()
    def __str__(self):
        return self.user.username
    def size(self):
        return self.variant.size_variant.name
    def color(self):
        return self.variant.color_variant.name

    @property
    def price(self):
        if self.product.status != 'None':
            #return 3000
            return self.variant.total_price * self.quantity
        else:
            return self.product.total_price * self.quantity

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['email',
                  'f_name',
                  'l_name',
                  'address',
                  ]

