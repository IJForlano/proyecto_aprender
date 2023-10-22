from django.http import HttpResponse
from django.template import Template, Context, loader
import datetime


def probando_template(request):
    nombre = "Ignacio"
    apellido = "Forlano"
    lista_de_notas = [1, 3, 4, 5, 6, 8, ]
    hoy = datetime.datetime.now()
    diccionario = {"nombre": nombre, "apellido": apellido, "notas": lista_de_notas, "hoy": hoy}
    plantilla = loader.get_template('template1.html')
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)
