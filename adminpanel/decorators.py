from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import redirect
from django.contrib import messages


def superuser_required(view_func):
    """
    Decorator to ensure the view is accessible only to superusers.
    """
    decorated_view_func = user_passes_test(
        lambda u: u.is_active and u.is_superuser,
        login_url='/admin/',  # Redirect to admin login if not superuser
    )(view_func)
    return decorated_view_func


def auth(view_function):
    def wrapped_view(request, *args, **kwargs):
        # Skip the auth check if the user is already on the login page
        if request.path != '/user/login/':
            if not request.user.is_authenticated:
                messages.error(request, "Please log in to access this page.")
                return redirect('user:login')  # Redirect to login page if not authenticated
        return view_function(request, *args, **kwargs)
    return wrapped_view






