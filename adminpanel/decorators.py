from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import user_passes_test

def superuser_required(view_func):
    """
    Decorator to ensure the view is accessible only to superusers.
    """
    decorated_view_func = user_passes_test(
        lambda u: u.is_active and u.is_superuser,
        login_url='/admin/',  # Redirect to admin login if not superuser
    )(view_func)
    return decorated_view_func
