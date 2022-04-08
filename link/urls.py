from django.urls import path

from link.views import contact

urlpatterns = [
    path('contact', contact, name='contact_url'),
    ]
