from django.urls import path
from .views import start_page, create_contact, contact_detail, delete_contact, edit_contact
from . import views

urlpatterns = [
    path('', start_page, name='start_page'),
    path('create/', views.create_contact, name='create_contact'),
    path('delete/<int:pk>/', delete_contact, name='delete_contact'),
    path('contacts/<int:pk>/', contact_detail, name='contact_details'),
    path('contact/edit/<int:pk>/', edit_contact, name='edit_contact'),
]