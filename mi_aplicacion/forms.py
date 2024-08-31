from django import forms
from mi_aplicacion.models import Album, Artista, Cancion

class artistasFormulario(forms.Form):
    nombre = forms.CharField(max_length=100, label="Nombre del Artista")
    genero = forms.CharField(max_length=50, label="Género")
    pais = forms.CharField(max_length=50, label="País")
    orden_de_artista_BD = forms.IntegerField()

class AlbumFormulario(forms.Form):
    titulo = forms.CharField(max_length=100, label="Título del Álbum")
    artista_nombre = forms.CharField(max_length=100, label="Nombre del Artista")
    fecha_lanzamiento = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))


class CancionFormulario(forms.ModelForm):
    class Meta:
        model = Cancion
        fields = ['titulo', 'album', 'duracion']
        widgets = {
            'duracion': forms.TimeInput(attrs={'type': 'time'}),
        }

class BuscarFormulario(forms.Form):
    termino_busqueda = forms.CharField(max_length=100, label="Buscar")