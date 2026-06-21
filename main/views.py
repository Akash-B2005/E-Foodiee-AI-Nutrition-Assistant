from django.shortcuts import render, get_object_or_404
from .models import Restaurant, MenuItem

def home(request):
    restaurants = Restaurant.objects.all()
    offers = Restaurant.objects.exclude(offer='')
    return render(request, 'home.html', {'restaurants': restaurants, 'offers': offers})

def restaurant_menu(request, id):
    restaurant = get_object_or_404(Restaurant, id=id)
    items = MenuItem.objects.filter(restaurant=restaurant)
    return render(request, 'menu.html', {'restaurant': restaurant, 'items': items})

def contact(request):
    return render(request, 'contact.html')
