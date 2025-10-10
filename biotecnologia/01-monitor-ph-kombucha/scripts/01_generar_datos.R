# ============================================================================
# GENERACIÓN DE DATOS SINTÉTICOS DE FERMENTACIÓN
# Basado en literatura científica de kombucha
# ============================================================================

library(dplyr)
library(ggplot2)

set.seed(123) #Reproducibilidad

# Parámetros del experimento
dias_totales <- 14
mediciones_por_dia <- 24 #Cada hora
total_mediciones <- dias_totales * mediciones_por_dia #336 mediciones totales

# Generar timestamps
tiempo_horas <- seq(0, dias_totales * 24, length.out = total_mediciones)
tiempo_dias <- tiempo_horas / 24

# MODELO DE pH (descenso logístico)
# Literatura: pH inicial 4.5, final 2.5 - 3.0
ph_inicial <- 4.5
ph_final <- 2.8
tasa_cambio <- 0.5
punto_inflexion <- 5 #Día 5 = mayor cambio

ph_teorico <- ph_final + (ph_inicial - ph_final) / 
  (1 + exp(tasa_cambio * (tiempo_dias - punto_inflexion)))

# Agregar ruido realista (variación de medición)
ph_medio <- ph_teorico + rnorm(total_mediciones, 0, 0.08)

# MODELO DE TEMPERATURA (variación día/noche + tendencia)
temp_base <- 25
amplitud_diaria <- 3
temp_teorica <- temp_base +
                amplitud_diaria * sin(tiempo_horas * 2 * pi / 24) +
                0.5 * sin(tiempo_dias * pi / 7) #Variación semanal
temp_medida <- temp_teorica + rnorm(total_mediciones, 0, 0.3)

# CREAR DATASET COMPLETO
datos_fermentacion <- data.frame(
  timestamp = Sys.time() + tiempo_horas * 3600,
  dia = tiempo_dias,
  hora = tiempo_horas %% 24,
  pH = ph_medio,
  temperatura_C = temp_medida,
  fase = case_when(
    tiempo_dias < 3 ~ "Lag (adaptación)",
    tiempo_dias < 7 ~ "Exponencial (activa)",
    tiempo_dias < 12 ~ "Estacionaria (maduración)",
    TRUE ~ "Declive (final)"
  )
)

# Agregar variables calculadas
datos_fermentacion <- datos_fermentacion %>%
  mutate(
    acidez_relativa = (ph_inicial - pH) / (ph_inicial - ph_final),
    temp_optima = between (temperatura_C, 22, 28),
    pH_optimo = between(pH, 2.5, 4.5)
  )

# GUARDAR DATOS
write.csv(datos_fermentacion,
          "~/all-projects/biotecnologia/01-monitor-ph-kombucha/datos/fermentacion_kombucha_simulada.csv",
          row.names = FALSE) #Sin números de fila

#Vista previa
head(datos_fermentacion)
summary(datos_fermentacion)

print("¡Datos generados exitosamente!")
print(paste("Total de mediciones:", nrow(datos_fermentacion)))