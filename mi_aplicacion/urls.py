from mi_aplicacion import views
from django.urls import path

urlpatterns = [
    path('inicio/', views.inicio, name='inicio'),
    path('Artista/', views.artistas_formulario, name='Artistas'),  
    path('Album/', views.album_formulario, name='Album'),
    path('Cancion/', views.cancion_formulario, name='Cancion'),
    path('buscar/', views.buscar, name='buscar'),
]