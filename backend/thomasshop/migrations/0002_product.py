# Generated by Django 4.0.1 on 2022-01-24 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thomasshop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('description', models.TextField()),
            ],
        ),
    ]
