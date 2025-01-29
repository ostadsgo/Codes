from django.urls import path,re_path
from . import views
app_name= 'order'
urlpatterns = [
    path('<int:order_id>/',views.order_detail,name='order_detail'),
    path('create/',views.order_create,name='order_create'),
]