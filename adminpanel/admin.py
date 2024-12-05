from django.contrib import admin
from .models import Category, Author, Customer, Warehouse, PurchaseHistory, Book

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'description')

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'city', 'country', 'is_active')

@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')

@admin.register(PurchaseHistory)
class PurchaseHistoryAdmin(admin.ModelAdmin):
    list_display = ('customer', 'book', 'quantity', 'total_price', 'purchased_at')

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'author', 'price', 'unique_id')
