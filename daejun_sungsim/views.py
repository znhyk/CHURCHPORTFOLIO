from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'daejun_sungsim/index.html')
 
def sosik(request):
    return render(request, 'daejun_sungsim/sosik.html')

def iljung(request):
    return render(request, 'daejun_sungsim/iljung.html')

def yebe(request):
    return render(request, 'daejun_sungsim/yebe.html')