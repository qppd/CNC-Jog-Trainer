#include "LimitSwitch.h"

LimitSwitch::LimitSwitch(uint8_t pin) : _pin(pin) {}

void LimitSwitch::begin() {
    pinMode(_pin, INPUT_PULLUP); // Use internal pull-up resistor
}

bool LimitSwitch::isPressed() {
    return digitalRead(_pin) == LOW; // LOW means pressed (active low)
}
