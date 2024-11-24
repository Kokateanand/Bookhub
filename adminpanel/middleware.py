from django.shortcuts import redirect

class SuperAdminCheckMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/adminpanel/') and not request.user.is_superuser:
            return redirect('/admin/login/')
        return self.get_response(request)
    



# ******* Authenticated *******
def auth(view_function):
    def wrapped_view(request,*args,**kwargs):
        if request.user.is_authenticated == False:
            return redirect('login')
        return view_function(request, *args, **kwargs)
    return wrapped_view

# ******* Guest *******
def guest(view_function):
    def wrapped_view(request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')
        return view_function(request, *args, **kwargs)
    return wrapped_view


