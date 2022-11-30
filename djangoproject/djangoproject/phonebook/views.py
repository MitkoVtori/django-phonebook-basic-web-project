from django.shortcuts import render, redirect

from djangoproject.phonebook.models import Contact


def landing_page(request):
    contacts = Contact.objects.all()
    context = {
        'contacts': contacts
    }
    return render(request, 'phonebook/index.html', context)


def create_contact(requests):
    name = requests.POST.get('name')
    number = requests.POST.get('number')
    contact = Contact(
        name=name,
        number=number
    )
    contact.save()

    return redirect('landing-page')