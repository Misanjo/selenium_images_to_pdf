# Create PDF

## Descripción
Este programa utiliza Selenium para capturar imágenes de un Flipbook y hacer clic en las páginas. Se puede usar tanto con parámetros individuales como a través de un archivo CSV.

## Requisitos
* Python 3.x
* Librerías:
    * selenium
    * Pillow
    * csv
* Además, necesita el controlador de Chrome (chromedriver).

## Instalación
1) Clonar el repositorio o descargar los archivos.
2) Instalar las dependencias necesarias:
``pip install selenium pillow``
3) Descargar el chromedriver y asegúrate de que esté en tu PATH o actualiza la ruta en el código.

## Uso
El programa puede ejecutarse proporcionando parámetros individuales o un archivo CSV que contenga múltiples configuraciones.

### Uso con Parámetros Individuales
``python capture_flipbook.py --url <url_del_flipbook> --iterations <numero_de_iteraciones> --folder <ruta_a_la_carpeta>``
* --url: URL del Flipbook.
* --iterations: Número de iteraciones para capturar imágenes.
* --folder: Carpeta donde se guardarán las imágenes PNG.
### Uso con Archivo CSV
``python capture_flipbook.py --csv_file <ruta_al_csv>``
* --csv_file: Archivo CSV que contiene la URL, el número de iteraciones y la carpeta.
El archivo CSV debe tener el siguiente formato:

````csv
url_del_flipbook_1;numero_de_iteraciones_1;carpeta_1
url_del_flipbook_2;numero_de_iteraciones_2;carpeta_2
...
````