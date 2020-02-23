from django.shortcuts import get_object_or_404, render
from .models import Service

def index(request):
  services = Service.objects.all()

  context = {
    'services': services,
    
  }

  return render(request, 'services/services.html', context)