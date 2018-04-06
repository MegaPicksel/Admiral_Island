from django.shortcuts import render, redirect
from django import forms
from .tasks import contact_email
from . forms import ContactForm


def home(request):
    return render(request, 'info/home.html')


def about(request):
    return render(request, 'info/about.html')


def admiral_island(request):
    return render(request, 'info/admiral_island.html')


def port_owen(request):
    return render(request, 'info/port_owen.html')


def gallery(request):
    return render(request, 'info/gallery.html')


def thankYou(request):
    return render(request, 'info/thank_you_redirect.html')



# Function allows user to contact website owner via an email
# Using Celery Email Backend to send the email

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Capture information from form, form not being saved to a database, data cleaned in forms.py.
            name = request.POST.get('name')
            message = request.POST.get('message')
            email = request.POST.get('email')
            contact = request.POST.get('contact')

            # Pass the data to tasks.py, from where the email is sent as a Celery task.

            contact_email.delay(name, message, email, contact)
            return redirect('thankYou')
        else:
            raise forms.ValidationError("Something is up, your message has not been sent, please try again.")

    else:
        form = ContactForm()
        return render(request, 'info/email.html', {'form': form})






