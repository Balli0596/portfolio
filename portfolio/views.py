from django.shortcuts import render, redirect
from django.http import HttpResponse    
from base.models import Contact
from django.contrib import messages 


# def home(request):
#     return render(request, 'home.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        print(name, email, phone)

        # Basic validation
        if len(name) < 2 or len(email) < 3 or len(phone) < 10:
            messages.error(request, "Please fill the form correctly.")
        else:
            contact = Contact(name=name, email=email, phone=phone)
            contact.save()
            messages.success(request, "Your message has been sent successfully!")
            return redirect('home')  # Redirect after successful POST

    # Optional: to display all contacts (for admin/testing only)
    all_contacts = Contact.objects.all()
    return render(request, 'home.html', {'contacts': all_contacts})
