# Generated by Django 3.0.3 on 2020-02-12 21:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_auto_20200213_1015'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feature',
            name='name_ja',
        ),
        migrations.RemoveField(
            model_name='feature',
            name='name_ko',
        ),
        migrations.RemoveField(
            model_name='feature',
            name='name_zh',
        ),
    ]
