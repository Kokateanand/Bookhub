# adminpanel/forms.py

from django import forms
from .models import Customer,Category , Author , Warehouse ,Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'author', 'category', 'price', 'image']


class WarehouseForm(forms.ModelForm):
    class Meta:
        model = Warehouse
        fields = ['name', 'location']

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'email', 'phone']  # Include the fields you want to be editable



class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']  # Add more fields as needed

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'email', 'profile']  # Add any other fields you need

