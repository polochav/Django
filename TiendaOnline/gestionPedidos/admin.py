from django.contrib import admin

from gestionPedidos.models import (
    Clientes,
    Articulos,
    Pedidos,
)  # importamos el modelo a trabajar

# Register your models here.


class ClientesAdmin(admin.ModelAdmin):
    list_display = ("nombre", "direccion", "telefono")
    search_fields = ("nombre", "telefono")


admin.site.register(Clientes, ClientesAdmin)
admin.site.register(Articulos)
admin.site.register(Pedidos)
