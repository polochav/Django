from django.shortcuts import render
from django.http import HttpResponse
from gestionPedidos.models import Articulos
# Create your views here.

def busqueda_productos(request):
    return render(request, "busqueda_productos.html")

def resultado_busqueda(request):
    if request.GET["prod"]:
        #mensaje = "Articulo buscado: %r" %request.GET["prod"]
        producto = request.GET["prod"]
        articulos = Articulos.objects.filter(nombre__icontains=producto)
        return render(request, "resultados_busqueda.html",{"articulos":articulos,"query":producto})

    else:
        mensaje = "No has introducido nada"
    return HttpResponse (mensaje)