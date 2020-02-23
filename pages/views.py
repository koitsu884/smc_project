from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect

from services.models import Service
from cars.models import Car
from .forms import FeedbackModelForm
from .models import ContactDetail

def index(request):
    # listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    services = Service.objects.filter(display_top=True)
    cars = Car.objects.order_by('-timestamp').all()[:6]

    # context = {
    #     'listings': listings,
    #     'state_choices': state_choices,
    #     'bedroom_choices': bedroom_choices,
    #     'price_choices': price_choices
    # }
    context = {
        'cars': cars,
        'services': services
    }

    return render(request, 'pages/index.html', context)


def contact(request):
    form = FeedbackModelForm(request.POST or None)
    if request.POST:
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully')
            return HttpResponseRedirect('/contact')
        else:
            messages.error(request, 'Failed to send message. Please correct all highlighted errors and try again.')
        

    contact_details = ContactDetail.objects.first()

    context = {
        "form" :form,
        "contact_details": contact_details
    }

    return render(request, 'pages/contact.html', context)
