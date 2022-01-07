from django.urls import path
from . import views
#url cuentas

urlpatterns=[
    path("registro/",views.registro,name="R"),
    path("acceso/",views.acceso_user, name = "L"),
]
