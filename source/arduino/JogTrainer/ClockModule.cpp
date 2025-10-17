#include "ClockModule.h"

ClockModule::ClockModule() {}

void ClockModule::begin() {
    if (!rtc.begin()) {
        Serial.println("Couldn't find RTC");
        while (1);
    }
    if (rtc.lostPower()) {
        Serial.println("RTC lost power, setting time to compile time");
        rtc.adjust(DateTime(F(__DATE__), F(__TIME__)));
    }
}

DateTime ClockModule::now() {
    return rtc.now();
}

void ClockModule::printNow(Stream& s) {
    DateTime t = now();
    s.print(t.year(), DEC);
    s.print('/');
    s.print(t.month(), DEC);
    s.print('/');
    s.print(t.day(), DEC);
    s.print(' ');
    s.print(t.hour(), DEC);
    s.print(':');
    s.print(t.minute(), DEC);
    s.print(':');
    s.print(t.second(), DEC);
}
