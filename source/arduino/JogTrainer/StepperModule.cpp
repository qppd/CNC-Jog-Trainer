#include "StepperModule.h"

StepperModule::StepperModule(uint8_t stepPin, uint8_t dirPin, uint8_t enPin)
    : _stepPin(stepPin), _dirPin(dirPin), _enPin(enPin) {}

void StepperModule::begin() {
    pinMode(_stepPin, OUTPUT);
    pinMode(_dirPin, OUTPUT);
    pinMode(_enPin, OUTPUT);
    disable();
}

void StepperModule::enable() {
    digitalWrite(_enPin, LOW); // LOW to enable TB6600
}

void StepperModule::disable() {
    digitalWrite(_enPin, HIGH); // HIGH to disable TB6600
}

void StepperModule::step(bool dir, int steps, int speedDelay) {
    digitalWrite(_dirPin, dir ? HIGH : LOW);
    enable();
    for (int i = 0; i < steps; i++) {
        digitalWrite(_stepPin, HIGH);
        delayMicroseconds(speedDelay);
        digitalWrite(_stepPin, LOW);
        delayMicroseconds(speedDelay);
    }
    disable();
}
