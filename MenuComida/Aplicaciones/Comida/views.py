from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from .models import Platillo, Calificacion
from datetime import date
from decimal import Decimal, InvalidOperation


from django.contrib import messages

def inicio(request):
    return render(request,'inicio.html')

#Presentando en pantalla el formulario de nuevo Estudiante
def platillos(request):
    platillo=Platillo.objects.all()
    return render(request,'platillos.html',{'platillos':platillo})


def verPlatillo(request):
    platillos=Platillo.objects.all()
    return render(request,'verPlatillo.html',{'platillos':platillos})




def menu_filtrado(request, tipo=None):
    if tipo:
        platillos = Platillo.objects.filter(tipo=tipo, is_hidden=False)
    else:
        platillos = Platillo.objects.filter(is_hidden=False)

    return render(request, 'menu_filtrado.html', {'platillos': platillos, 'tipo': tipo})

# Vista para mostrar los detalles de un platillo
# Vista para mostrar los detalles de un platillo y gestionar calificaciones
def platillo_detalle(request, platillo_id):
    platillo = get_object_or_404(Platillo, id=platillo_id)
    calificaciones = Calificacion.objects.filter(platillo=platillo)
    
    if request.method == "POST":
        # Diferenciar entre agregar y eliminar calificaciones
        if 'eliminar_calificacion' in request.POST:
            calificacion_id = request.POST.get('eliminar_calificacion')
            calificacion = get_object_or_404(Calificacion, id=calificacion_id)
            calificacion.delete()
            messages.success(request, "La calificación ha sido eliminada exitosamente.")
            return redirect('platillo_detalle', platillo_id=platillo_id)
        else:
            # Guardar nueva calificación
            usuario = request.POST.get('usuario')
            calificacion = request.POST.get('calificacion')
            comentario = request.POST.get('comentario')
            Calificacion.objects.create(
                platillo=platillo,
                usuario=usuario,
                calificacion=calificacion,
                comentario=comentario
            )
            messages.success(request, "Tu calificación ha sido guardada exitosamente.")
            return redirect('platillo_detalle', platillo_id=platillo_id)

    return render(request, 'platillo_detalle.html', {
        'platillo': platillo,
        'calificaciones': calificaciones
    })


#Capturando datos del formulario e insertando en la Bdd
def guardarPlatillo(request):
    nombre=request.POST['txt_nombre']
    foto_platillo=request.FILES.get('foto_platillo')
    descripcion=request.POST['txt_descripcion']
    precio = Decimal(request.POST['txt_precio'])
    tipo = request.POST['txt_tipo']

    informacion_nutricional=request.POST['txt_info_nutricional']
    fecha_disponible=request.POST.get('txt_fecha_disponible')
    platillos=Platillo.objects.create(nombre=nombre, foto_platillo=foto_platillo,
                                             descripcion=descripcion, tipo=tipo, precio=precio,informacion_nutricional=informacion_nutricional,
                                             fecha_disponible=fecha_disponible)
    messages.success(request, "Platillo agregado exitosamente")
    return redirect('/platillos')




def procesarEdicionPlatillo(request):
    # Obtener el platillo mediante el ID
    platillo = Platillo.objects.get(id=request.POST['id'])

    # Actualizar los campos del platillo con los valores enviados desde el formulario
    platillo.id = request.POST['id']
    platillo.nombre = request.POST['txt_nombre']
    platillo.descripcion = request.POST['txt_descripcion']
    platillo.tipo = request.POST['txt_tipo']

    precio_str = request.POST['txt_precio'].replace(',', '.')  # Convertir coma a punto
    platillo.precio = Decimal(precio_str)
    
    platillo.informacion_nutricional = request.POST['txt_informacion_nutricional']
    platillo.fecha_disponible = request.POST.get('txt_fecha_disponible')

    if 'foto_platillo' in request.FILES:
        platillo.foto_platillo = request.FILES['foto_platillo']

    platillo.save()
    messages.success(request, "Platillo editado exitosamente")
    return redirect('/verPlatillo')



def editarPlatillo(request, platillo_id):
    # Obtén el platillo por su ID
    platillo = Platillo.objects.get(id=platillo_id)
    platillo.precio = str(platillo.precio).replace(',', '.')
    return render(request, 'editarPlatillo.html', {'platillo': platillo})  # Cambiar 'platillos' a 'platillo'



def eliminarPlatillo(request,id):
    eliminar=Platillo.objects.get(id=id)
    eliminar.delete()
    messages.success(request, "Platillo eliminado exitosamente")
    return redirect('/verPlatillo')

def ocultar_platillo(request, platillo_id):
    platillo = get_object_or_404(Platillo, id=platillo_id)
    platillo.is_hidden = not platillo.is_hidden  # Cambiar el estado de oculto
    platillo.save()
    return redirect('/verPlatillo') 
