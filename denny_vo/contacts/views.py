from django.shortcuts import render, get_object_or_404, redirect
from .forms import ContactForm
from .models import Contact
from django.urls import reverse

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

def contact_detail(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    return render(request, 'contacts/contact_detail.html', {'contact': contact})

def delete_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    contact.delete()
    return redirect(reverse('start_page'))