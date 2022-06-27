from django.http import HttpResponse
from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    mensaje="""
        <h1>Inicio</h1>
    """
    return HttpResponse(mensaje)

def saludo(request):
    mensaje = """
        <h1> Bienvenidos</h1>
        <h2> Elias Reyes</h2>
        <h3> Python</h3>
        <h2> Ahora largate hijo me indignas <h2>
        """
    return HttpResponse(mensaje)




