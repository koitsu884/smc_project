# Generated by Django 3.0.3 on 2020-02-10 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('opening_hour_mon', models.CharField(max_length=20)),
                ('opening_hour_tue', models.CharField(max_length=20)),
                ('opening_hour_wed', models.CharField(max_length=20)),
                ('opening_hour_thu', models.CharField(max_length=20)),
                ('opening_hour_fri', models.CharField(max_length=20)),
                ('opening_hour_sat', models.CharField(max_length=20)),
                ('opening_hour_sun', models.CharField(max_length=20)),
            ],
        ),
    ]
