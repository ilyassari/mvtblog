from django.shortcuts import render, redirect
from django.contrib import messages

from link.models import ContactModel
from link.forms import ContactForm

def contact(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            contact = ContactModel()
            contact.title = cd['title']
            contact.email = cd['email']
            contact.full_name = cd['full_name']
            contact.message = cd['message']
            contact.save()
            form.send_email(contact.title, contact.email, contact.message)
            messages.success(request, 'Mesajınız iletilmiştir.')
            return redirect('home_url')
    elif request.user.is_authenticated:
        initial = {
            'email' : request.user.email,
            'full_name' : request.user.get_full_name()
        }
        form = ContactForm(initial=initial)
    context={
        'form' : form,
    }
    return render(request, 'contact.html', context)
