from django.shortcuts import render
from home import views
# Create your views here.

def home_view(request):
    return render(request, 'home/home.html')
