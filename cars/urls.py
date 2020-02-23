from django.urls import path

from . import views

urlpatterns = [
    path('<int:car_id>', views.car_details, name='car_details'),
    path('search', views.search, name='search'),
    path('search', views.search, name='search'),
    path('ajax/load-models/', views.load_models, name='ajax_load_models')
]
