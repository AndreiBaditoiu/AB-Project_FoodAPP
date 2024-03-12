from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse("<h1>This is the food app homepage.</h1>")


def item(request):
    return HttpResponse("<h1>This is an item view</h1>")


def order(request):
    return HttpResponse("<h1>This is an order page</h1>")


def cart(request):
    return HttpResponse("<h1>This is your cart</h1>")
