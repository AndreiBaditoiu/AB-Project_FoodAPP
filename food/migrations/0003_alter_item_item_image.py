# Generated by Django 5.0.3 on 2024-03-25 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_item_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='https://cookinupastorm.biz/wp-content/uploads/2023/04/EmptyDinnerPlates.jpg', max_length=500),
        ),
    ]
