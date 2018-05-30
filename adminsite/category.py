from django.shortcuts import render
from adminsite.models import Category
from django.http import HttpResponse
# Create your views here.


def index(request):
    data = {'categories': Category.objects.all()}
    return render(request, 'category.html', data)


def create(request):
    category = Category.objects.create(name='áo len', slug='ao-len')
    data = {'abc': 'abc'}
    return render(request, 'baseadmin.html', data)