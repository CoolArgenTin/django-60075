
from django.http import HttpResponse
from django.template import Template, Context, loader
from datetime import datetime
from django.shortcuts import render
from inicio.models import Auto


def mi_view(request):
    return HttpResponse("SOY UNA VISTA (view) JAJA")

def inicio(request):
    return render(request, "index.html")

def dataxd(request):
    return HttpResponse("XD")

def segundo_template(request):
    
    fecha_actual = datetime.now()
    datos = {
        "fecha_actual": fecha_actual,
        "numeros": list(range(1, 7))
    }
    
    # V1
    # archivo_del_template = open(r"templates\segundo_template.html")
    # template = Template(archivo_del_template.read())
    # archivo_del_template.close()
    # contexto = Context(datos)
    # render_template = template.render(contexto)
    # return HttpResponse(render_template)
    
    # V2
    # template = loader.get_template("segundo_template.html")
    # render_template = template.render(datos)
    # return HttpResponse(render_template)
    
    # V3
    return render(request, "segundo_template.html", datos)

def primer_template(request):
    
    archivo_del_template = open(r"templates\primer_template.html")
    
    template = Template(archivo_del_template.read())
    
    archivo_del_template.close()
    
    contexto = Context()
    
    render_template = template.render(contexto)
    
    return HttpResponse(render_template)

def crear_auto(request, marca, modelo, anio):
    
    auto = Auto(marca=marca, modelo=modelo, edad=anio)
    auto.save()
    
    return render(request, "crear_auto.html", {"auto": auto})