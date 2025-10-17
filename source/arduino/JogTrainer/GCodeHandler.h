#ifndef GCODEHANDLER_H
#define GCODEHANDLER_H

#include <Arduino.h>

// Forward declarations for modules
class StepperModule;
class LimitSwitch;
class PiezoBuzzer;
class ClockModule;


class GCodeHandler {
public:
    GCodeHandler(StepperModule& sx, StepperModule& sy, LimitSwitch& lx, LimitSwitch& ly, PiezoBuzzer& buz, ClockModule& clk,
                 float stepsPerMM_X, float stepsPerMM_Y, float defaultFeedrate);
    void handleLine(const String& line);
    long getXSteps() const;
    long getYSteps() const;
private:
    StepperModule& stepperX;
    StepperModule& stepperY;
    LimitSwitch& limitX;
    LimitSwitch& limitY;
    PiezoBuzzer& buzzer;
    ClockModule& clock;
    float stepsPerMM_X;
    float stepsPerMM_Y;
    float defaultFeedrate;
    long posX_steps;
    long posY_steps;

    // State for feed hold, pause, home, cycle start, reset
    bool isFeedHold;
    bool isPaused;
    bool isHoming;
    bool isResetting;

    void jogCommand(const String& cmd);
    float parseGcodeValue(const String& line, char code, float fallback);
    void moveTo(long targetX, long targetY, float feedrate_mm_min);
    void handleGcode(const String& line);

    void handleFeedHold();
    void handlePause();
    void handleCycleStart();
    void handleReset();
    void handleHome();
    void doHome();
};

#endif // GCODEHANDLER_H
