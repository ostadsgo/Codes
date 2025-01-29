from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from ckeditor_uploader.fields import RichTextUploadingField
from taggit.managers import TaggableManager
from django import forms
from django.db.models import Avg


class Category(models.Model):
    sub_category = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='sub')
    sub_cat = models.BooleanField(default=False)
    name = models.CharField(max_length=200)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    slug = models.SlugField(allow_unicode=True, unique=True, null=True, blank=True)
    image = models.ImageField(upload_to='Category', null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home:category', args=[self.slug, self.id])


class product(models.Model):
    VARIANT = (
        ('None', 'none'),
        ('Size', 'size'),
        ('Color', 'color'),
    )
    Category = models.ManyToManyField(Category, blank=True)
    name = models.CharField(max_length=100)
    mount = models.PositiveIntegerField()
    unit_price = models.PositiveIntegerField()
    discounting = models.PositiveIntegerField(blank=True, null=True)
    total_price = models.PositiveIntegerField(blank=True, null=True)
    information = RichTextUploadingField(blank=True, null=True)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    tags = TaggableManager(blank=True)
    available = models.BooleanField(default=True)
    status = models.CharField(max_length=150, blank=True, null=True, choices=VARIANT)
    image = models.ImageField(upload_to='product')
    like = models.ManyToManyField(User, blank=True, related_name='product_like')
    total_like = models.IntegerField(default=0)
    unlike = models.ManyToManyField(User, blank=True, related_name='product_unlike')
    total_unlike = models.IntegerField(default=0)

    def average(self):
        data = Comment.objects.filter(is_reply=False, Product=self).aggregate(avg=Avg('rate'))
        star = 0
        if data['avg'] is not None:
            star = round(data['avg'], 1)
        return star

    def total_like(self):
        return self.like.count()

    def total_unlike(self):
        return self.unlike.count()

    def __str__(self):
        return self.name

    @property
    def total_price(self):
        if not self.discounting:
            return self.unit_price
        elif self.discounting:
            total = (self.discounting * self.unit_price) / 100
            return int(self.unit_price - total)
        return self.total_price


class Size(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Variants(models.Model):
    name = models.CharField(max_length=100)
    product_variant = models.ForeignKey(product, on_delete=models.CASCADE, related_name='pro')
    size_variant = models.ForeignKey(Size, on_delete=models.CASCADE, blank=True, null=True)
    color_variant = models.ForeignKey(Color, on_delete=models.CASCADE,blank=True, null=True)
    mount = models.PositiveIntegerField()
    unit_price = models.PositiveIntegerField()
    discounting = models.PositiveIntegerField(blank=True, null=True)
    total_price = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

    @property
    def total_price(self):
        if not self.discounting:
            return self.unit_price
        elif self.discounting:
            total = (self.discounting * self.unit_price) / 100
            return int(self.unit_price - total)
        # return self.total_price
        return 9000


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Product = models.ForeignKey(product, on_delete=models.CASCADE)
    comment = models.TextField()
    rate = models.PositiveIntegerField(default=1)
    create = models.DateTimeField(auto_now_add=True)
    reply = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='comment_reply')
    is_reply = models.BooleanField(False)
    comment_like = models.ManyToManyField(User, blank=True, related_name='com_like')
    total_comment_like = models.PositiveIntegerField(default=0)

    def total_comment_like(self):
        return self.comment_like.count()

    def __str__(self):
        return self.Product.name


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment', 'rate']


class ReplyForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']


class Image(models.Model):
    Product = models.ForeignKey(product, on_delete=models.CASCADE, related_name='PI')
    name = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='image/', blank=True)
