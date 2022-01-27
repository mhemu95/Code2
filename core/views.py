from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Brand
from .forms import ProductForm 



def home(request):
    products = Product.objects.all()

    context = {
        'products': products
    }
    return render(request, 'front/home.html', context)


def singlePost(request, slug):
    single = get_object_or_404(Product, prod_slug=slug)

    context = {
        'single': single
    }

    return render(request, 'front/single.html', context)


def about(request):

    return render(request, 'front/about.html')


## category
def brand(request):
    brand = Brand.objects.filter(brand_status=True)

    context={
        'brand':brand,
    }

    return render(request, 'front/brands.html', context)


### add a product 
def addProduct(request):
    
    brand = Brand.objects.all()

    context = {
        "brand":brand
    }

    if request.method == 'POST':
        name = request.POST['name']
        slug = request.POST['slug']
        price = request.POST['price']
        tag = request.POST['tag']
        details = request.POST['details']
        img = request.FILES['image']
        if len(request.POST['offer']) != 0:
            offer = request.POST['offer']
            o = Product(offer_price=offer)
            o.save()

        p = Product.objects.create(prod_name=name, prod_slug=slug, prod_price=price, prod_tag=tag, prod_details=details, prod_img=img)
        p.save()
        return redirect('home')
    
    return render(request, 'front/create.html', context)


def collections(request, slug):
    prods = Product.objects.filter(brands__brand_slug=slug)

    context = {
       'prods': prods,
    }

    return render(request, 'front/collection.html', context)