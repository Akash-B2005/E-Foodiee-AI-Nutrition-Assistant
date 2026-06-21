from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    offer = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='restaurants/', blank=True, null=True)

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='menu_items/', blank=True, null=True)

    def __str__(self):
        return self.name
