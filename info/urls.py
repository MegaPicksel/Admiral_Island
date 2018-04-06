from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('admiral_island/', views.admiral_island, name='admiral_island'),
    path('port_owen/', views.port_owen, name='port_owen'),
    path('gallery/', views.gallery, name='gallery'),
    path('thankyou/', views.thankYou, name='thankYou'),
]