

"""
def hello_world(request):
    return render(request, 'hello_world.html', {})

    NO HE CONSEGUIDO LOCALIZAR EL METODO PARA PODER
    OBTENER LA INFO EN UN JSON, SIMPLE VISUALIZACION EN
    LA CONSOLA.
"""

from django.shortcuts import render
from django.http import  HttpRequest




def hello_world(request):
    query = request.GET.get('dominio')
    message = "Este es el dominio {} ".format(query)
    template = "hello_world.html"
    context = {
        'message': message,
    }
    return render(request, template, context)