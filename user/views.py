from django.shortcuts import render, redirect
from django.contrib import messages
from adminpanel.models import Customer, Book, PurchaseHistory, Warehouse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import login as auth_login
from adminpanel.decorators import auth
from django.contrib.auth.backends import BaseBackend
# from django.utils.http import url_has_allowed_host_and_scheme




def login_view(request):
    if request.user.is_authenticated:
        messages.info(request, "You are already logged in.")
        return redirect('user:shop')  # Redirect to the shop page if already logged in

    if request.method == 'POST':
        login_input = request.POST.get('login_input')  # Email or phone
        password = request.POST.get('password')
        next_url = request.GET.get('next')  # Get the next parameter from URL

        # Find customer by email or phone
        try:
            customer = Customer.objects.get(email=login_input)  # Try to find by email first
        except Customer.DoesNotExist:
            try:
                customer = Customer.objects.get(phone=login_input)  # Try to find by phone if email fails
            except Customer.DoesNotExist:
                messages.error(request, "No account found with that email or mobile number.")
                return render(request, 'auth/login.html')

        # Verify the password
        if check_password(password, customer.password):  # Check if password matches
            # If password is correct, log the user in
            auth_login(request, customer)  # Log in the customer
            messages.success(request, "Login successful!")

            # Redirect to the next URL or the shop page
            if next_url:
                return redirect(next_url)
            return redirect('user:shop')  # Default redirect to shop page
        else:
            messages.error(request, "Incorrect password.")
            return render(request, 'auth/login.html')

    return render(request, 'auth/login.html')



class CustomerBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        # Try to authenticate using email or phone
        try:
            user = Customer.objects.get(email=username)  # Try to find by email first
        except Customer.DoesNotExist:
            try:
                user = Customer.objects.get(phone=username)  # Try to find by phone
            except Customer.DoesNotExist:
                return None  # No user found

        if user and check_password(password, user.password):  # Verify password
            return user
        return None  # Return None if authentication fails





# @login_required
def dashboard_view(request):
    customer_id = request.session.get('customer_id')
    if not customer_id:
        return redirect('login')

    try:
        customer = Customer.objects.get(id=customer_id)
        purchase_history = PurchaseHistory.objects.filter(customer=customer)
        books = Book.objects.all()
        return render(request, 'user_admin/dashboard.html', {
            'customer': customer,
            'purchase_history': purchase_history,
            'books': books,
        })
    except ObjectDoesNotExist:
        messages.error(request, "User not found.")
        return redirect('login')



# @auth
def shop_view(request):
    books = Book.objects.all()  # Fetch all books
    return render(request, 'user_admin/shopping_page.html', {'books': books})
    # return render(request, 'user_admin/shopping_page.html')

def shopping_page_view(request):
    books = Book.objects.all()
    return render(request, 'user_admin/shopping_page.html', {
        'books': books,
    })


# @login_required
def product_detail_view(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
        warehouses = Warehouse.objects.filter(books__id=book_id)
        return render(request, 'user_admin/product_detail.html', {
            'book': book,
            'warehouses': warehouses,
        })
    except ObjectDoesNotExist:
        messages.error(request, "Book not found.")
        return redirect('user_admin/shopping_page')




# def login_view(request):
#     if request.user.is_authenticated:
#         messages.info(request, "You are already logged in.")
#         return redirect('Shop')  # Redirect to shop page if already logged in

#     if request.method == 'POST':
#         login_input = request.POST.get('login_input')  # Email or mobile
#         password = request.POST.get('password')

#         try:
#             user = Customer.objects.get(email=login_input)  # Try email first
#         except Customer.DoesNotExist:
#             try:
#                 user = Customer.objects.get(phone=login_input)  # Then phone
#             except Customer.DoesNotExist:
#                 messages.error(request, "No account found with that email or mobile number.")
#                 return render(request, 'auth/login.html')

#         # Verify password
#         if check_password(password, user.password):
#             # Log the user in
#             login(request, user)
#             messages.success(request, "Login successful!")
#             return redirect('Shop')  # Redirect to shop page
#         else:
#             messages.error(request, "Incorrect password.")
#             return render(request, 'auth/login.html')

#     return render(request, 'auth/login.html')




def register_view(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm-password')

        # Check if passwords match
        if password != confirm_password:
            messages.error(request, "Password and Confirm Password do not match.")
            return render(request, 'auth/register.html')

        # Check if the mobile number already exists in the database
        if Customer.objects.filter(phone=mobile).exists():
            messages.error(request, "Mobile number is already registered.")
            return render(request, 'auth/register.html')

        # Check if the email already exists in the database
        if Customer.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered.")
            return render(request, 'auth/register.html')

        # If everything is okay, create the user
        customer = Customer(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=mobile,
            password=password  # Store the password directly for now (consider hashing it)
        )
        customer.save()

        messages.success(request, "You are registered successfully! Now you can log in.")
        return redirect('user:login')

    return render(request, 'auth/register.html')


def logout_view(request):
    request.session.flush()
    messages.success(request, "Logged out successfully.")
    return redirect('user:login')



