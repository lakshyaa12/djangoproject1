from django.shortcuts import render
from datetime import datetime
from home.models import Contact  
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request, 'index.html')
    #return HttpResponse("this is homepage")

def about(request):
    return render(request, 'about.html')

def service(request):
    return render(request, 'sanitary.html')

def tiles_view(request):
    return render(request, 'tiles.html')

def marbles_view(request):
    return render(request, 'marbles.html')

def sanitary_view(request):
    return render(request, 'sanitary.html')

def contact_view(request):  # Renamed the view function to avoid conflict
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        contact = Contact(name=name, email=email, phone=phone, message=message, date=datetime.today())
        contact.save()
        
        messages.success(request, "Your message has been sent!")
    return render(request, 'contact.html')
