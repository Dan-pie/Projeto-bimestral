from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')

def login_pag(request):
    return render(request, 'login.html',)

def cad_pag(request):
    return render(request, 'cad.html',)
