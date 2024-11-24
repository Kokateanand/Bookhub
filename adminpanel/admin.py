from django.contrib import admin
from .models import Category, Author, Book, Customer, Warehouse

# Register your models here.



admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Customer)
admin.site.register(Warehouse)
