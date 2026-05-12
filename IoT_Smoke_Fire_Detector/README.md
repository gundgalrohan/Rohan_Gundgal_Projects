IoT Smoke & Fire Detector
An Arduino-based real-time smoke and fire detection system that displays alerts on an LCD and triggers a buzzer based on sensor readings.

Hardware Required
Arduino Uno
MQ-2 Smoke Sensor (Analog pin A0)
IR Flame Sensor (Digital pin 8)
Buzzer (Digital pin 9)
16x2 I2C LCD Display (Address: 0x27)

Features
Real-time smoke level classification: LOW / MEDIUM / HIGH
Fire detection with immediate buzzer alert
LCD display with live status updates
Serial monitor output for debugging

Tech Stack
Arduino (C++) LiquidCrystal_I2C Analog & Digital I/O

Setup
Wire components as per pin definitions in the sketch
Install LiquidCrystal_I2C library via Arduino Library Manager
Upload smoke_fire_detector.ino to your Arduino board
