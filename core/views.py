from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'core/index.html')
def contacto(request):
    return render(request, 'core/contacto.html')
def tienda(request):
    return render(request, 'core/tienda.html')
def posturas(request):
    return render(request, 'core/posturas.html')
def sucursales(request):
    return render(request, 'core/sucursales.html')
def yoga(request):
    return render(request, 'core/clases.html')
def register(request):
    return render(request, 'core/register.html')

def login(request):
    return render(request, 'core/login.html')
def nosotros(request):
    return render(request, 'core/nosotros.html')


