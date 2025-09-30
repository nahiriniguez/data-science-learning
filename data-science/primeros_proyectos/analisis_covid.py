import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("=== ANÁLISIS DE DATOS COVID-19 REALES ===")
print("Proyecto: Primeros pasos con datasets externos")
print("="*50)

# PASO 1: CARGAR DATOS REALES DE COVID-19
print("\n1. DESCARGANDO DATOS REALES...")

# URL del dataset global de COVID-19 (Johns Hopkins University)
url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"

try:
    # Cargar datos directamente desde internet
    covid_data = pd.read_csv(url)
    print(f"✅ Datos cargados exitosamente: {covid_data.shape[0]} países/regiones")
    print(f"   Columnas de fechas: {covid_data.shape[1] - 4}")
    
except Exception as e:
    print(f"❌ Error cargando datos: {e}")
    print("💡 Verifica tu conexión a internet")

# PASO 2: EXPLORAR LA ESTRUCTURA
print("\n2. EXPLORANDO LA ESTRUCTURA DE DATOS...")
print("Primeras 5 filas:")
print(covid_data.head())

print(f"\nDimensiones del dataset: {covid_data.shape}")
print(f"Columnas: {list(covid_data.columns[:10])}...")  # Primeras 10 columnas

# PASO 3: ANÁLISIS DE PAÍSES ESPECÍFICOS
print("\n3. ANÁLISIS POR PAÍSES...")

# Países de interés (incluyendo México)
paises_interes = ['Mexico', 'US', 'Spain', 'Italy', 'Germany']

# Función para obtener datos de un país
def obtener_datos_pais(datos, pais):
    """Extrae los datos de casos confirmados para un país específico"""
    pais_data = datos[datos['Country/Region'] == pais]
    
    if len(pais_data) == 0:
        print(f"⚠️ No se encontraron datos para {pais}")
        return None
    
    # Si hay múltiples regiones, sumar todas
    if len(pais_data) > 1:
        # Sumar todas las regiones del país
        casos_totales = pais_data.iloc[:, 4:].sum()
    else:
        # Solo una región
        casos_totales = pais_data.iloc[:, 4:].iloc[0]
    
    return casos_totales

# PASO 4: PROCESAMIENTO Y LIMPIEZA
print("\n4. PROCESANDO DATOS...")

# Crear DataFrame para almacenar datos procesados
datos_procesados = pd.DataFrame()

for pais in paises_interes:
    casos = obtener_datos_pais(covid_data, pais)
    if casos is not None:
        datos_procesados[pais] = casos

# Convertir índices (fechas) a datetime
datos_procesados.index = pd.to_datetime(datos_procesados.index)

print(f"Datos procesados: {datos_procesados.shape}")
print("Últimos 5 días de datos:")
print(datos_procesados.tail())

# PASO 5: ANÁLISIS ESTADÍSTICO
print("\n5. ANÁLISIS ESTADÍSTICO...")

# Casos totales por país (último día)
casos_finales = datos_procesados.iloc[-1].sort_values(ascending=False)
print("\nCasos totales confirmados (último reporte):")
for pais, casos in casos_finales.items():
    print(f"{pais}: {casos:,.0f} casos")

# Calcular casos nuevos diarios
print("\n6. CALCULANDO CASOS NUEVOS DIARIOS...")
casos_nuevos = datos_procesados.diff()  # Diferencia día a día

# Promedio de casos nuevos en últimos 7 días
promedio_7_dias = casos_nuevos.tail(7).mean()
print("\nPromedio de casos nuevos (últimos 7 días):")
for pais, promedio in promedio_7_dias.sort_values(ascending=False).items():
    print(f"{pais}: {promedio:.0f} casos/día")

# PASO 7: VISUALIZACIONES
print("\n7. CREANDO VISUALIZACIONES...")

# GRÁFICO 1: Evolución temporal de casos acumulados
plt.figure(figsize=(14, 8))
for pais in datos_procesados.columns:
    plt.plot(datos_procesados.index, datos_procesados[pais], 
             marker='o', label=pais, linewidth=2, markersize=3)

plt.title('Evolución de Casos COVID-19 Confirmados por País', fontsize=16, fontweight='bold')
plt.xlabel('Fecha', fontsize=12)
plt.ylabel('Casos Confirmados Acumulados', fontsize=12)
plt.legend()
plt.grid(True, alpha=0.3)
plt.xticks(rotation=45)
plt.yscale('log')  # Escala logarítmica para mejor visualización
plt.tight_layout()
plt.show()

# GRÁFICO 2: Casos totales actuales (barras)
plt.figure(figsize=(10, 6))
colores = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7']
barras = plt.bar(casos_finales.index, casos_finales.values, 
                color=colores[:len(casos_finales)], edgecolor='black', linewidth=1.5)

# Agregar valores encima de las barras
for i, valor in enumerate(casos_finales.values):
    plt.text(i, valor + valor*0.01, f'{valor:,.0f}', 
            ha='center', fontweight='bold', fontsize=10)

plt.title('Casos COVID-19 Confirmados Totales por País', fontsize=16, fontweight='bold')
plt.ylabel('Casos Confirmados', fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.show()

# GRÁFICO 3: Casos nuevos diarios (últimos 30 días)
plt.figure(figsize=(14, 8))
ultimos_30_dias = casos_nuevos.tail(30)

for pais in ultimos_30_dias.columns:
    plt.plot(ultimos_30_dias.index, ultimos_30_dias[pais], 
             marker='s', label=pais, linewidth=2, markersize=4, alpha=0.8)

plt.title('Casos Nuevos Diarios COVID-19 (Últimos 30 Días)', fontsize=16, fontweight='bold')
plt.xlabel('Fecha', fontsize=12)
plt.ylabel('Casos Nuevos por Día', fontsize=12)
plt.legend()
plt.grid(True, alpha=0.3)
plt.xticks(rotation=45)
plt.axhline(y=0, color='black', linestyle='-', alpha=0.3)
plt.tight_layout()
plt.show()

# PASO 8: ANÁLISIS MÉDICO
print("\n8. ANÁLISIS DESDE PERSPECTIVA MÉDICA...")

# Tasa de crecimiento promedio
print("\nTASAS DE CRECIMIENTO:")
for pais in datos_procesados.columns:
    # Calcular tasa de crecimiento (últimos 7 vs anteriores 7 días)
    ultimos_7 = datos_procesados[pais].tail(7).mean()
    anteriores_7 = datos_procesados[pais].tail(14).head(7).mean()
    
    if anteriores_7 > 0:
        tasa_crecimiento = ((ultimos_7 - anteriores_7) / anteriores_7) * 100
        tendencia = "📈 Aumentando" if tasa_crecimiento > 0 else "📉 Disminuyendo"
        print(f"{pais}: {tasa_crecimiento:+.1f}% {tendencia}")

print("\n" + "="*50)
print("✅ ANÁLISIS COMPLETADO")
print("📊 Revisa los gráficos generados")
print("📈 Datos actualizados desde Johns Hopkins University")
print("🔬 Aplicaste: pandas, matplotlib, análisis estadístico")
print("="*50)
