from django.http import HttpResponseRedirect

class RestrictLoginSignupMiddleware:
    """
    Middleware to restrict logged-in users from accessing login or signup pages.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path in ['/adminpanel/login', '/user/auth/login/', '/user/auth/register/'] and request.user.is_authenticated:
            return HttpResponseRedirect('/adminpanel/dashboard')
        return self.get_response(request)
