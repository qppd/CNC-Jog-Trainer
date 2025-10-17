#include "PiezoBuzzer.h"

PiezoBuzzer::PiezoBuzzer(uint8_t pin) : _pin(pin) {}

void PiezoBuzzer::begin() {
    pinMode(_pin, OUTPUT);
    digitalWrite(_pin, LOW);
}

void PiezoBuzzer::beep(unsigned int durationMs) {
    digitalWrite(_pin, HIGH);
    delay(durationMs);
    digitalWrite(_pin, LOW);
}
