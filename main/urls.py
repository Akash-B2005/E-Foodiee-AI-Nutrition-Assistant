from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('restaurant/<int:id>/', views.restaurant_menu, name='restaurant_menu'),
    path('contact/', views.contact, name='contact'),
]
