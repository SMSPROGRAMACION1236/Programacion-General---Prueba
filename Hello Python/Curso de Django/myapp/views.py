from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

""" Explicacion:
En esta seccion se va a crear una vista que va a renderizar un template HTML.
La vista se va a llamar 'index' y va a recibir una solicitud HTTP.
Que se realizara o que enviaremos al cliente."""



def hello_word(request):
  return HttpResponse("<h1>Hello World!<!/h1>")

def about(request):
  return HttpResponse("<h1>About</h1>")