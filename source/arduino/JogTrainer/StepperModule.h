#ifndef STEPPERMODULE_H
#define STEPPERMODULE_H

#include <Arduino.h>

class StepperModule {
public:
    StepperModule(uint8_t stepPin, uint8_t dirPin, uint8_t enPin);
    void begin();
    void step(bool dir, int steps, int speedDelay = 500);
    void enable();
    void disable();
private:
    uint8_t _stepPin, _dirPin, _enPin;
};

#endif // STEPPERMODULE_H
