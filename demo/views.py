from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'demo/themes/home.html')

def about(request):
    return render(request, 'demo//themes/about.html')

def blog(request):
    return render(request, 'demo//themes/blog.html')

def portfolio(request):
    return render(request, 'demo//themes/portfolio.html')

def contact(request):
    return render(request, 'demo//themes/contact.html')

def blogsingle(request):
    return render(request, 'demo//themes/blogsingle.html')

