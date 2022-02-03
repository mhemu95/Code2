from multiprocessing import context
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Brand, Category
from .forms import ProductForm


# home
def home(request):
    products = Product.objects.all()

    context = {
        'products': products
    }
    return render(request, 'front/home.html', context)


# detail view
def singlePost(request, slug):
    single = get_object_or_404(Product, prod_slug=slug)

    context = {
        'single': single
    }

    return render(request, 'front/single.html', context)


# about site
def about(request):

    return render(request, 'front/about.html')


# car brands
def brand(request):
    brand = Brand.objects.filter(brand_status=True)

    context = {
        'brand': brand,
    }

    return render(request, 'front/brands.html', context)


# product categories
def category(request):
    category = Category.objects.all()

    context = {
        'category': category
    }

    return render(request, 'front/category.html', context)


# products by brand
def collections(request, slug):
    prods = Product.objects.filter(brands__brand_slug=slug)

    context = {
        'prods': prods,
    }

    return render(request, 'front/collection.html', context)


# products by category
def prodByCat(request, slug):
    category = Product.objects.filter(category__category_slug=slug)

    context = {
        'category2': category,
    }

    return render(request, 'front/collection2.html', context)


# search
def search(request):
    query = request.GET['q']
    data = Product.objects.filter(prod_name__icontains = query)

    context = {
        'data': data
    }
    return render(request, 'front/search.html', context)


# add a product CRUD
'''def addProduct(request):

    brand = Brand.objects.all()

    context = {
        "brand": brand
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

        p = Product.objects.create(prod_name=name, prod_slug=slug,
                                   prod_price=price, prod_tag=tag, prod_details=details, prod_img=img)
        p.save()
        return redirect('home')

    return render(request, 'front/create.html', context) ''' 


# add a product by form CRUD 
def addProduct(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("panel:list")

    return render(request, 'front/create.html', {'form': form})


# update a product by form CRUD
def updateProduct(request, slug):
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

        p = Product.objects.create(prod_name=name, prod_slug=slug,
                                   prod_price=price, prod_tag=tag, prod_details=details, prod_img=img)
        p.save()
    
    return render(request, 'back/updateProduct.html')