from multiprocessing import context
from django.shortcuts import render, redirect, get_list_or_404
from core.models import Product


def ProductLIst(request):
    list = Product.objects.all()

    context = {
        'list': list
    }

    return render(request, 'back/list.html', context)

