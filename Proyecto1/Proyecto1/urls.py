"""
URL configuration for Proyecto1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from Proyecto1.views import saludo
from Proyecto1.views import despedida
from Proyecto1.views import despedida2, fecha, calcula_edad,calcula_edad2,saludo2,fecha2,saludo3,cursoC,cursocss

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
    path("edad/<int:agno>", calcula_edad), #LE INDICAMOS AL PATH QUE SE LE PASARÁ UN PARÁMETRO POR LA URL 
    path("edad/<int:edad>/<int:agno>", calcula_edad2), #LE INDICAMOS AL PATH QUE SE LE PASARÁ UN PARÁMETRO POR LA URL 

]
