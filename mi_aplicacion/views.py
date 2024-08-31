from django.shortcuts import render, redirect
from mi_aplicacion.models import Artista, Album, Cancion
from mi_aplicacion.forms import artistasFormulario, AlbumFormulario, CancionFormulario, BuscarFormulario
from django.http import HttpResponse, HttpResponseRedirect
from mi_aplicacion.models import Cancion
# Create your views here.

def inicio(request):
    return render(request, 'Mi_Aplicacion/padre.html')

def Artistas(request):
    return render(request, 'Mi_Aplicacion/Artistas.html')

def Album(request):
    return render(request, 'Mi_Aplicacion/Album.html')

def cancion_view(request):
    return render(request, 'Mi_Aplicacion/Cancion.html')

def Artistas_Formulario(request):
    if request.method == 'POST':
        artista = Artista(nombre=request.POST['artista'], genero=request.POST['genero'], pais=request.POST['pais'])
        artista.save()
        return render(request, 'Mi_Aplicacion/padre.html')
    return render(request, 'Mi_Aplicacion/ArtistasFormulario.html')

def artistas_formulario(request):
    if request.method == 'POST':
        miFormulario = artistasFormulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            artista = Artista(
                nombre=informacion["nombre"],
                genero=informacion["genero"],
                pais=informacion["pais"],
                orden=informacion["orden_de_artista_BD"]
            )
            artista.save()
            return render(request, 'Mi_Aplicacion/padre.html')
    else:
        miFormulario = artistasFormulario()

    return render(request, 'Mi_Aplicacion/artistaFormulario.html', {"miFormulario": miFormulario}) 


from django.shortcuts import render
from mi_aplicacion.models import Album, Artista
from mi_aplicacion.forms import AlbumFormulario

def album_formulario(request):
    if request.method == 'POST':
        miFormulario = AlbumFormulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            
            artista, creado = Artista.objects.get_or_create(nombre=informacion['artista_nombre'])

            album = Album.objects.create(
                titulo=informacion['titulo'],
                artista=artista,
                fecha_lanzamiento=informacion['fecha_lanzamiento']
            )

            return render(request, 'Mi_Aplicacion/padre.html')
    else:
        miFormulario = AlbumFormulario()

    return render(request, 'Mi_Aplicacion/albumFormulario.html', {"miFormulario": miFormulario})


def cancion_formulario(request):
    if request.method == 'POST':
        miFormulario = CancionFormulario(request.POST)
        if miFormulario.is_valid():
            miFormulario.save()
            return render(request, 'Mi_Aplicacion/padre.html')
    else:
        miFormulario = CancionFormulario()

    return render(request, 'Mi_Aplicacion/CancionFormulario.html', {'miFormulario': miFormulario})


def buscar(request):
    resultados = None
    if request.method == 'POST':
        formulario = BuscarFormulario(request.POST)
        if formulario.is_valid():
            termino_busqueda = formulario.cleaned_data['termino_busqueda']
            resultados = Cancion.objects.filter(titulo__icontains=termino_busqueda)
    else:
        formulario = BuscarFormulario()

    return render(request, 'Mi_Aplicacion/buscar.html', {'formulario': formulario, 'resultados': resultados})
