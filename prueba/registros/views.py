from django.shortcuts import render 
from .models import Alumnos
from .forms import ComentarioContactoForm
from .models import ComentarioContacto
from django.shortcuts import get_object_or_404
import datetime
#accedemos al modelo alumnos que contiene  la estructura de la tabla
# Create your views here.
def registros(request):
    alumnos=Alumnos.objects.all()
#All recupera todos los objetos del modelo (Registros de la tabla alumnos)
#indicamos el lugar donde se randerizara el resultado de esta vista

    return render(request, "registros/principal.html",{"alumnos":alumnos})
#Indicamos el lugar donde se renderizara el resultado de la vista 

def contacto(request):
    return render(request, "registros/contacto.html")

def registrar(request):
    if request.method == 'POST':
        form = ComentarioContactoForm(request.POST)
        if form.is_valid(): # Si los datos son correctos
            form.save() # inserta
            return render(request, 'registros/contacto.html')
    form = ComentarioContactoForm()
    # Si algo sale mal se reenvian al formulario los datos ingresados
    return render(request, 'registros/contacto.html', {'form': form})


def comentario(request):
    comentarios = ComentarioContacto.objects.all()
    return render(request, 'registros/consultar_comentario.html', {'comentarios': comentarios})

def eliminarComentarioContacto(request, id, 
        confirmacion='registros/confirmarEliminacion.html'):
        comentario = get_object_or_404(ComentarioContacto, id=id)
        if request.method == 'POST':
             comentario.delete()
             comentarios = ComentarioContacto.objects.all()
             return render(request, 'registros/consultar_comentario.html', {'comentarios': comentarios})
        return render(request, confirmacion, {'object': comentario})

def consultarComentarioIndividual(request, id):
     comentario=ComentarioContacto.objects.get(id=id)
     return render(request, "registros/formEditarComentario.html", {'comentario': comentario})

def editarComentarioContacto(request, id):
     comentario= get_object_or_404(ComentarioContacto, id=id)
     form = ComentarioContactoForm(request.POST, instance=comentario)

     if form.is_valid():
            form.save()
            comentarios = ComentarioContacto.objects.all() 
            return render(request,'registros/consultar_comentario.html', {'comentarios': comentarios})
     
     return render(request, 'registros/formEditarComentario.html', {'comentario': comentario})

def consultar1(request):
     alumnos = Alumnos.objects.filter(carrera="TI")
     return render(request, 'registros/consulta.html', {'alumnos': alumnos})

def consultar2(request):
     alumnos = Alumnos.objects.filter(carrera="TI").filter(turno="Matutino")
     return render(request, 'registros/consulta.html', {'alumnos': alumnos})

def consultar3(request):
     alumnos = Alumnos.objects.all().only("matricula","nombre","carrera","turno", "imagen")
     return render(request, 'registros/consulta.html', {'alumnos': alumnos})

def consultar4(request):
     alumnos = Alumnos.objects.filter(turno__contains="Vesp")
     return render(request, 'registros/consulta.html', {'alumnos': alumnos})

def consultar5(request):
     alumnos = Alumnos.objects.filter(nombre__in=["Juan","Ana"])
     return render(request, 'registros/consulta.html', {'alumnos': alumnos})

def consultar6(request):
     fechaInicio=datetime.date(2024, 5, 1)
     fechaFin=datetime.date(2024, 7, 31)
     alumnos = Alumnos.objects.filter(created__range=(fechaInicio,fechaFin))
     return render(request, 'registros/consulta.html', {'alumnos': alumnos})

def consultar7(request):
     alumnos = Alumnos.objects.filter(comentario__coment__contains='No inscrito')
     return render(request, 'registros/consulta.html', {'alumnos': alumnos})


def consultasSQL(request):
     alumnos=Alumnos.objects.raw('SELECT id, matricula,nombre, carrera, turno, imagen FROM registros_alumnos WHERE carrera="TI"ORDER BY turno DESC')
     return render(request,"registros/consulta.html",{'alumnos':alumnos})



