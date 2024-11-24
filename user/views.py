# views.py

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from adminpanel.models import Customer
from user.forms import RegisterForm, LoginForm
from django.core.exceptions import ValidationError



def login_view(request):
    if request.method == 'POST':
        login_input = request.POST.get('login_input')  # Could be email or mobile number
        password = request.POST.get('password')

        try:
            user = Customer.objects.get(phone=login_input)  # Try finding by phone first
        except Customer.DoesNotExist:
            try:
                user = Customer.objects.get(email=login_input)  # If not found, try finding by email
            except Customer.DoesNotExist:
                messages.error(request, "No account found with that email or mobile.")
                return render(request, 'auth/login.html')

        # Check if password matches
        if user.password == password:  # You may want to hash the password in a real app
            login(request, user)  # Log the user in
            messages.success(request, "Login successful!")
            return redirect('home')  # Redirect to home or dashboard
        else:
            messages.error(request, "Incorrect password.")
            return render(request, 'auth/login.html')

    return render(request, 'auth/login.html')

    # return render(request, 'auth/login.html', {'form': form})

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
        return redirect('login')

    return render(request, 'auth/register.html')