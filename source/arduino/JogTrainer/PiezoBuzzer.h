#ifndef PIEZOBUZZER_H
#define PIEZOBUZZER_H

#include <Arduino.h>

class PiezoBuzzer {
public:
    PiezoBuzzer(uint8_t pin);
    void begin();
    void beep(unsigned int durationMs = 100);
private:
    uint8_t _pin;
};

#endif // PIEZOBUZZER_H
