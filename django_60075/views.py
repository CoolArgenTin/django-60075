
from django.http import HttpResponse

def mi_view(request):
    return HttpResponse("SOY UNA VISTA (view) JAJA")

def inicio(request):
    return HttpResponse("<h1> PANTALLA DE INICIO TODO PIOLA </h1>")

def dataxd(request, nombre):
    nombre_mayuscula = nombre.upper()
    return HttpResponse(f"Buenas, NANA, ACASO SOS {nombre_mayuscula}?? PIOLAAA")
