from django.shortcuts import render, redirect
from .models import Book, Author, Category, Warehouse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .middleware import guest



# Create your views here.

@guest
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('dashboard')
    else:
        initial_data = {'username':'', 'password':''}
        form = AuthenticationForm(initial=initial_data)
    return render(request, 'auth/login.html',{'form':form}) 

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard(request):
    if not request.user.is_superuser:
        return HttpResponseForbidden("You do not have access to this page.")
    return render(request, 'admin/dashboard.html')

@login_required
def books(request):
    if request.method == 'POST':
        # Add book logic
        pass
    books = Book.objects.all()
    return render(request, 'admin/books.html', {'books': books})

@login_required
def authors(request):
    authors = Author.objects.all()
    return render(request, 'admin/authors.html', {'authors': authors})

@login_required
def categories(request):
    categories = Category.objects.all()
    return render(request, 'admin/categories.html', {'categories': categories})

@login_required
def customers(request):
    # if request.method == 'POST':
    #     # Adding a new customer
    #     first_name = request.POST.get('first_name')
    #     last_name = request.POST.get('last_name')
    #     phone = request.POST.get('phone')
    #     city = request.POST.get('city')
    #     country = request.POST.get('country')
    #     email = request.POST.get('email')
    #     password = request.POST.get('password')
        
    #     Customer.objects.create(
    #         first_name=first_name,
    #         last_name=last_name,
    #         phone=phone,
    #         city=city,
    #         country=country,
    #         email=email,
    #         password=password,
    #     )
    #     return redirect('customers')

    # customers = Customer.objects.all()
    # return render(request, 'admin/customers.html', {'customers': customers})
    return render(request, 'admin/customers.html')

@login_required
def warehouses(request):
    if request.method == 'POST':
        # Adding a new warehouse
        name = request.POST.get('name')
        location = request.POST.get('location')
        
        Warehouse.objects.create(name=name, location=location)
        return redirect('warehouses')

    warehouses = Warehouse.objects.all()
    return render(request, 'admin/warehouses.html', {'warehouses': warehouses})


