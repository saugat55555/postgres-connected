from django.shortcuts import render
from .models import Destination

# Create your views here.

def index(request):
    des1 = Destination()
    des1.name = "New york"
    des1.img = "destination_1.jpg"
    des1.descrip = "hello in the name of floor"
    des1.price = 3444
    des1.offer = False
    
    des2 = Destination()
    des2.name = "Londan"
    des2.img = "destination_2.jpg"
    des2.descrip = "hello in the name of floor"
    des2.price = 3444
    des2.offer = False
    
    des3 = Destination()
    des3.name = "Delhi"
    des3.img = "destination_3.jpg"
    des3.descrip = "hello in the name of floor"
    des3.price = 3444
    des3.offer = True

    des4 = Destination()
    des4.name = "Goa"
    des4.img = "destination_4.jpg"
    des4.descrip = "hello in the name of floor"
    des4.price = 3444
    des4.offer = True

    des5 = Destination()
    des5.name = "Pokhara"
    des5.img = "destination_5.jpg"
    des5.descrip = "hello in the name of floor"
    des5.price = 3234
    des5.offer = True

    des6 = Destination()
    des6.name = "Kathmandu"
    des6.img = "destination_6.jpg"
    des6.descrip = "hedkd fldk dsa"
    des6.price = 44532
    des6.offer = False

    dest = [des1, des2, des3, des4, des5, des6]

    return render(request, 'index.html',{'destion':dest})