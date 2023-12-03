from django.urls import path
from .views import start_page

urlpatterns = [
    path('', start_page, name='start_page'),
]