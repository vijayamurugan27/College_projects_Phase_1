from django.shortcuts import render

from restaurant.models import Foods
# Create your views here.
def home(request):
    food = Foods.objects.all()
    context = {'food':food}
    return render(request, 'restaurant/home.html', context)