from django.shortcuts import render

# Create your views here.
def home_falkov(request):
    return render(request, 'app_1/home_falkov.html', {})

def home(request):
    return render(request, 'app_1/home.html', {})
