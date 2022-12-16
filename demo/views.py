from django.shortcuts import render
from demo.models import Project, Blog, Team


# Create your views here.
def home(request):
    training = Project.objects.all()
    context = {'training': training}
    return render(request, 'demo/themes/home.html', context)

def about(request):
    team = Team.objects.all()
    context = {'team': team}
    return render(request, 'demo//themes/about.html', context)

def blog(request):
    blog = Blog.objects.all()
    context = {'blog': blog}
    return render(request, 'demo//themes/blog.html', context)

def portfolio(request):
    return render(request, 'demo//themes/portfolio.html')

def contact(request):    
    return render(request, 'demo//themes/contact.html')

def blogsingle(request, id):
    blog = Blog.objects.get(id = id)
    blog1= Blog.objects.all()
    context = {'blog': blog, 'blog1': blog1}
    return render(request, 'demo//themes/blogsingle.html', context)

def training(request):
    training = Project.objects.all()
    context = {'training': training}
    return render(request, 'demo//themes/training.html', context)



def trainingdetails(request, id):
    training = Project.objects.get(id=id)
    context = {'training': training}
    print(type(training.syllabus1))
    print(type(training.syllabus18))
    print(training.syllabus1)
    print(training.syllabus18)
    if not training.syllabus18:
        print("Hai")
    if (training.syllabus18 == None):
        print("Hello")
    return render(request, 'demo//themes/trainingdetails.html', context)

from django.views.generic import CreateView,  UpdateView

class TrainerCreateView(CreateView):
    model = Team
    fields = '__all__'
    template_name = 'demo/themes/cbv/create.html'
    success_url = '/demo/home'

class TrainerUpdateView(UpdateView):
    model = Team
    fields = '__all__'
    template_name = 'demo/themes/cbv/update.html'
    success_url = '/demo/home'
    
