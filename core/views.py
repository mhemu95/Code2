from multiprocessing import context
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Brand, Category
from .forms import BrandForm, CategoryForm, ProductForm


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
    category = Category.objects.filter(category_status=True)

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
    data = Product.objects.filter(prod_name__icontains=query)

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
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("core:home")

    return render(request, 'front/create.html', {'form': form})


# add a category by form crud
def addCategory(request):
    cform = CategoryForm()
    if request.method == 'POST':
        cform = CategoryForm(request.POST)
        if cform.is_valid():
            cform.save()
            return redirect("core:category")

    return render(request, 'back/Create_Category.html', {'cform': cform})


# add a brand by form crud
def addBrand(request):
    bform = BrandForm()
    if request.method == 'POST':
        bform = BrandForm(request.POST, request.FILES)
        if bform.is_valid():
            bform.save()
            return redirect('core:brand')

    return render(request, 'back/Create_Brand.html', {'bform': bform})


# update a product by form CRUD
def updateProduct(request, slug):
    prod = Product.objects.get(prod_slug=slug)
    form = ProductForm(instance=prod)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=prod)
        if form.is_valid():
            form.save()
            return redirect('core:home')

    return render(request, 'back/updateProduct.html', {'prod':prod, 'form':form})

# update a category by form CRUD
def updateCategory(request, slug):
    category = Category.objects.get(category_slug=slug)
    cform = CategoryForm(instance=category)
    if request.method == 'POST':
        cform = CategoryForm(request.POST, instance=category)
        if cform.is_valid():
            cform.save()
            return redirect('core:category')

    return render(request, 'back/update_category.html', {'category':category, 'cform':cform})


# update a brand by form CRUD
def updateBrand(request, slug):
    brand = Brand.objects.get(brand_slug=slug)
    bform = BrandForm(instance=brand)
    if request.method == 'POST':
        bform = BrandForm(request.POST, request.FILES, instance=brand)
        if bform.is_valid():
            bform.save()
            return redirect('core:brand')

    return render(request, 'back/update_brand.html', {'brand':brand, 'bform':bform}) 


# Delete a product CRUD
def deleteProduct(request, slug):
    obj = Product.objects.get(prod_slug=slug)
    obj2 = 'Product'

    if request.method == 'POST':
        obj.delete()
        return redirect('core:home')

    return render(request, 'back/delete.html', {'obj':obj, 'obj2':obj2})


# delete a category
def deleteCategory(request, slug):
    obj = Category.objects.get(category_slug=slug)
    obj2 = 'Category'

    if request.method == 'POST':
        obj.delete()
        return redirect('core:category')

    return render(request, 'back/delete.html', {'obj':obj, 'obj2':obj2})


# delete a category
def deleteBrand(request, slug):
    obj = Brand.objects.get(brand_slug=slug)
    obj2 = 'Brand'

    if request.method == 'POST':
        obj.delete()
        return redirect('core:category')

    return render(request, 'back/delete.html', {'obj':obj, 'obj2':obj2})
