from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'navy_church/index.html')
 
def sosik(request):
    return render(request, 'navy_church/sosik.html')

def iljung(request):
    return render(request, 'navy_church/iljung.html')

def yebe(request):
    return render(request, 'navy_church/yebe.html')