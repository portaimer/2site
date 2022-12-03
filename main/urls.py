from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('bani', views.bani, name='bani'),
    path('houses', views.houses, name='houses'),
    path('dom_iz_penobloka', views.dom_iz_penobloka, name='dom_iz_penobloka'),
    path('otdelochnye_raboty', views.otdelochnye_raboty, name='otdelochnye_raboty'),
    path('contact_us', views.contact_us, name='contact_us')
]