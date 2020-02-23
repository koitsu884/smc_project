from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.core import serializers
from django.http import JsonResponse

from .models import Car, Manufacturer, CarModel
from .forms import CarSearchForm
from .filters import CarFilter
from .choices import BODYTYPE_CHOICES, TRANSMISSION_CHOICES, ENEGY_SOURCE_CHOICES


# Create your views here.
def car_details(request, car_id):
    car = get_object_or_404(Car.objects.prefetch_related('photos'), pk=car_id)

    context = {
        'car': car
    }

    return render(request, 'cars/car.html', context)



def search(request):

    filter = CarFilter(
        request.GET,
        queryset=Car.objects.order_by('-timestamp')
    )

    queryset_list = filter.qs

    paginator = Paginator(queryset_list, 12)
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)

    print(request.GET)

    manufacturer = request.GET.get('model__manufacturer')
    model_name = request.GET.get('model__name')
    model_choices = None
    selected_model = None
    if manufacturer and model_name:
        model_choices = CarModel.objects.filter(manufacturer=manufacturer).order_by('name')
        selected_model = model_name
            # queryset_list = queryset_list.filter(model__manufacturer__exact=manufacturer)

    context = {
        # 'manufacturer_choices': Manufacturer.objects.all(),
        'model_choices': model_choices,
        'selected_model': selected_model,
        # 'enegy_type_choices': ENEGY_SOURCE_CHOICES,
        # 'bodytype_choices': BODYTYPE_CHOICES,
        # 'transmission_choices': TRANSMISSION_CHOICES,
        'cars': paged_cars,
        'form': filter.form
    }

    return render(request, 'cars/search.html', context)


def search_old(request):
    queryset_list = Car.objects.order_by('-timestamp')


    if 'manufacturer' in request.GET:
        manufacturer = request.GET['manufacturer']
        if manufacturer:
            model_choices = CarModel.objects.filter(manufacturer=manufacturer).order_by('name')
            queryset_list = queryset_list.filter(model__manufacturer__exact=manufacturer)

    if 'carmodel' in request.GET:
        carmodel = request.GET['carmodel']
        if carmodel:
            queryset_list = queryset_list.filter(model__exact=carmodel)

    # if 'energy_source' in request.GET:
    #     energy_source = request.GET['energy_source']
    #     if energy_source:
    #         queryset_list = queryset_list.filter(
    #             energy_source__iexact=energy_source)

    # if 'body_type' in request.GET:
    #     body_type = request.GET['body_type']
    #     if body_type:
    #         queryset_list = queryset_list.filter(body_type__iexact=body_type)

    # if 'transmission' in request.GET:
    #     transmission = request.GET['transmission']
    #     if transmission:
    #         queryset_list = queryset_list.filter(transmission__iexact=transmission)

    # if 'odo' in request.GET:
    #     odo = request.GET['odo']
    #     if odo:
    #         queryset_list = queryset_list.filter(odo__lte=odo)

    # if 'year' in request.GET:
    #     year = request.GET['year']
    #     if year:
    #         queryset_list = queryset_list.filter(year__gte=year)

    # if 'price_from' in request.GET:
    #     price_from = request.GET['price_from']
    #     if price_from:
    #         queryset_list = queryset_list.filter(price__gte=price_from)

    # if 'price_to' in request.GET:
    #     price_to = request.GET['price_to']
    #     if price_to:
    #         queryset_list = queryset_list.filter(price__lte=price_to)

    # if 'seats_to' in request.GET:
    #     seats_to = request.GET['seats_to']
    #     if seats_to:
    #         queryset_list = queryset_list.filter(seats__lte=seats_to)

    # if 'seats_from' in request.GET:
    #     seats_from = request.GET['seats_from']
    #     if seats_from:
    #         queryset_list = queryset_list.filter(seats__gte=seats_from)

    paginator = Paginator(queryset_list, 12)
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)


    context = {
        'manufacturer_choices': Manufacturer.objects.all(),
        'model_choices': model_choices if model_choices else None,
        'enegy_type_choices': ENEGY_SOURCE_CHOICES,
        'bodytype_choices': BODYTYPE_CHOICES,
        'transmission_choices': TRANSMISSION_CHOICES,
        'cars': paged_cars,
        'values': request.GET
    }

    return render(request, 'cars/search.html', context)


def load_models(request):
    manufacturer_id = request.GET.get('manufacturer')
    models = CarModel.objects.filter(manufacturer=manufacturer_id).order_by('name')
    return JsonResponse(serializers.serialize('json', models), safe=False)
