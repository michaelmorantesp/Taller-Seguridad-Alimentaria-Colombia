# analisis_manual.py
# Intento de análisis SIN Docker - Experimentar errores

import pandas as pd

print("="*50)
print("INTENTO DE ANÁLISIS SIN DOCKER")
print("="*50)

# Intentar pdfplumber
print("\n[1] Probando pdfplumber...")
try:
    import pdfplumber
    print("    ✓ pdfplumber importado correctamente")
    with pdfplumber.open("WFP_Colombia_2024.pdf") as pdf:
        print(f"    ✓ PDF cargado: {len(pdf.pages)} páginas")
        tablas_encontradas = 0
        for i, page in enumerate(pdf.pages[:10]):
            tables = page.extract_tables()
            if tables:
                tablas_encontradas += len(tables)
        print(f"    ✓ Tablas encontradas (primeras 10 págs): {tablas_encontradas}")
except ImportError:
    print("    ✗ ERROR: pdfplumber no está instalado")
    print("      Ejecute: pip install pdfplumber")
except FileNotFoundError:
    print("    ✗ ERROR: No se encontró WFP_Colombia_2024.pdf")
    print("      Descárguelo de: https://es.wfp.org/publicaciones")
except Exception as e:
    print(f"    ✗ ERROR: {e}")

# Intentar tabula
print("\n[2] Probando tabula-py...")
try:
    import tabula
    print("    ✓ tabula-py importado correctamente")
    tables = tabula.read_pdf("WFP_Colombia_2024.pdf", pages="1", silent=True)
    print(f"    ✓ Tablas en página 1: {len(tables)}")
except ImportError:
    print("    ✗ ERROR: tabula-py no está instalado")
    print("      Ejecute: pip install tabula-py")
except Exception as e:
    print(f"    ✗ ERROR (¿Java instalado?): {e}")
    print("      tabula-py requiere Java. Descárguelo de: https://adoptium.net/")

# Intentar DBF
print("\n[3] Probando dbfread para archivos DANE...")
try:
    from dbfread import DBF
    import os
    print("    ✓ dbfread importado correctamente")
    
    if os.path.exists("datos_dane"):
        archivos_dbf = [f for f in os.listdir("datos_dane") if f.lower().endswith('.dbf')]
        if archivos_dbf:
            for archivo in archivos_dbf[:3]:  # Primeros 3
                try:
                    table = DBF(f"datos_dane/{archivo}", encoding='latin-1')
                    df = pd.DataFrame(iter(table))
                    print(f"    ✓ {archivo}: {len(df):,} registros, {len(df.columns)} columnas")
                except Exception as e:
                    print(f"    ✗ {archivo}: {e}")
        else:
            print("    ✗ No hay archivos .dbf en datos_dane/")
    else:
        print("    ✗ No existe la carpeta datos_dane/")
        print("      Descargue los microdatos de: https://microdatos.dane.gov.co/")
except ImportError:
    print("    ✗ ERROR: dbfread no está instalado")
    print("      Ejecute: pip install dbfread")

print("\n" + "="*50)
print("RESULTADO DEL INTENTO")
print("="*50)
print("\nPreguntas para reflexionar:")
print("1. ¿Funcionaron todas las librerías?")
print("2. ¿Sus compañeros tuvieron los mismos resultados?")
print("3. ¿Cuánto tiempo tomó intentar que todo funcionara?")
print("4. ¿Cómo garantizaría que su código funcione en otro computador?")
