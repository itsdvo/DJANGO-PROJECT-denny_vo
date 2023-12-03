from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import Contact

# Create your views here.

def start_page(request):
    contacts = Contact.objects.all()  # Retrieves all contacts from the database
    return render(request, 'contacts/start_page.html', {'contacts': contacts})

def create_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('start_page')
    else:
        form = ContactForm()
    
    return render(request, 'contacts/create_contact.html', {'form': form})