from django.http import HttpResponse
import datetime
from django.template import Template,Context
from django.template.loader import get_template
from django.shortcuts import render


# ======MOSTRANDO CONTENIDO ESTÁTICO=====


def saludo(request):  # PRIMERA VISTA CARGANDO UNA PLANTILLA DESDE UN ARCHIVO
    # PRIMERA FORMA DE DAR ESTILOS HTML (FORMA MUY SIMPLE)
    return HttpResponse("<html><body><h1>Hola amigos:)))</h1><body></html>")


def despedida(request):
    # SEGUNDA FORMA DE DAR ESTILOS HTML (MÁS ELEGANTE Y RECOMENDADA)

    documento = "<html><body><h1>ADIOOOOOOOOOOOOOOOS</h1></body></html>"
    return HttpResponse(documento)


def despedida2(request):
    # TERCERA MANERA AÚN MÁS ELEGANTE DE DAR ESTILOS CON FORMATO HTML

    documento = """<html>
    <body>
    <h1>
    Hasta luego amigos (forma elegante)
    </h1>
    </body>
    </html>
    """

    return HttpResponse(documento)


# ======MOSTRANDO CONTENIDO DINÁMICO======

# MOSTRAR LA FECHA EXACTA DEL DÍA Y HORA EN QUE SE EJECUTE EL SERVIDOR


def fecha(request):
    fecha_actual = datetime.datetime.now()

    documento = (
        """
    <html>
    <body>
    <h1>
    Fecha actual: %s 
    </h1>
    </body>
    </html>"""
        % fecha_actual
    )

    return HttpResponse(documento)


# =====PASAR PARÁMETROS POR URL======


# EL VALOR AGNO ES PASADO COMO PARÁMETRO AL MOMENTO DE ESCRIBIR LA URL EN EL NAVEGADOR A LA SIGUIENTE VISTA
def calcula_edad(request, agno):  # Primera vez que la vistarecibe otro parámetro
    edad_actual = 20
    periodo = agno - 2024
    edad_futura = edad_actual + periodo
    documento = """
    <html>
    <body>
    <h1>
    En el año: %s tendrás %s años
    </h1>
    </body>
    </html>""" % (
        agno,
        edad_futura,
    )

    return HttpResponse(documento)


# ======PASAR DOS O MÁS PARÁMETROS POR URL========

def calcula_edad2(request, edad, agno):  # Primera vez que la vistarecibe otro parámetro
    periodo = agno - 2024
    edad_futura = edad + periodo
    documento = """
    <html>
    <body>
    <h1>
    En el año: %s tendrás %s años
    </h1>
    </body>
    </html>""" % (
        agno,
        edad_futura,
    )

    return HttpResponse(documento)

# ======PLANTILLAS 1======

# PRIMERA VISTA CARGANDO UNA PLANTILLA DESDE UN ARCHIVO EXTERNO
def saludo2(request):  

    doc_externo = open("/Users/leopoldochavarria/Documents/Programacion/Django/Proyecto1/Proyecto1/Plantillas/Primera_plantilla.html")

    plt = Template(doc_externo.read())

    doc_externo.close()

    ctx = Context()

    documento = plt.render(ctx)

    return HttpResponse(documento)

# SEGUNDA VISTA CARGANDO UNA PLANTILLA DESDE UN ARCHIVO EXTERNO CON VARIABLES
def fecha2(request):
    fecha = datetime.datetime.now()

    doc_externo = open("/Users/leopoldochavarria/Documents/Programacion/Django/Proyecto1/Proyecto1/Plantillas/Segunda_plantilla.html")

    plt = Template(doc_externo.read())

    doc_externo.close()

    ctx=Context({"Nombre":"Polo Chavarría","fecha_exacta":fecha})

    documento=plt.render(ctx)

    return HttpResponse(documento)

# ======CREANDO INSTANCIAS DE CLASES========

class Persona(object):
    def __init__(self,nombre,apellido):
        self.nombre=nombre
        self.apellido=apellido

# ======INSTANCIANDO LA CLASE PERSONA=====
def saludo3(request):

    p1=Persona("Leopoldo","Chavarría")

    # doc_externo = open("/Users/leopoldochavarria/Documents/Programacion/Django/Proyecto1/Proyecto1/Plantillas/Tercera_plantilla.html")

    # plt = Template(doc_externo.read())

    # doc_externo.close()

    #====USANDO LOADERS PARA CARGAR PLANTILLAS====

    # doc_externo = get_template("Tercera_plantilla.html")    

    mi_lista = ["Plantillas", "Modelos", "Formularios", "Listas"]

    # ctx = Context({"Nombre":p1.nombre,"Apellido":p1.apellido,"Temas":mi_lista})   #=====USANDO LISTA EN EL CONTEXTO=====

    # documento = doc_externo.render({"Nombre":p1.nombre,"Apellido":p1.apellido,"Temas":mi_lista})

    return render(request,"Tercera_plantilla.html",{"Nombre":p1.nombre,"Apellido":p1.apellido,"Temas":mi_lista})

# ======HERENCIA DE PLANTILLAS======
def cursoC(request):
    fecha_actual= datetime.datetime.now()
    return render(request,"cursoC.html",{"dame_fecha":fecha_actual})

def cursocss(request):
    fecha_actual = datetime.datetime.now()
    return render(request, "cursoCss.html", {"dame_fecha": fecha_actual})
