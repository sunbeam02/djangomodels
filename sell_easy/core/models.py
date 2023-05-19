from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q
from core.account.models import Profile
from django.core.validators import MaxValueValidator,MinValueValidator


# Create your models here.
class Store(models.Model):
    owner = models.OneToOneField(Profile, on_delete=models.CASCADE)
    tagline = models.CharField(max_length=200)
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        pass


class Category(models.Model):
    #owner
    name = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.name
    


class Products(models.Model):
    #owner
    store = models.ForeignKey(Store,on_delete=models.DO_NOTHING, related_name="products", null=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, related_name="products", null=True)
    name = models.CharField(max_length=100)
    desc = models.TextField()
    price = models.DecimalField(decimal_places=2,max_digits=10)
    is_available = models.BooleanField(default=True)
    date_added =  models.DateField(auto_now_add=True)
   

    def discount(self, discount=20):
        self.price = self.price * (discount/100)
        return self.price
    
    def __str__(self) -> str:
        return f'{self.name}, {self.desc}'
    
    @property
    def num_reviews(self):
        num = self.ratings.count()
        return num
    
    @num_reviews.getter
    def get_num_reviews(self):
        return self.num_reviews
    
    def average_rating(self):
        rating = self.ratings.aggregate(models.Sum('rating'))
        total = rating.get('rating__sum')
        return (total/ self.get_num_reviews) if total is not None and self.get_num_reviews is not None else 0

    


class Rating(models.Model):
    product = models.ForeignKey(Products, related_name="ratings", on_delete=models.CASCADE)
    rating = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0)])
    remark = models.CharField(max_length=200)

    def __str__(self) -> str:
        return f"{self.rating}"

# class Meta:
#     ordering =('name', "-price",)
#     verbose_name = "Products"
#     contraints = [models.CheckConstraint(check=Q('price__gt=120000'), name="price_gt_12000")]




    

    