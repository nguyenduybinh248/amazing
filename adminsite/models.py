from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'adminsite'
        db_table = 'adminsite_category'
        # ordering = ('name',)
        # verbose_name = 'category'
        # verbose_name_plural = 'categories'

    # def __str__(self):
    #     return self.name
    #
    # def get_absolute_url(self):
    #     return reverse('', args=[self.slug])