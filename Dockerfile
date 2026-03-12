# Dockerfile
# Ambiente completo para análisis de datos no estructurados

FROM python:3.11-slim

# Instalar Java (necesario para tabula-py)
RUN apt-get update && apt-get install -y \
    default-jre \
    && rm -rf /var/lib/apt/lists/*

# Establecer directorio de trabajo
WORKDIR /app

# Copiar archivo de dependencias
COPY requirements.txt .

# Actualizar pip
RUN pip install --upgrade pip

# Instalar dependencias de Python (numpy se instala primero automáticamente)
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo el proyecto
COPY . .

# Crear carpeta para resultados
RUN mkdir -p resultados

# Comando por defecto
CMD ["python", "analisis_docker.py"]
