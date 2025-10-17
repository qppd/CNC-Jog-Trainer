# Arduino CNC Jog Trainer

<p align="center">
  <b>Stepper</b> • <b>Limit Switch</b> • <b>Piezo Buzzer</b> • <b>DS3231 RTC</b> • <b>G-code Interpreter</b>
</p>

---

## ✨ Features

- Control 2-axis NEMA 17 stepper motors via TB6600 drivers
- Limit switch support for both X and Y axes
- Piezo buzzer for audio feedback
- DS3231 Real-Time Clock (RTC) integration
- Serial command interface for manual jogging and status
- G-code interpreter (G0/G1) for CNC movement
- Ready for G-code streaming from Raspberry Pi or PC
- Modular C++ codebase: each hardware feature is encapsulated in its own class (StepperModule, LimitSwitch, PiezoBuzzer, ClockModule, GCodeHandler)
- Customizable pin assignments in `JogTrainer.ino`

## 🛠️ Hardware Requirements

- Arduino Uno/Nano/compatible
- 2x NEMA 17 stepper motors
- 2x TB6600 stepper drivers
- 2x Limit switches
- Piezo buzzer
- DS3231 RTC module
- Raspberry Pi (for G-code streaming, optional)


## 🚀 Usage

### Serial Interface

- **Baud Rate:** 115200

#### Manual Commands

| Command     | Description                        |
|-------------|------------------------------------|
| `X+`        | Jog X axis forward                 |
| `X-`        | Jog X axis backward                |
| `Y+`        | Jog Y axis forward                 |
| `Y-`        | Jog Y axis backward                |
| `LIM?`      | Query limit switch status          |
| `BUZ`       | Test buzzer                        |
| `CLOCK`     | Print current RTC time             |
| `FEEDHOLD`  | Pause all motion (feed hold)       |
| `PAUSE`     | Pause all motion                   |
| `CYCLE`     | Resume from feed hold/pause        |
| `START`     | Resume from feed hold/pause        |
| `RESUME`    | Resume from feed hold/pause        |
| `RESET`     | Stop all motion, reset state       |
| `HOME`      | Home both axes to limit switches   |

#### G-code Support

- Supports standard G-code streaming (G0/G1 X Y F) for CNC movement.
- Example: `G1 X10 Y20 F600` (move to X=10mm, Y=20mm at 600mm/min)

### Project Structure

```text
JogTrainer.ino         // Main sketch and pin assignments
StepperModule.h/.cpp   // Stepper motor control
LimitSwitch.h/.cpp     // Limit switch handling
PiezoBuzzer.h/.cpp     // Buzzer control
ClockModule.h/.cpp     // DS3231 RTC integration
GCodeHandler.h/.cpp    // G-code command parsing and execution
```

### Libraries Used

- **RTClib** by Adafruit (v2.1.4) — for DS3231 RTC

---

## 👨‍💻 About Us

This project is maintained by **Quezon Province Programmers & Developers** — a community of makers, engineers, and developers from Quezon Province, Philippines. We build open-source tools and solutions for automation, education, and industry.

---

**Note:** Pin assignments for motors, switches, and buzzer can be customized in `JogTrainer.ino` to match your hardware setup.

## 📞 Contact

- 📧 Email: [quezon.province.pd@gmail.com](mailto:quezon.province.pd@gmail.com)
- 🐙 GitHub: [github.com/qppd](https://github.com/qppd)
- 🌐 Portfolio: [sajed-mendoza.onrender.com](https://sajed-mendoza.onrender.com)
- 📘 Facebook: [facebook.com/qppd.dev](https://facebook.com/qppd.dev)
- 📄 Facebook Page: [facebook.com/QUEZONPROVINCEDEVS](https://facebook.com/QUEZONPROVINCEDEVS)

---

<div align="center">
  &copy; 2025 Quezon Province Programmers & Developers. All rights reserved.
</div>
