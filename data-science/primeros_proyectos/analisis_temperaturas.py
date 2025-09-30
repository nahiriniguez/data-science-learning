import pandas as pd
import numpy as np

print ("=== ANÁLISIS DE TEMPERATURAS DE PACIENTES ===")

#Simulador temperaturas de pacientes durante una semana

np.random.seed (123)
temperaturas = pd.DataFrame ({
   'dia': ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo'],
   'paciente_1': np.round(np.random.normal(36.5, 0.5, 7),1),
   'paciente_2': np.round(np.random.normal(37.2, 0.8, 7),1),
   'paciente_3': np.round(np.random.normal(36.8, 0.3, 7),1)
})

print ("Temperaturas por día")
print (temperaturas)


print ("\n--- ANÁLISIS ESTADÍSTICO ---")

#Temperatura promedio por paciente
for paciente in ['paciente_1', 'paciente_2', 'paciente_3']:
	promedio = temperaturas[paciente].mean()
	print(f"Temperatura promedio {paciente}: {promedio:.2f}°C")

#Detectar fiebre (>37.7°C)
print("\n--- DETECCIÓN DE FIEBRE ---")
for paciente in ['paciente_1', 'paciente_2', 'paciente_3']:
	fiebre = temperaturas[temperaturas[paciente] > 37.5]
	if len(fiebre) > 0:
		print(f"{paciente} tuvo fiebre:")
		print(fiebre[['dia', paciente]])
	else:
		print(f"{paciente}: Sin fiebre esta semana")
		
# EJERCICIOS DE FILTRADO 

print ("\n=== EJERCICIOS DE FILTRADO ===")

#1. Temperaturas bajas (hipotermia) - menores a 36.0°C
print("\n1. TEMPERATURAS BAJAS (<36.0)°C")
for paciente in ['paciente_1', 'paciente_2', 'paciente_3']:
	bajas = temperaturas[temperaturas[paciente]<36.0]
	if len(bajas) > 0:
		print(f"{paciente} tuvo hipotermia:")
		print(bajas[['dia',paciente]])
	else:
		print(f"{paciente}: Sin temperaturas bajas")
		
#2. Temperaturas exactas (ejemplo: exactamente 36.5)
print ("\n2. TEMPERATURAS EXACTAS (36.5°C)")
exactas = temperaturas[temperaturas['paciente_2'] == 36.5]
print("Días donde paciente_2 tuvo exactamente 36.5°C:")
print(exactas[['dia', 'paciente_2']])

#3. Rango de temperaturas (entre 37.0 y 37.5°C - Zona de alerta)
print("\n3. ZONA DE ALERTA (37.0°C - 37.5°C)")
zona_alerta = temperaturas[(temperaturas['paciente_2'] >= 37.0) & 
        (temperaturas['paciente_2'] <= 37.5)]
print("Paciente_2 en zona de alerta:")
print(zona_alerta[['dia', 'paciente_2']])

#4. Comparar pacientes (paciente_1 vs paciente_3)
print ("\n4. COMPARACIÓN ENTRE PACIENTES")
comparacion = temperaturas[temperaturas['paciente_1'] > temperaturas['paciente_3']]
print("Días donde paciente_1 tuvo mayor temperatura que paciente_3:")
print(comparacion[['dia', 'paciente_1', 'paciente_3']])

#5. Múltiples condiciones - Días especificos con fiebre
print("\n5. FIEBRE EN DÍAS ESPECÍFICOS")
fiebre_weekend = temperaturas[(temperaturas['paciente_2'] > 37.5) & 
                              ((temperaturas['dia'] == 'Sábado') |
                              (temperaturas['dia'] == 'Domingo'))]
print("Paciente_2 con fiebre en fin de semana:")
print(fiebre_weekend[['dia', 'paciente_2']])

#Estadísticas de filtros
print("\n6. ESTADÍSTICAS GLOBALES")
total_fiebres = len(temperaturas[(temperaturas['paciente_1'] > 37.5) |
                                 (temperaturas['paciente_2'] > 37.5) |
                                 (temperaturas['paciente_3'] > 37.5)])
print(f"Total de casos de fiebre esta semama: {total_fiebres}")                                 


# IMPORTAT MATPLOTLIB
import matplotlib.pyplot as plt


print("\n" + "=" *50)
print("VISUALIZACIONES CON MATPLOTLIB")
print("="*50)

#GRÁFICO 1: Líneas de temperatura por paciente
plt.figure(figsize=(12,6))
plt.plot(temperaturas['dia'], temperaturas['paciente_1'], marker='o', label='Paciente 1', linewidth=2)
plt.plot(temperaturas['dia'], temperaturas['paciente_2'], marker='s', label='Paciente 2', linewidth=2)
plt.plot(temperaturas['dia'], temperaturas['paciente_3'], marker='^', label='Paciente 3', linewidth=2)

# Línea de referencia para fiebre
plt.axhline (y=37.5, color='red', linestyle='--', alpha=0.7, label='Límite fiebre (37.5°C)')

plt.title('Temperaturas de Pacientes Durante la Semana', fontsize=16, fontweight='bold')
plt.xlabel('Día de la Semana', fontsize=12)
plt.ylabel('Temperatura (°C)', fontsize=12)
plt.legend(fontsize=10)
plt.grid(True, alpha=1)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()



#GRÁFICO 2: Gráfico de barras - Promedios
promedios = [temperaturas['paciente_1'].mean(),
             temperaturas['paciente_2'].mean(),
             temperaturas['paciente_3'].mean()]

pacientes = ['Paciente 1', 'Paciente 2', 'Paciente 3']
plt.figure(figsize=(8,6))
barras = plt.bar(pacientes, promedios, color=['lightblue', 'lightcoral', 'lightgreen'],
                        edgecolor='black', linewidth=1.5)
                        
# Agregar valores encima de las barras
for i, valor in enumerate(promedios):
    plt.text(i, valor + 0.5, f'{valor:.2f}°C', ha='center', fontweight='bold')
    
plt.title('Temperatura Promedipo por Paciente', fontsize=16, fontweight='bold')
plt.ylabel('Temperatura Promedio (°C)', fontsize=12)
plt.axhline(y=37.5, color='red', linestyle='--', alpha=0.7, label='Limite fiebre')
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.show()


#GRÁFICO 3: Histograma - Distribución de temperaturas
plt.figure(figsize=(10,6))
plt.hist(temperaturas['paciente_1'], bins=15, alpha=0.7, label='Paciente 1', color='lightblue')
plt.hist(temperaturas['paciente_2'], bins=15, alpha=0.7, label='Paciente 2', color='lightcoral')
plt.hist(temperaturas['paciente_3'], bins=15, alpha=0.7, label='Paciente 3', color='lightgreen')

plt.axvline(x=37.5, color='red', linestyle='--', linewidth=2, label='Límite fiebre')
plt.title('Distribución de Temperaturas por Paciente', fontsize=16, fontweight='bold')
plt.xlabel('Temperatura (°C)', fontsize=12)
plt.ylabel('Frecuencia', fontsize=12)
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

print("¡Gráficos generados exitosamente")
print("Revisa las ventanas que se abrieron para ver las visualizaciones.")
