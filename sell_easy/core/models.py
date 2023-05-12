from django.db import models

# Create your models here.

class Products(models.Model):
    #owner
    name = models.CharField(max_length=100)
    desc = models.TextField()
    price = models.DecimalField(decimal_places=2,max_digits=10)
    is_available = models.BooleanField(default=True)
    date_added =  models.DateField(auto_now_add=True)
    rating = models.IntegerField()
    