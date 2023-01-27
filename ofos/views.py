from django.shortcuts import render
from ofos.models import FoodModel, ProductModel
# Create your views here.

def home(request):
    sandwiches = FoodModel.objects.all()
    products = ProductModel.objects.all()
    return render(request, 'home.html', {'sandwiches' : sandwiches, 'products' : products})

def aboutus(request):
    return render(request, 'aboutus.html')

def contactus(request):
    return render(request, 'contactus.html')

def faq(request):
    return render(request, 'faq.html')

def add(request):
    cl_name = request.GET['cl_name']
    cl_email = request.GET['cl_email']
    cl_number = int(request.GET['cl_number'])
    cl_subject = request.GET['cl_subject']
    cl_textmessage = request.GET['cl_textmessage']
    return render(request, 'aboutus.html', {
        'cl_name': cl_name, 
        'cl_email': cl_email, 
        'cl_number' : cl_number,
        'cl_subject' : cl_subject,
        'cl_textmessage': cl_textmessage })