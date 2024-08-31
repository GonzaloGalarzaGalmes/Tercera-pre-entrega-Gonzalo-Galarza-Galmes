from django.http import HttpResponse
from django.template import Template, Context
from datetime import datetime
from django.template import loader
from mi_aplicacion.models import Artista



def saludo(request):
    return HttpResponse("Hola")

def desde_plantilla(request):

    nom = "Gonzalo"
    ap = "Galarza Galmes"

    diccionario = {"nombre": nom, "apellido": ap, "Hoy": datetime.now}
    # mi_html = open('C:/Users/Kalukiddd/Desktop/Entregable/mi_proyecto/plantillas/template1.html')
    # plantilla = Template(mi_html.read())
    # mi_html.close()
    # mi_contexto = Context(diccionario)
    plantilla = loader.get_template("template1.html")
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)

def agregar_artista(request, nom, gen, p):
    artista = Artista(nombre = nom, genero = gen, pais = p)
    artista.save()
    return HttpResponse("Artista agregado")