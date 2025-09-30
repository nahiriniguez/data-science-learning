# Mi primer script de análisis de datos
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print ("¡Hola! Este es mi primer script de data science")
print ("Elaborado el 19 de Agosto de 2025 gracias a la ayuda de Claude Sonnet 4.0")
print ("Python version funcionando correctamente")

#Crear datos de ejemplo
datos = pd.DataFrame ({
    'nombre': ['Ana', 'Luis', 'María', 'Carlos'],
    'edad': [25,30,35,28]
})

print ("\nMis primeros datos:") #\n es salto de línea
print (datos)

