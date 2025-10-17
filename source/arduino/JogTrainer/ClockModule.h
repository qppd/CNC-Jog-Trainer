#ifndef CLOCKMODULE_H
#define CLOCKMODULE_H

#include <Arduino.h>
#include <RTClib.h> // Adafruit RTClib library for DS3231

class ClockModule {
public:
    ClockModule();
    void begin();
    DateTime now();
    void printNow(Stream& s = Serial);
private:
    RTC_DS3231 rtc;
};

#endif // CLOCKMODULE_H
