from django.shortcuts import render
from .models import Contact
from django.contrib import messages

def home(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        if len(name) < 2 or len(email) < 3 or len(phone) < 10:
            messages.error(request, "Please fill the form correctly")
        else:
            Contact.objects.create(name=name, email=email, phone=phone)
            messages.success(request, "Your message has been sent")
    
    return render(request, 'home.html')
