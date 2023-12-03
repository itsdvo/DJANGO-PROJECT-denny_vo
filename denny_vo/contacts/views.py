from django.shortcuts import render

# Create your views here.

def start_page(request):
    return render(request, 'contacts/start_page.html')