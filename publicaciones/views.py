from django.shortcuts import render
from django.http import HttpResponse
from .models import Pub_instagram,Com_instagram
# views.publicaciones


def publicacion(request):
    posts= Pub_instagram.objects.all().order_by("-created_at")
    return render(request,"publicaciones/publicaciones.html",{"var_post":posts})
