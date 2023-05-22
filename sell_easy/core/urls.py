from django.urls import path, include
from core.account import views as account_views

from . import views

urlpatterns = [
    path('products', views.products, name="products"),
    path('products/<int:id>', views.products, name="product"),
    path('stores', views.stores, name="stores"),
    path('stores/<int:id>', views.store, name="store"),
    path('stores/<int:id>/roducts', views.store_products, name="store_products"),
    path('categories', views.categories, name="categories"),
    path('categories/<int:id>', views.category, name="category"),

    path('account/', include([
        path('login', account_views.login, name='login'),
        path('signup', account_views.signup, name='signup'),
    ])),

    path('dashboard', account_views.dashboard, name='dashboard')

]