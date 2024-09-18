from django.db import models

<<<<<<< HEAD

""" 
Define a model Pizza with a field called name, 
which will hold name values, such as Hawaiian and Meat Lovers. 
"""

class Pizza(models.Model):
    """ Represent a pizza that can be ordered from the pizzeria. """
=======
# Create your models here.
""" Define a model Pizza with a field called name, 
which will hold name values, such as Hawaiian and Meat Lovers. """

class Pizza(models.Model):
    """Represent a pizza that can be ordered from the pizzeria."""
>>>>>>> 2f3f196629cff24a4fe148a9e0fe5a3171560a01
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
<<<<<<< HEAD
        """ Return a string representation of the model."""
        return self.name


""" 
Define a model called Topping with
fields called pizza and name. 
=======
        """ Return pizza name """
        return self.text



""" 
Define a model called Topping with fields called pizza and name. 
>>>>>>> 2f3f196629cff24a4fe148a9e0fe5a3171560a01
The pizza field should be a foreign key to Pizza, 
and name should be able to hold values such as pineapple, 
Canadian bacon, and sausage.
"""

<<<<<<< HEAD

class Topping(models.Model):
    """ A topping that can be added to a pizza."""
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
=======
class Toppings(models.Model):
    """A topping that can be added to a pizza."""
    pizza = models.ForeignKey(pizza, on_delete=models.CASCADE)
>>>>>>> 2f3f196629cff24a4fe148a9e0fe5a3171560a01
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
<<<<<<< HEAD
        """ Return a string representation of the model."""
        return self.name
=======
        """ Return a string representing the model """
        return self.name

>>>>>>> 2f3f196629cff24a4fe148a9e0fe5a3171560a01
