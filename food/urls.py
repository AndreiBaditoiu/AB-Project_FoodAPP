from . import views
from django.urls import path


# namespacing
app_name = 'food'
urlpatterns = [
    # /food/
    path('', views.IndexClassView.as_view(), name='index'),
    # /food/1 (id 1)--exemplu
    path('<int:pk>/', views.FoodDetail.as_view(), name='detail'),
    path('item/', views.item, name='item'),
    # add items page
    path('add/', views.CreateItemView.as_view(), name='create_item'),
    # edit items page
    path('update/<int:pk>/', views.UpdateItemView.as_view(), name='update_item'),
    # delete item page
    path('delete/<int:pk>/', views.DeleteItemView.as_view(), name='delete_item'),
]
