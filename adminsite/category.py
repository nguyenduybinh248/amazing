from django.shortcuts import render
from adminsite.models import Category
from django.http import HttpResponse
# Create your views here.


def index(request):
    data = {'categories': Category.objects.all()}
    return render(request, 'category.html', data)


def create(request):
    # category = Category.objects.create(name='phụ kiện', slug='phu-kien')
    category = Category()
    category.name = 'phụ kiện'
    category.slug = 'phu-kien'
    category.save()
    data = {'abc': 'abc'}
    return render(request, 'baseadmin.html', data)