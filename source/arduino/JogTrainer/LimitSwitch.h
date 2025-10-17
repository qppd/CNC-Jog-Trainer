#ifndef LIMITSWITCH_H
#define LIMITSWITCH_H

#include <Arduino.h>

class LimitSwitch {
public:
    LimitSwitch(uint8_t pin);
    void begin();
    bool isPressed();
private:
    uint8_t _pin;
};

#endif // LIMITSWITCH_H
