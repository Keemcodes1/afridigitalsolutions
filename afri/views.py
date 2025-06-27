from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')
def about_us(request):
    return render(request, 'about-us.html')
def contact_us(request):
    return render(request, 'contact-us.html')
def our_services(request):
    return render(request, 'our-services.html')

