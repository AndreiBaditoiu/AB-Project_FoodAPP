# Generated by Django 5.0.3 on 2024-05-23 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0007_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total',
            field=models.CharField(default='1', max_length=200),
            preserve_default=False,
        ),
    ]
