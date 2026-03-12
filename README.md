Taller Seguridad Alimentaria Colombia
Análisis de Datos No Estructurados con Docker, PySpark y Python

Autor: Michael Morantes
Universidad: Universidad Santo Tomás (USTA)
Asignatura: Estadística / Análisis de Datos
Año: 2026

Descripción del proyecto

Este proyecto analiza el problema de la seguridad alimentaria en Colombia utilizando fuentes de datos estructuradas y no estructuradas. Se emplea un informe en formato PDF del Programa Mundial de Alimentos (WFP) junto con microdatos de la Encuesta de Calidad de Vida (ECV) 2024 del DANE. El objetivo es extraer información relevante, estructurarla y analizarla estadísticamente para identificar patrones de inseguridad alimentaria en el país.

El proyecto también demuestra cómo Docker y Docker Compose permiten crear un ambiente reproducible para el análisis de datos. En lugar de instalar manualmente múltiples dependencias (Python, Java, librerías de PDFs, DBF, etc.), el contenedor Docker configura automáticamente el entorno necesario para ejecutar el análisis.

Finalmente, el análisis se realiza utilizando Python, PySpark y Jupyter Notebook, permitiendo explorar grandes volúmenes de datos y generar estadísticas descriptivas y visualizaciones sobre la situación de inseguridad alimentaria en Colombia.

Instrucciones para ejecutar con Docker
1. Clonar el repositorio
git clone https://github.com/usuario/taller-seguridad-alimentaria.git
cd taller-seguridad-alimentaria
2. Descargar los datos

Descargue manualmente las siguientes fuentes y colóquelas en las carpetas correspondientes.

PDF WFP

Evaluación de seguridad alimentaria para población colombiana 2024

Descargar aquí:

https://es.wfp.org/publicaciones/evaluacion-de-la-seguridad-alimentaria-para-la-poblacion-colombiana-2024

Guardar como:

WFP_Colombia_2024.pdf
Microdatos DANE – ECV 2024

Descargar desde:

https://microdatos.dane.gov.co/index.php/catalog/861/get-microdata

Descargar al menos:

Datos_vivienda

Caracteristicas_composicion_hogar

Condiciones_vida_hogar

Descomprimir en la carpeta:

datos_dane/
3. Construir y ejecutar con Docker
docker-compose up

La primera ejecución puede tardar varios minutos porque descarga la imagen de PySpark + Jupyter.

4. Abrir Jupyter Notebook

Abrir en el navegador:

http://localhost:8888

Desde allí se puede ejecutar el notebook con el análisis.

Estructura del repositorio
taller-seguridad-alimentaria/

├── README.md
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
│
├── notebooks/
│   └── analisis.ipynb
│
├── datos_dane/
│   └── archivos .dbf
│
├── resultados/
│   ├── tablas_wfp/
│   └── graficos/
│
└── informe/
    └── informe.pdf