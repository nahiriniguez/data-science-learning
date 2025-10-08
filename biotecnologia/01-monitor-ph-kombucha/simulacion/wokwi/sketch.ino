// Monitor de pH y Temperatura para Fermentación
// Proyecto: Kombucha casera

#include <LiquidCrystal.h>

// Inicializar LCD (RS, E, D4, D5, D6, D7)
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

// Pines de sensores
const int pinTemp = A0;     // TMP36
const int pinPH = A1;       // Simulador de pH

void setup() {
  // Inicializar LCD
  lcd.begin(16, 2);
  lcd.print("Monitor Kombucha");
  delay(2000);
  lcd.clear();
  
  // Inicializar comunicación serial
  Serial.begin(9600);
}

void loop() {
  // ===== LEER TEMPERATURA =====
  int lecturaTemp = analogRead(pinTemp);
  float voltajeTemp = lecturaTemp * (5.0 / 1023.0);
  float temperaturaCelsius = (voltajeTemp - 0.5) * 100.0;
  
  // ===== LEER pH (SIMULADO) =====
  int lecturaPH = analogRead(pinPH);
  // Convertir a escala pH (0-14)
  // 0V = pH 0, 5V = pH 14
  float pH = (lecturaPH * 14.0) / 1023.0;
  
  // ===== MOSTRAR EN LCD =====
  lcd.setCursor(0, 0);
  lcd.print("Temp: ");
  lcd.print(temperaturaCelsius, 1);
  lcd.print("C");
  
  lcd.setCursor(0, 1);
  lcd.print("pH: ");
  lcd.print(pH, 2);
  
  // Indicador de zona óptima
  if (pH >= 2.5 && pH <= 4.5) {
    lcd.print(" OK");
  } else if (pH > 4.5 && pH <= 5.0) {
    lcd.print(" !!");
  } else {
    lcd.print(" XX");
  }
  
  // ===== ENVIAR A MONITOR SERIAL =====
  Serial.print("Temperatura: ");
  Serial.print(temperaturaCelsius);
  Serial.print(" C | pH: ");
  Serial.println(pH);
  
  delay(1000); // Actualizar cada segundo
}