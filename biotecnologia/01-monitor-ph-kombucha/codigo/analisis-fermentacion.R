# Mi primer                                                      biotecnólogico
# Simulación de fermentación de Kombucha

# Cargar librerías
library(ggplot2)
library(dplyr)
library(readr)

# Datos de fermentación
dias <- 1:14
ph_inicial <- 4.5
ph_datos <- ph_inicial - 0.15 + rnorm(14, 0, 0.1)
temperatura <- 25 + 2*sin(dias/7*pi) + rnorm(14, 0, 1)

# Crear dataset
fermentacion <- data.frame(
  dia = dias,
  pH = ph_datos,
  temperatura_C = temperatura,
  proceso = "fermentacion_kombucha"
)

# Ver primeras filas
head(fermentacion)

# Gráfico con ggplot2
ggplot(fermentacion, aes(x = dia, y =pH)) +
  geom_line(color = "darkblue", size = 1.5, linetype="dashed") +
  geom_point(color = "red", size = 4, alpha =0.7) +
  geom_hline(yintercept = 4.0, color = "green", linetype = "dotted") +
  labs(title = "Descanso de pH durante fermentación",
       subtitle = "Kombucha casera - 14 días",
       x = "Días de fermentación",
       y = "pH (escala logarítmica)",
       caption = "Datos simulados") +
  theme_classic() +
  theme(
    plot.title = element_text(size=16, face="bold"),
    axis.text = element_text(size=12)
  )
