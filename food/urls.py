from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('item/', views.item, name='item'),
    path('order/', views.order, name='order'),
    path('cart/', views.cart, name='cart'),
]

