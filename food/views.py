from django.shortcuts import render
from django.http import HttpResponse
from .models import Item
from django.template import loader


# Create your views here.


# varianta 1
# def index(request):
#     item_list = Item.objects.all()
#     template = loader.get_template('food/index.html')
#     context = {
#         'item_list': item_list,
#
#     }
#     return HttpResponse(template.render(context, request))


# varianta 2 pt functia de mai sus
def index(request):
    item_list = Item.objects.all()
    context = {
        'item_list': item_list,
    }
    return render(request, 'food/index.html', context)


def item(request):
    return HttpResponse("<h1>This is an item view</h1>")


def detail(request, item_id):
    return HttpResponse("This is item no/id: %s" % item_id)
