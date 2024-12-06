from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Author, Book, Warehouse,Customer
from .decorators import superuser_required
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.crypto import get_random_string
from django.contrib.auth import authenticate, login
from django.http import HttpResponseForbidden



from .forms import CustomerForm , CategoryForm , AuthorForm  , WarehouseForm  ,BookForm

def prevent_authenticated_access(view_func):
    """
    Middleware-like decorator to prevent authenticated users from accessing certain views.
    """
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseForbidden("You are already logged in.")
        return view_func(request, *args, **kwargs)
    return wrapper


def admin_login(request):
    """
    Custom login view for superusers in the admin panel.
    """
    if request.user.is_authenticated and request.user.is_superuser:
        return redirect('adminpanel:dashboard')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user and user.is_superuser:
            login(request, user)
            return redirect('adminpanel:dashboard')
        else:
            return render(request, 'adminpanel/login.html', {'error': 'Invalid credentials or not a superuser'})

    return render(request, 'login.html')


@login_required
@superuser_required
def dashboard(request):
    """
    Superuser-only dashboard view.
    """
    return render(request, 'adminpanel/dashboard.html')


# Categories
@login_required
@superuser_required
def categories(request):
    categories = Category.objects.all()
    return render(request, 'adminpanel/categories.html', {'categories': categories})

@login_required
@superuser_required
def add_category(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        Category.objects.create(name=name, description=description)
        messages.success(request, 'Category added successfully!')
        return redirect('adminpanel:categories')
    return render(request, 'adminpanel/add_category.html')


# Authors
@login_required
@superuser_required
def authors(request):
    authors = Author.objects.all()
    return render(request, 'adminpanel/authors.html', {'authors': authors})

@login_required
@superuser_required
def add_author(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        description = request.POST.get('description')
        profile = request.FILES.get('profile')
        Author.objects.create(name=name, email=email, description=description, profile=profile)
        messages.success(request, 'Author added successfully!')
        return redirect('adminpanel:authors')
    return render(request, 'adminpanel/add_author.html')


# Books
@login_required
@superuser_required
def books(request):
    books = Book.objects.all()
    return render(request, 'adminpanel/books.html', {'books': books})


@login_required
@superuser_required
def add_book(request):
    categories = Category.objects.all()
    authors = Author.objects.all()
    warehouses = Warehouse.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        category_id = request.POST.get('category')
        author_id = request.POST.get('author')
        description = request.POST.get('description')
        price = request.POST.get('price')
        image = request.FILES.get('image')
        selected_warehouses = request.POST.getlist('warehouses')

        # Generate a unique ID
        unique_id = get_random_string(10)

        # Create the book
        category = get_object_or_404(Category, id=category_id)
        author = get_object_or_404(Author, id=author_id)
        book = Book.objects.create(
            name=name, category=category, author=author, description=description, price=price, image=image, unique_id=unique_id
        )

        # Assign warehouses
        for warehouse_id in selected_warehouses:
            warehouse = get_object_or_404(Warehouse, id=warehouse_id)
            book.warehouses.add(warehouse)

        messages.success(request, 'Book added successfully!')
        return redirect('adminpanel:books')

    return render(request, 'adminpanel/add_book.html', {
        'categories': categories,
        'authors': authors,
        'warehouses': warehouses
    })


# Warehouses
@login_required
@superuser_required
def warehouses(request):
    warehouses = Warehouse.objects.all()
    return render(request, 'adminpanel/warehouses.html', {'warehouses': warehouses})

@superuser_required
def add_warehouse(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        location = request.POST.get('location')
        Warehouse.objects.create(name=name, location=location)
        messages.success(request, 'Warehouse added successfully!')
        return redirect('adminpanel:warehouses')
    return render(request, 'adminpanel/add_warehouse.html')

@login_required
@superuser_required
def customers(request):
    customers = Customer.objects.all()
    return render(request, 'adminpanel/customers.html', {'customers': customers})
#  categories = Category.objects.all()
    # return render(request, 'adminpanel/categories.html', {'categories': categories})


@login_required
@superuser_required
def add_customer(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone = request.POST.get('phone')
        city = request.POST.get('city')
        country = request.POST.get('country')
        email = request.POST.get('email')
        password = request.POST.get('password')

        Customer.objects.create(
            first_name=first_name, last_name=last_name, phone=phone, city=city, country=country, email=email, password=password
        )
        messages.success(request, 'Customer added successfully!')
        return redirect('user:customers')
    return render(request, 'adminpanel/add_customer.html')


def update_customer(request, id):
    # Retrieve the customer object by ID or return a 404 error if not found
    customer = get_object_or_404(Customer, id=id)
    
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('adminpanel:customers')  # Redirect to the customer list page
    else:
        form = CustomerForm(instance=customer)

    return render(request, 'adminpanel/update_customer.html', {'form': form, 'customer': customer})



def update_category(request, id):
    category = get_object_or_404(Category, id=id)
    form = CategoryForm(request.POST or None, instance=category)

    if form.is_valid():
        form.save()
        return redirect('adminpanel:categories')  # Redirect to the category list view

    return render(request, 'adminpanel/update_category.html', {'form': form, 'category': category})


def update_author(request, id):
    author = get_object_or_404(Author, id=id)
    form = AuthorForm(request.POST or None, instance=author)

    if form.is_valid():
        form.save()
        return redirect('adminpanel:authors')  # Redirect to the authors list view

    return render(request, 'adminpanel/update_author.html', {'form': form, 'author': author})


def update_warehouse(request, id):
    warehouse = get_object_or_404(Warehouse, id=id)
    form = WarehouseForm(request.POST or None, instance=warehouse)

    if form.is_valid():
        form.save()
        return redirect('adminpanel:warehouses')  # Redirect to the warehouse list view

    return render(request, 'adminpanel/update_warehouse.html', {'form': form, 'warehouse': warehouse})


def update_book(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('adminpanel:books')  # Redirect to books list after saving
    else:
        form = BookForm(instance=book)
    return render(request, 'adminpanel/update_book.html', {'form': form, 'book': book})