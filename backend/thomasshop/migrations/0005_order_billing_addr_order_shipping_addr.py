# Generated by Django 4.0.1 on 2022-02-07 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thomasshop', '0004_rename_basketitems_basketitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='billing_addr',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='order',
            name='shipping_addr',
            field=models.TextField(default=''),
        ),
    ]