PDF a JPG Converter

Este proyecto es una herramienta en Python que permite convertir archivos PDF a imágenes JPG mediante una interfaz gráfica con Tkinter.

Requisitos

Antes de ejecutar el script, asegúrate de tener instaladas las siguientes dependencias:

pip install pdf2image pillow tqdm

Además, en algunos sistemas operativos, es necesario instalar poppler. Puedes hacerlo con:

Ubuntu/Debian:

sudo apt install poppler-utils

Windows:

Descarga poppler desde aquí. https://pypi.org/project/pdf2image/

Extrae el archivo y agrega la ruta del binario a las variables de entorno.

Uso

Ejecuta el script Python.

Se abrirá una interfaz gráfica.

Selecciona los archivos PDF que deseas convertir.

Elige la carpeta donde deseas guardar las imágenes JPG.

El programa procesará los archivos y guardará cada página en formato JPG.

Recibirás una notificación cuando la conversión se complete.

Características

Interfaz gráfica intuitiva con Tkinter.

Convierte archivos PDF a imágenes JPG.

Soporta documentos de varias páginas.

Permite elegir la carpeta de salida.
