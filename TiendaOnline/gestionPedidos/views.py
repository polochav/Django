from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def busqueda_productos(request):
    return render(request, "busqueda_productos.html")

def resultado_busqueda(request):
    if request.GET["prod"]:
        mensaje = "Articulo buscado: %r" %request.GET["prod"]
    else:
        mensaje = "No has introducido nada"
    return HttpResponse (mensaje)