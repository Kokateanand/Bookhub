from django.urls import path
from . import views

app_name = 'home'  # This sets the namespace for this app

urlpatterns = [
    path('', views.index, name='home_page'),
   
    path("Contact", views.contact, name='Contact'),
    path("Shop", views.shop, name='Shop'),
    path("About", views.about, name='About'),
    path("privacy_policy", views.privacy_policy, name='privacy_policy'),
    path("terms_of_service", views.terms_of_service, name='terms_of_service')
]
