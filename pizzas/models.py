from django.db import models

# Create your models here.
""" Define a model Pizza with a field called name, 
which will hold name values, such as Hawaiian and Meat Lovers. """

class Pizza(models.Model):
    """Represent a pizza that can be ordered from the pizzeria."""
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """ Return pizza name """
        return self.text



""" 
Define a model called Topping with fields called pizza and name. 
The pizza field should be a foreign key to Pizza, 
and name should be able to hold values such as pineapple, 
Canadian bacon, and sausage.
"""

class Toppings(models.Model):
    """A topping that can be added to a pizza."""
    pizza = models.ForeignKey(pizza, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """ Return a string representing the model """
        return self.name

