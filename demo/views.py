from django.shortcuts import render
from demo.models import Project


# Create your views here.
def home(request):
    training = Project.objects.all()
    context = {'training': training}
    return render(request, 'demo/themes/home.html', context)

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

def training(request):
    training = Project.objects.all()
    context = {'training': training}
    return render(request, 'demo//themes/training.html', context)

def trainingdetails(request, id):
    training = Project.objects.get(id=id)
    context = {'training': training}
    return render(request, 'demo//themes/trainingdetails.html', context)

