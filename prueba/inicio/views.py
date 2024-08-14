from django.shortcuts import render

menu="""
    <a href="/">Home</a>
    <a href="/contacto">Contacto</a>
    <a href="/formulario>Formulario</a>
"""

def principal(request):
    return render(request, "inicio/principal.html")

def contacto(request):
    return render(request, "inicio/contacto.html")

def formulario(request):
    return render(request, "inicio/formulario.html")

def ejemplo(request):
    return render(request, "inicio/ejemplo.html")

def seguridad(request, nombre=None):
    nombre = request.GET.get('nombre')
    return render(request, "inicio/seguridad.html",{'nombre': nombre})

def comentarios(request):
    return render(request, "inicio/comentarios.html")
# Create your views here.

# Create your views here.
