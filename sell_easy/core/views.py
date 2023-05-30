from django.shortcuts import render
from django.http import HttpResponse
from .models import Products, Store, Category
# Create your views here.

# def index(request, id):
#     print(request.method, id)
#     return HttpResponse("Homepage")

# def web_page(products):
#     page = '<ul>'
#     for product in products:
#         page += f"<li><h1>{product['name']}</h1><h2>{product['desc']}</h2><p>{product['price']}</p></li>"
#     page += '</ul>'
#     return page

# def store_page(stores):
#     page = '<ul>'
#     for store in stores:
#         page += f"<li><h1>{store['name']}</h1><h2>{store['tagline']}</h2><p>{store.owner.username}, Welcome</p></li>"
#     page += '</ul>'
#     return page

def home(request):
    products = Products.objects.all()
    best_selling_products = products
    products =products[:8]
    categories = Category.objects.all()[:4]
    stores = Store.objects.all()[:4]

    context={
        'products':products,
        'categories':categories,
        'stores':stores,
        'best_selling_products':best_selling_products
    }

    return render(request, 'core/home.html', context)

def products(request):
    products = Products.objects.all()
    categories = Category.objects.all()
    context = {'products':products, 'categories':categories}
    return render(request, 'core/products.html', context)

def product(request, id):
    products = Products.objects.get(id=id)
    related_products = Products.objects.filter(category=product.category).exclude(id=product.id)
    return render(request, 'core/details.html', {'product':product, 'related_products':related_products})
    
    

def stores(request):
    stores = Store.objects.all()
    # return HttpResponse(store_page(stores))

def store(request, id):
    pass

def store_products(request, id):
    pass

def categories(request):
    pass

def category(request):
    pass



