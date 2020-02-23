import datetime
import django_filters
from django.utils.translation import ugettext as _

from .models import Car, Manufacturer, CarModel
from .choices import TRANSMISSION_CHOICES, BODYTYPE_CHOICES


class CarFilter(django_filters.FilterSet):
    price__gt = django_filters.NumberFilter(field_name='price', lookup_expr='gt', label='')
    price__lt = django_filters.NumberFilter(field_name='price', lookup_expr='lt', label='')
    year__gt = django_filters.NumberFilter(field_name='year', lookup_expr='gt', label='')
    year__lt = django_filters.NumberFilter(field_name='year', lookup_expr='lt', label='')
    odo__lt = django_filters.NumberFilter(field_name='odo', lookup_expr='lt', label='')
    transmission = django_filters.ChoiceFilter(choices=TRANSMISSION_CHOICES, label='')
    body_type = django_filters.ChoiceFilter(choices=BODYTYPE_CHOICES, label='')
    # body_type = django_filters.ModelChoiceFilter(field_name='body_type', lookup_expr='exact')
    model__manufacturer = django_filters.ModelChoiceFilter(queryset=Manufacturer.objects.all().order_by('name'), label='')
    # model = django_filters.ModelChoiceFilter(queryset=CarModel.objects.all()[:1])
    model__name = django_filters.CharFilter(field_name='model__name', label='')

    class Meta:
        model = Car
        fields = [
            'price__gt', 
            'price__lt', 
            'year__gt',
            'year__lt',
            'transmission', 
            'body_type', 
            'model__name',
            'model__manufacturer', 
        ]
        # fields = {
        #     'price': ['lt', 'gt'],
        #     'transmission': ['exact'],
        #     'body_type': ['exact'],
        #     'model': ['exact'],
        #     'model__manufacturer': ['exact'],
        # }