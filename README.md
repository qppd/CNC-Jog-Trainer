
<h1 align="center">CNC Jog Trainer</h1>

<p align="center">
  <b>Touchscreen-friendly CNC controller app for Raspberry Pi and Windows, with a modern Python GUI.</b><br>
  <span style="color:gray">A touchscreen-friendly CNC controller app for Raspberry Pi, originally developed on Windows.</span>
</p>

---

## 📝 Overview

CNC Jog Trainer is a modern, touchscreen-optimized graphical user interface (GUI) for controlling GRBL-based CNC machines. It is designed for use on a Raspberry Pi with a 7-inch touchscreen, but also runs on Windows. The app provides manual jog controls (X and Y axes), G-code file upload and sending, real-time status display, and robust serial connection management.

---

## 🚩 Features

 - **Manual Jog Controls:** Move X and Y axes with large, touch-friendly buttons (Z-axis jog is not available in this version).
- **G-code Sender:** Upload and send `.gcode` or `.nc` files to your CNC machine with progress tracking.
- **Homing & Reset:** Home the machine (`$H`) and perform soft reset (`Ctrl-X`).
- **Serial Connection Manager:** List, select, and connect/disconnect from available serial ports (e.g., Arduino/GRBL).
- **Status & Position Display:** Real-time display of machine status and X/Y/Z coordinates.
- **Pause/Resume/Feed Hold:** Pause, resume, and hold jobs with dedicated controls.
- **Touchscreen-Optimized UI:** Large buttons, grid layout, and fixed 800x480 window for Raspberry Pi touchscreen.
- **Threaded Communication:** Serial operations run in background threads to keep the UI responsive.

---

## 🖥️ UI/UX Design

- **Grid-based layout** with header (status bar), main content (jog panel, controls), and footer (connection & file upload panels).
- **Large, color-coded buttons** for all major actions.
- **Progress bar** for G-code sending.
- **Status bar** with live machine state and position.
- **See [`ui_ux_design.md`](ui_ux_design.md) for full design documentation.**

---

## 📁 Project Structure

```
JogTrainer/
│
├── main.py                   # Main application logic and UI
├── requirements.txt          # Python dependencies
├── ui_ux_design.md           # UI/UX design documentation
├── assets/                   # Icons, images (e.g., Raspberry Pi logo)
├── controller/               # Serial & GRBL-related code
│   ├── grbl_serial.py        # GRBL serial communication logic
│   └── gcode_sender.py       # G-code file sending logic
├── ui_components/            # Custom widgets
│   ├── jog_panel.py          # Jog controls (X/Y)
│   ├── file_upload.py        # File upload & progress
│   ├── status_bar.py         # Status and position display
│   └── connection_panel.py   # Serial port selection & connection
└── README.md
```

---

## 🧰 Requirements

- **Python 3.11+**
- [customtkinter](https://github.com/TomSchimansky/CustomTkinter) (>=5.2.2)
- [pyserial](https://pypi.org/project/pyserial/) (>=3.5)
- darkdetect, packaging
- All dependencies are listed in `requirements.txt`.

---


## ⚡ Installation & Usage

### 1. Clone the Repository

```bash
git clone <repository-url>
cd JogTrainer
```

### 2. Create a Virtual Environment

```bash
# For Windows
python -m venv venv
.\venv\Scripts\Activate
# For Linux/Raspberry Pi
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the App

```bash
python main.py
```

## 🤝 Contributing

Contributions are welcome! Please open issues or pull requests for bug fixes, improvements, or new features.

---

## 📄 License

This project is open source. See the `LICENSE` file for details.


This project is maintained by **Quezon Province Programmers & Developers** — a community of makers, engineers, and developers from Quezon Province, Philippines. We build open-source tools and solutions for automation, education, and industry.

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
