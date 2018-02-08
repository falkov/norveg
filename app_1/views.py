from django.shortcuts import render

# Create your views here.
def home_falkov(request):
    return render(request, 'app_1/home_falkov.html', {})

def home(request):
    return render(request, 'app_1/app_main.html', {})

def my_index(request):
    return render(request, 'app_1/my_index.html', {})