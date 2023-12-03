from django.urls import path
from .views import start_page, create_contact
from . import views

urlpatterns = [
    path('', start_page, name='start_page'),
    path('create/', views.create_contact, name='create_contact'),
]