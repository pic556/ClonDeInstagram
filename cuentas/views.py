from django.shortcuts import render
# views.cuentas


def registro(request):
    return render(request, "cuentas/registros.html")

def acceso_user(request):
    return render(request,"cuentas/acceso.html")
