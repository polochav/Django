"""
Configuración de URLs para el proyecto Proyecto1.

La lista `urlpatterns` enruta URLs a vistas. Para más información, consulta:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Ejemplos:
Vistas basadas en funciones
    1. Agrega una importación:  from my_app import views
    2. Agrega una URL a urlpatterns:  path('', views.home, name='home')
Vistas basadas en clases
    1. Agrega una importación:  from other_app.views import Home
    2. Agrega una URL a urlpatterns:  path('', Home.as_view(), name='home')
Incluyendo otra configuración de URLs
    1. Importa la función include(): from django.urls import include, path
    2. Agrega una URL a urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from Proyecto1.views import saludo
from Proyecto1.views import despedida
from Proyecto1.views import despedida2, fecha, calcula_edad,calcula_edad2,saludo2
from Proyecto1.views import fecha2,saludo3,cursoC,cursocss

urlpatterns = [
    path("admin/", admin.site.urls),
    path("saludo/", saludo),
    path("cursoC/", cursoC),
    path("cursocss/", cursocss),
    path("saludo2/", saludo2),
    path("saludo3/", saludo3),
    path("despedida/", despedida),
    path("despedida2/", despedida2),
    path("fecha/", fecha),
    path("fecha2/", fecha2),
    path("edad/<int:anio>", calcula_edad), #LE INDICAMOS AL PATH QUE SE LE PASARÁ UN PARÁMETRO POR LA URL 
    path("edad/<int:edad>/<int:anio>", calcula_edad2), #LE INDICAMOS AL PATH QUE SE LE PASARÁ VARIOS PARÁMETROS POR LA URL 

]
