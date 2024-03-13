from django.shortcuts import render
from django.http import HttpResponse
from .models import Item
# Create your views here.


def index(request):
    item_list = Item.objects.all()
    return HttpResponse(item_list)


def item(request):
    return HttpResponse("<h1>This is an item view</h1>")


def order(request):
    return HttpResponse("<h1>This is an order page</h1>")


def cart(request):
    return HttpResponse("<h1>This is your cart</h1>")
