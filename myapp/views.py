from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    return render(request, 'index.html')

    # return HttpResponse ("this is the home page")

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def shop(request):
    return render(request, 'shop.html')