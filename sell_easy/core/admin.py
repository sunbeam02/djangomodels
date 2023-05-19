from django.contrib import admin
from .models import Products, Store, Category, Rating

# Register your models here.
admin.site.register(Products)
admin.site.register(Store)
admin.site.register(Category)
admin.site.register(Rating)
