from django.contrib import admin

from .models import Product, Category ,Tag , Review

admin.site.register(Product)

# Register your models here.
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Review)
