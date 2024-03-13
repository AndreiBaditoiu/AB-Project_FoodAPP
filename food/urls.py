from . import views
from django.urls import path

urlpatterns = [
    # /food/
    path('', views.index, name='index'),
    # /food/1 (id 1)--exemplu
    path('<int:item_id>/', views.detail, name='detail'),
    path('item/', views.item, name='item'),
]
