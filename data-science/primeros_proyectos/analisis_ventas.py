#Análisis de ventas, Proyecto 2, 21 Ago 25, Claude Sonnet
import pandas as pd
import numpy as np

print ("====ANÁLISIS DE VENTAS MENSUALES====")

#Crear datos de ventas de una farmacia
ventas_farmacia = pd.DataFrame ({
    'mes': ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio'],
    'medicinas_vendidas': [120, 95, 140, 110, 165, 180],
    'ingresos': [24000, 19000, 28000, 22000, 33000, 36000]
})

print ("Datos de ventas:")
print (ventas_farmacia)

print ("\n--- ANÁLISIS BÁSICO ---")
print ("Total de medicinas vendidas:", ventas_farmacia['medicinas_vendidas'].sum())
print ("Promedio de ingresos mensuales:", ventas_farmacia['ingresos'].mean())
print ("Mes con más ventas:", ventas_farmacia.loc[ventas_farmacia['medicinas_vendidas'].idxmax(), 'mes'])
