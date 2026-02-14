#include <SPI.h>
#include <LoRa.h>
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);

void setup() {
  Serial.begin(9600);
  lcd.init();
  lcd.backlight();
  
  lcd.setCursor(0,0);
  lcd.print("LoRa SECURE-LINK");
  
  if (!LoRa.begin(433E6)) {
    lcd.setCursor(0,1);
    lcd.print("INIT FAILED!");
    while (1);
  }
  
  LoRa.setSpreadingFactor(10);
  LoRa.setSignalBandwidth(125E3);
  LoRa.setCodingRate4(8);
  
  lcd.setCursor(0,1);
  lcd.print("RADIO ONLINE");
  delay(2000);
  lcd.clear();
}

void loop() {
  int packetSize = LoRa.parsePacket();
  if (packetSize) {
    String incoming = "";
    while (LoRa.available()) {
      incoming += (char)LoRa.read();
    }
    
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("MSG RCVD:");
    lcd.setCursor(0,1);
    lcd.print(incoming.substring(0,16)); 
    
    Serial.print("RADIO_IN:");
    Serial.println(incoming);
  }

  if (Serial.available()) {
    String toSend = Serial.readStringUntil('\n');
    
    LoRa.beginPacket();
    LoRa.print(toSend);
    LoRa.endPacket();
    
    lcd.clear();
    lcd.print("PACKET SENT");
    delay(500);
  }
}
