# Taller Seguridad Alimentaria Colombia  
## Análisis de Datos No Estructurados con Docker, PySpark y Python

**Autor:** Michael Morantes  
**Universidad:** Universidad Santo Tomás (USTA) **Asignatura:** Machine Learning con pyspark y docker**Asignatura:** Machine Learning con PySpark y Docker  
**Año:** 2026  

---

# Descripción del proyecto

Este proyecto analiza el problema de la **seguridad alimentaria en Colombia** utilizando fuentes de datos estructuradas y no estructuradas. Se emplea un informe en formato PDF del Programa Mundial de Alimentos (WFP) junto con microdatos de la **Encuesta de Calidad de Vida (ECV) 2024 del DANE**. El objetivo es extraer información relevante, estructurarla y analizarla estadísticamente para identificar patrones de inseguridad alimentaria en el país.

El proyecto también demuestra cómo **Docker y Docker Compose** permiten crear un ambiente reproducible para el análisis de datos. En lugar de instalar manualmente múltiples dependencias (Python, Java, librerías de PDFs, DBF, etc.), el contenedor Docker configura automáticamente el entorno necesario para ejecutar el análisis.

Finalmente, el análisis se realiza utilizando **Python, PySpark y Jupyter Notebook**, permitiendo explorar grandes volúmenes de datos y generar estadísticas descriptivas y visualizaciones sobre la situación de inseguridad alimentaria en Colombia.

---

# Instrucciones para ejecutar con Docker

## 1. Clonar el repositorio

```bash
git clone https://github.com/usuario/taller-seguridad-alimentaria.git
cd taller-seguridad-alimentaria
```

## 2. Descargar los datos

Descargue manualmente las siguientes fuentes y colóquelas en las carpetas correspondientes.

### PDF WFP

**Evaluación de seguridad alimentaria para población colombiana 2024**

Descargar aquí:

https://es.wfp.org/publicaciones/evaluacion-de-la-seguridad-alimentaria-para-la-poblacion-colombiana-2024

Guardar como:

```
WFP_Colombia_2024.pdf
```

### Microdatos DANE – ECV 2024

Descargar desde:

https://microdatos.dane.gov.co/index.php/catalog/861/get-microdata

Descargar al menos:

- Datos_vivienda  
- Caracteristicas_composicion_hogar  
- Condiciones_vida_hogar  

Descomprimir en la carpeta:

```
datos_dane/
```

## 3. Construir y ejecutar con Docker

```bash
docker-compose up
```

La primera ejecución puede tardar varios minutos porque descarga la imagen de **PySpark + Jupyter**.

## 4. Abrir Jupyter Notebook

Abrir en el navegador:

```
http://localhost:8888
```

Desde allí se puede ejecutar el notebook con el análisis.

---

# Estructura del repositorio

```
taller-seguridad-alimentaria/

taller-seguridad-alimentaria/
├── README.md                    # Descripción del proyecto
├── Dockerfile                   # Su Dockerfile funcional
├── docker-compose.yml           # Su archivo Compose
├── requirements.txt             # Dependencias de Python
├── datos/                       # Carpeta para datos (NO subir datos)
│   └── .gitkeep                
├── notebooks/
│   └── analisis_completo.ipynb  # Su notebook con el análisis
├── resultados/
│   ├── datos_combinados_wfp_dane.csv
│   ├── grafico_inseguridad_departamentos.png
│   └── grafico_correlaciones.png
└── informe/
    └── informe_seguridad_alimentaria.pdf

# Principales hallazgos

1. La **media nacional de inseguridad alimentaria es 30.2%**, lo que indica que aproximadamente **3 de cada 10 hogares** presentan dificultades para acceder de forma estable a alimentos.

2. Existe una **alta variabilidad entre departamentos** (desviación estándar de 10.9%), lo que evidencia importantes desigualdades territoriales en Colombia.

3. **La Guajira presenta el nivel más alto de inseguridad alimentaria (59%)**, seguido por **Chocó (52%)**, mostrando una fuerte concentración del problema en regiones históricamente vulnerables.

4. **Bogotá D.C. tiene el nivel más bajo (13%)**, lo que refleja diferencias significativas entre áreas urbanas con mayor infraestructura y regiones con mayores limitaciones socioeconómicas.

5. La clasificación del WFP muestra que:
   - 7 departamentos presentan **inseguridad baja**
   - 6 presentan **nivel medio**
   - 5 presentan **nivel alto**
   - 3 presentan **nivel medio-alto**
   - 2 presentan **niveles muy altos**

6. En general, los resultados sugieren que la inseguridad alimentaria en Colombia **no está distribuida de forma uniforme**, sino que se concentra en regiones con mayores niveles de pobreza, aislamiento geográfico y menor acceso a servicios.

```