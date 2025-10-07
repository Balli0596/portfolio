from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages

def home(request):
    """
    Handles the homepage and contact form POST request.
    """
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        print("POST received:", name, email, phone)

        # Simple validation
        if len(name) < 2 or len(email) < 3 or len(phone) < 10:
            messages.error(request, "Please fill the form correctly")
        else:
            # Save to database
            Contact.objects.create(name=name, email=email, phone=phone)
            messages.success(request, "Your message has been sent successfully!")
            return redirect('home')  # Avoid duplicate submission on refresh

    return render(request, 'home.html')
