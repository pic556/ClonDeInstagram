from django.urls import path
from . import views

#url Publicaciones
urlpatterns=[
    path("",views.publicacion),
]
