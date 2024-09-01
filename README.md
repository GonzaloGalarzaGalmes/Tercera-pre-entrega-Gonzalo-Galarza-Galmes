Tercera Pre-Entrega - Gonzalo Galarza Galmes
Este es un proyecto desarrollado en Django que permite gestionar una base de datos de artistas, álbumes y canciones.

Requisitos Previos
- Antes de ejecutar el proyecto, debe tener instalado:
Python 3.x.x (yo lo hice en la versión 3.12.4).
Django 4.x (yo lo hice con la versión 4.2).
Un entorno virtual configurado.
Instalación:
Tienes que clonar el repositorio: "git clone https://github.com/GonzaloGalarzaGalmes/Tercera-pre-entrega-Gonzalo-Galarza-Galmes.git".
Navegar en el directorio del proyecto: "cd Tercera-pre-entrega-Gonzalo-Galarza-Galmes"

- Crear el entorno virtual: 
python -m venv venv
source venv/Scripts/activate(estos dos ultimas son de Windows).
o sino para linux o MacOs: source venv/bin/activate.

- Seguimos instalando la dependencia: pip install -r requirements.txt.

- Realizamos las migraciones(para la Base de Datos): python manage.py migrate


- Iniciamos el servidor: python manage.py runserver.

- Y por ultimo en el navegador ponemos esto: http://127.0.0.1:8000/

- Dentro de la aplicacion: lo que para poder navegar en esta aplicación pones esto en la parte de url(paso anterior, donde te hice poner
"http://127.0.0.1:8000/") le agregas esto: http://127.0.0.1:8000/mi_aplicacion/inicio/

A partir de ello te aparece una pagina(muy simple) en la cual al principio Funcionalidades de la Aplicación
Página de Inicio: Arriba a la derecha, verás cinco botones: Inicio, Artistas, Álbum, Canción, y Buscar.

Inicio: Te lleva a la página de inicio.
Artistas: Te muestra un formulario para agregar un artista, incluyendo el nombre, género, país, y el orden de ingreso en la base de datos.
Álbum: Muestra un formulario para agregar un álbum, que incluye el nombre del álbum, el nombre del artista (nombre artístico) y la fecha de lanzamiento.
Canción: Permite agregar una canción. Debes seleccionar el álbum desde un desplegable que muestra las opciones en el formato "Album object(x)",
donde "x" es el ID del álbum que puedes verificar en la base de datos (tabla mi_aplicacion_album). Además, puedes ingresar la duración de la canción en segundos (la base de datos la almacenará en milisegundos).


Si querés ingresar a la parte de admin simplementes pones en la url esto: http://127.0.0.1:8000/admin/
Usuario principal:
Username: Gonzalo
Password: LilPeep21

Usuario secundario:
Username: Diego
Password: LilPeep21

La cuenta principal tiene todos los permisos de administración, mientras que la cuenta secundaria tiene permisos limitados para visualización.

