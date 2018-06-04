from django.shortcuts import render
from adminsite.models import Category
from django.http import HttpResponse
from django.http import JsonResponse
from django.utils.text import slugify
from django.contrib.humanize.templatetags.humanize import naturaltime
from django.core import serializers
# Create your views here.


def _get_unique_slug(self):
    slug = slugify(self)
    unique_slug = slug
    num = 1
    while Category.objects.filter(slug=unique_slug).exists():
        num += 1
        unique_slug = '{slug}-{num}'.format(slug=slug, num=num)
    return unique_slug


def index(request):
    data = {'categories': Category.objects.all().order_by('-created_at')}
    return render(request, 'category.html', data)


def create(request):
    if request.method == "POST":
        name = request.POST['name']
        slug = _get_unique_slug(name)
        category = Category.objects.create(
            name=name,
            slug=slug
        )
        category.created = naturaltime(category.created_at)
        category.updated = naturaltime(category.updated_at)
        # category_se = serializers.serialize('json', [category])
        # return JsonResponse({'category': category_se})
        return JsonResponse({'name': category.name, 'slug': category.slug, 'created_at': category.created, 'id': category.id, 'updated_at': category.updated})
