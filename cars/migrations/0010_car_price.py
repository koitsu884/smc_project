# Generated by Django 3.0.3 on 2020-02-14 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0009_car_odo'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='price',
            field=models.PositiveIntegerField(default=6000),
            preserve_default=False,
        ),
    ]
