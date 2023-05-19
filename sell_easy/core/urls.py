from django.urls import path
from . import views

urlpatterns = [
    # path('<int:id>', views.index )
    path('products', views.products, name="products"),
    path('products/<int:id>', views.products, name="product"),
    path('stores', views.stores, name="stores"),
    path('stores/<int:id>', views.stores, name="store"),
    path('stores/<int:id>/roducts', views.store_products, name="store_products"),
    path('categories', views.categories, name="categories"),
    path('categories/<int:id>', views.category, name="category"),

]