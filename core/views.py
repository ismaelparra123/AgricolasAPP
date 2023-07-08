from django.shortcuts import render

# Create your views here.

def home (request):
    return render(request,'core/home.html')

def productos (request):
    return render(request,'core/productos.html')

def productores (request):
    return render(request,'core/productores.html')

def foro (request):
    return render(request,'core/foro.html')

def login (request):
    return render(request,'core/login.html')

def registro (request):
    if request.method == 'POST':
        usuario = request.POST.get("usuario")
        usuario = request.POST.get("usuario")
    return render(request,'core/registro.html')

def usuario (request):
    return render(request,'core/usuario.html')

def detalle_productores (request):
    return render(request,'core/detalle_productores.html')

def carrito (request):
    return render(request, 'core/carrito.html')

def API (request):
    return render(request, 'core/API.html')
   

