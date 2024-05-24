from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.


class Item(models.Model):

    def __str__(self):
        return self.item_name

    # str repr-(afisarea produsului-nume, decriere etc nu dupa id!
    # adaugat "placeholder image"(item_image-CharField pt. ca url contine multe caractere)-->
    # --> Atentie, aceste elemt nu este 'stilizare', este 'informatie' stocata in db( debugging 3,5 hr).
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500,
                                  default="https://cookinupastorm.biz/wp-content/uploads/2023/04/EmptyDinnerPlates.jpg")

    def get_absolute_url(self):
        return reverse('food:detail', kwargs={'pk': self.pk})


class Order(models.Model):
    items = models.CharField(max_length=1000)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    address = models.CharField(max_length=1000)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)
    total = models.CharField(max_length=200)
