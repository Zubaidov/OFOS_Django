from django.shortcuts import render
from ofos.models import FoodModel
# Create your views here.

def home(request):

    food1 = FoodModel()
    food1.offer = False
    food1.name = 'Toast'
    food1.desc = 'Sujuk + Bread + Mayoneez + Ketchup'
    food1.price = 3
    food1.img = 'blog-1.jpg'

    food2 = FoodModel()
    food2.offer = True
    food2.name = 'Toast'
    food2.desc = 'Sujuk + Bread + Mayoneez + Ketchup'
    food2.price = 4
    food2.img = 'blog-2.jpg'

    food3 = FoodModel()
    food3.offer = True
    food3.name = 'Nugets'
    food3.desc = 'Nugets + Bread + Mayoneez + Ketchup'
    food3.price = 3
    food3.img = 'blog-3.jpg'

    food4 = FoodModel()
    food4.offer = True
    food4.name = 'Nugets'
    food4.desc = 'Nugets + Bread + Mayoneez + Ketchup'
    food4.price = 4
    food4.img = 'blog-4.jpg'

    food5 = FoodModel()
    food5.offer = False
    food5.name = 'Nugets'
    food5.desc = 'Nugets + Bread + Mayoneez + Ketchup'
    food5.price = 4
    food5.img = 'blog-5.jpg'

    food6 = FoodModel()
    food6.offer = False
    food6.name = 'Nugets'
    food6.desc = 'Nugets + Bread + Mayoneez + Ketchup'
    food6.price = 4
    food6.img = 'blog-6.jpg'

    dests = [food1, food2, food3, food4, food5, food6]

    return render(request, 'home.html', {'dests' : dests})

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