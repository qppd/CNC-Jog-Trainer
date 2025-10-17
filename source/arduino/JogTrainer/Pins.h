// Pins.h
// Centralized pin assignments for CNC Jog Trainer

#ifndef PINS_H
#define PINS_H

#include <Arduino.h>

// Pin assignments for Motor 1 (X axis)
constexpr uint8_t X_STEP_PIN = 3;
constexpr uint8_t X_DIR_PIN  = 5;
constexpr uint8_t X_EN_PIN   = 4;
constexpr uint8_t X_LIMIT_PIN = 7;

// Pin assignments for Motor 2 (Y axis)
constexpr uint8_t Y_STEP_PIN = 11;
constexpr uint8_t Y_DIR_PIN  = 10;
constexpr uint8_t Y_EN_PIN   = 9;
constexpr uint8_t Y_LIMIT_PIN = 12;

// Pin assignment for Piezo Buzzer
constexpr uint8_t BUZZER_PIN = 13;

#endif // PINS_H
