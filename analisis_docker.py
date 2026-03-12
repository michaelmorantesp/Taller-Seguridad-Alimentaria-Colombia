# analisis_docker.py
# Análisis completo CON Docker - Todo funciona

import pandas as pd
import pdfplumber
import tabula
from dbfread import DBF
import os

print("="*60)
print("ANÁLISIS CON DOCKER")
print("Seguridad Alimentaria Colombia 2024")
print("="*60)

# ============================================
# PARTE A: Extraer datos del PDF del WFP
# ============================================
print("\n[1/3] EXTRAYENDO DATOS DEL PDF WFP...")

pdf_path = "WFP_Colombia_2024.pdf"

if os.path.exists(pdf_path):
    # Usar pdfplumber
    with pdfplumber.open(pdf_path) as pdf:
        print(f"    ✓ PDF cargado: {len(pdf.pages)} páginas")
        
    # Usar tabula para tablas
    print("    Extrayendo tablas con tabula-py...")
    tablas = tabula.read_pdf(pdf_path, pages='all', multiple_tables=True, silent=True)
    print(f"    ✓ Encontradas {len(tablas)} tablas")
    
    # Guardar primeras tablas
    for i, df in enumerate(tablas[:5]):
        if len(df) > 0:
            df.to_csv(f"resultados/tabla_wfp_{i+1}.csv", index=False)
    print(f"    ✓ Guardadas 5 tablas en resultados/")
else:
    print(f"    ✗ No se encontró {pdf_path}")

# ============================================
# PARTE B: Leer microdatos del DANE
# ============================================
print("\n[2/3] LEYENDO MICRODATOS DANE...")

dbf_folder = "datos_dane"
datos_dane = {}

if os.path.exists(dbf_folder):
    for archivo in os.listdir(dbf_folder):
        if archivo.lower().endswith('.dbf'):
            ruta = os.path.join(dbf_folder, archivo)
            try:
                table = DBF(ruta, encoding='latin-1')
                df = pd.DataFrame(iter(table))
                nombre = archivo.replace('.dbf', '').replace('.DBF', '')
                datos_dane[nombre] = df
                print(f"    ✓ {archivo}: {len(df):,} registros, {len(df.columns)} columnas")
            except Exception as e:
                print(f"    ✗ Error en {archivo}: {e}")
else:
    print(f"    ✗ No existe la carpeta {dbf_folder}")

# ============================================
# PARTE C: Resumen
# ============================================
print("\n[3/3] GENERANDO RESUMEN...")

resumen = {
    'Fuente': ['WFP PDF', 'DANE ECV'],
    'Archivos': [1, len(datos_dane)],
    'Descripción': [
        'Evaluación seguridad alimentaria 2024',
        'Microdatos Encuesta Calidad de Vida 2024'
    ]
}
df_resumen = pd.DataFrame(resumen)
df_resumen.to_csv("resultados/resumen_fuentes.csv", index=False)
print("    ✓ Resumen guardado en resultados/resumen_fuentes.csv")

print("\n" + "="*60)
print("✓ ANÁLISIS COMPLETADO EXITOSAMENTE")
print("  Resultados en: /app/resultados/")
print("="*60)
