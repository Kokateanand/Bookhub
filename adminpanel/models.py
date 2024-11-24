from django.db import models
from django.utils import timezone
import uuid

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=100)
    profile = models.ImageField(upload_to='authors/')
    email = models.EmailField()
    description = models.TextField()

    def __str__(self):
        return self.name




class Book(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='books/')
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)  # Auto generates UUID

    def __str__(self):
        return self.name





class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15, unique=True)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

       # Add fields from the default User model
    last_login = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)  # For active users

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    

     

class Warehouse(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name
