from django.urls import path
from . import category
from . import views

urlpatterns = [
    path('', category.index),
    path('create', category.create, name='create_category'),
]