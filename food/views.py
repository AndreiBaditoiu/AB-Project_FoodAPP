from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import ItemForm
from .models import Item, Order


# Create your views here.


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


class FoodDetail(DetailView):
    model = Item
    template_name = 'food/detail.html'


class CreateItemView(CreateView):
    model = Item
    fields = ['item_name', 'item_desc', 'item_price', 'item_image']
    template_name = 'food/item-form.html'

    def form_valid(self, form):
        form.instance.user_name = self.request.user

        return super().form_valid(form)


class UpdateItemView(UpdateView):
    model = Item
    form_class = ItemForm
    template_name = 'food/item-form.html'
    success_url = reverse_lazy('food:index')


class DeleteItemView(DeleteView):
    model = Item
    template_name = 'food/item-delete.html'
    success_url = reverse_lazy('food:index')


def checkout(request):
    if request.method == "POST":
        items = request.POST.get('items', "")
        name = request.POST.get('name', "")
        email = request.POST.get('email', "")
        address = request.POST.get('address', "")
        city = request.POST.get('city', "")
        state = request.POST.get('state', "")
        zipcode = request.POST.get('zipcode', "")
        total = request.POST.get('total', "")  # new line here
        order = Order(items=items, name=name, email=email, address=address, city=city, state=state, zipcode=zipcode,
                      total=total
                      )
        order.save()

    return render(request, 'food/checkout.html')
