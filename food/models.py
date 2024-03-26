from django.db import models


# Create your models here.


class Item(models.Model):

    def __str__(self):
        return self.item_name

    # str repr-(afisarea produsului-nume, decriere etc nu dupa id!
    # adaugat "placeholder image"(item_image-CharField pt. ca url contine multe caractere)-->
    # --> Atentie, aceste elemt nu este 'stilizare', este 'informatie' stocata in db( debugging 3,5 hr).
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500, default="https://cookinupastorm.biz/wp-content/uploads/2023/04/EmptyDinnerPlates.jpg")
