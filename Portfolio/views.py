from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm

# Create your views here.

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save form data or handle as needed
            messages.success(request, 'Your message has been successfully submitted.')
            return redirect('contact')  # Redirect back to contact page
    else:
        form = ContactForm()
    return render(request, 'portfolio/contact.html', {'form': form})


def home(request):
    return render(request, 'portfolio/home.html')