from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy

from .forms import ItemForm
from .models import Item
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


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


# varianta 2 pt functia de mai sus (optimizata)
# def index(request):
#     item_list = Item.objects.all()
#     context = {
#         'item_list': item_list,
#     }
#     return render(request, 'food/index.html', context)


# search option below
# def get_queryset(self):
#     query = self.request.GET.get("item_name")
#     if query:
#         return Item.objects.filter(
#             item_name__icontains=query)
#     else:
#         return Item.objects.all()


# paginator below
class IndexClassView(ListView):
    model = Item
    template_name = 'food/index.html'
    context_object_name = 'item_list'
    paginate_by = 5

    def get_queryset(self):
        query = self.request.GET.get("item_name")
        if query:
            return Item.objects.filter(
                item_name__icontains=query)
        else:
            return Item.objects.all()


def item(request):
    return HttpResponse("<h1>This is an item view</h1>")


# item var below not in connection with above function!!


# @never_cache
# def detail(request, item_id):
#     item = Item.objects.get(pk=item_id)
#     context = {
#         'item': item,
#
#     }
#     return render(request, 'food/detail.html', context)


class FoodDetail(DetailView):
    model = Item
    template_name = 'food/detail.html'


# def create_item(request):
#     form = ItemForm(request.POST or None)
#
#     if form.is_valid():
#         form.save()
#         return redirect('food:index')
#
#     return render(request, 'food/item-form.html', {'form': form})


class CreateItemView(CreateView):
    model = Item
    fields = ['item_name', 'item_desc', 'item_price', 'item_image']
    template_name = 'food/item-form.html'

    def form_valid(self, form):
        form.instance.user_name = self.request.user

        return super().form_valid(form)


# def update_item(request, id):
#     item = Item.objects.get(id=id)
#     form = ItemForm(request.POST or None, instance=item)
#     if form.is_valid():
#         form.save()
#         return redirect('food:index')
#     return render(request, 'food/item-form.html', {'form': form, 'item': item})
#

class UpdateItemView(UpdateView):
    model = Item
    form_class = ItemForm
    template_name = 'food/item-form.html'
    success_url = reverse_lazy('food:index')


# def delete_item(request, id):
#     item = Item.objects.get(id=id)
#
#     if request.method == 'POST':
#         item.delete()
#         return redirect('food:index')
#     # return to specific page to confirm item deletion by user
#     return render(request, 'food/item-delete.html', {'item': item})


class DeleteItemView(DeleteView):
    model = Item
    template_name = 'food/item-delete.html'
    success_url = reverse_lazy('food:index')

def checkout(request):
    return render(request, 'food/checkout.html')