from django.shortcuts import render
from django.http import HttpResponse
# views.publicaciones


def publicacion(request):
    return render(request,"publicaciones/publicaciones.html")
