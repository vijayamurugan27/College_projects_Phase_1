from django.shortcuts import render
from shop.models import Products, Customer

# Create your views here.
def home(request):
    return render(request, 'shop/home.html') 
def Shirts(request):
    shirts = Products.objects.all()
    context = {'shirts': shirts, }
    return render(request, 'shop/shirts.html', context)


from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView

class ShirtDetail(CreateView):
    model = Products
    fields = "__all__"
    template_name = 'shop/cbv/form.html'
    success_url = 'home'

# class ShirtList(ListView):
#     model = Products
#     template_name = 'library/cbv/stulist.html'
