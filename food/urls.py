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
    # add items page
    path('add/', views.create_item, name='create_item'),
    # edit items page
    path('update/<int:id>/', views.update_item, name='update_item'),
    #detelet item page
    path('delete/<int:id>/', views.delete_item, name='delete_item'),
]
