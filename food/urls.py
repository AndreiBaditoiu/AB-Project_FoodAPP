from . import views
from django.urls import path

# namespacing
app_name = 'food'
urlpatterns = [
    # /food/
    path('', views.index, name='index'),
    # /food/1 (id 1)--exemplu
    path('<int:item_id>/', views.detail, name='detail'),
    path('item/', views.item, name='item'),
    # add items
    path('add/', views.create_item, name='create_item'),
]
