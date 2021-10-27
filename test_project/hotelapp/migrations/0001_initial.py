# Generated by Django 3.2.8 on 2021-10-27 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RestaurantModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('valuation', models.CharField(max_length=30)),
                ('address', models.TextField()),
            ],
        ),
    ]
