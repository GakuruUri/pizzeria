from django.db import models

# Create your models here.
class Toppings(models.Model):
    """ Define Pizza Topic """
    text = modles.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

def __str__(self):
    """ Return pizza name """
    return self.text