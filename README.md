<h1 align="center">CNC Jog Trainer</h1>

<p align="center">
  Isang touchscreen-friendly na CNC controller app para sa Raspberry Pi, na unang dinevelop sa Windows.
</p>

## 🎯 Mga Layunin (Goals)

Ang proyektong ito ay naglalayong bumuo ng isang simpleng GUI para sa pag-kontrol ng isang GRBL-based CNC machine.

-   ✅ **Manual Jog Controls:** Madaling paggalaw ng X, Y, at Z axes.
-   ✅ **G-Code Sender:** Mag-upload at magpadala ng `.gcode` files sa iyong machine.
-   ✅ **Homing Function:** I-set ang machine sa kanyang home position.
-   ✅ **Serial Connection:** Kumonekta sa GRBL board (tulad ng Arduino) sa pamamagitan ng serial/USB.
-   ✅ **Status Display:** Ipakita ang kasalukuyang posisyon, status ng machine, at progress ng G-code.
-   ✨ **Optional Features:** Feedrate override at pagpili ng jog step size.

## 📁 Istraktura ng Proyekto (Project Structure)

```
JogTrainer/
│
├── venv/                      → Python virtual environment
├── main.py                   → Main application logic
├── ui_components/            → Custom widgets (e.g., jog panel, file loader)
│   ├── jog_panel.py
│   ├── file_upload.py
│   └── status_bar.py
├── controller/               → Serial & GRBL-related code
│   ├── grbl_serial.py
│   └── gcode_sender.py
├── assets/                   → Icons, sample G-code, etc.
├── requirements.txt
└── README.md
```

## 🧰 Mga Ginagamit na Tools at Libraries

-   **customtkinter:** Para sa paggawa ng modernong GUI.
-   **pyserial:** Para sa serial communication sa pagitan ng app at ng GRBL board.
-   **tkinter.filedialog:** Para sa pag-upload ng mga file.
-   **threading:** (Optional) Para hindi mag-freeze ang GUI habang nagpapadala ng G-code.

## 🚀 Development Plan (Step-by-Step)

Ito ang plano para sa pagbuo ng application:

1.  **Project Setup:** I-set up ang project folder, virtual environment, at i-install ang mga kailangan na libraries.
2.  **Basic GUI:** Buuin ang pangunahing bintana ng app gamit ang customtkinter.
3.  **Manual Jog Control:** Gumawa ng mga button para sa pag-jog ng X, Y, Z axes at step size selector.
4.  **Homing and Reset:** Magdagdag ng controls para sa homing (`$H`) at reset/unlock (`Ctrl-X`).
5.  **G-Code File Handling:** Mag-implement ng file picker para sa `.gcode` files at mga button para i-kontrol ang pagpapadala nito.
6.  **Serial Connection Manager:** Gumawa ng UI para makapili ng COM port at mag-connect/disconnect.
7.  **Status Display:** Ipakita ang mahahalagang impormasyon tulad ng coordinates at machine state.
8.  **Raspberry Pi Optimization:** I-adjust ang layout para maging friendly sa 7-inch touchscreen.

## 🎨 UI Layout Mockup

Ang app ay magkakaroon ng iba't ibang "pages" para sa bawat function:

| Page     | Mga Nilalaman (Widgets)                                            |
| :------- | :----------------------------------------------------------------- |
| **Jog**  | Jog buttons (X, Y, Z), step size selector, home button, reset button |
| **Upload** | File upload button, file path display, start/pause/stop buttons, progress bar |
| **Status** | Serial port selector, GRBL status indicator, coordinates, connect button |

## 🛠️ Paano Simulan (Setup and Installation)

Sundan ang mga hakbang na ito para patakbuhin ang proyekto sa iyong local machine.

### 1. I-clone ang Repository

```bash
git clone <repository-url>
cd JogTrainer
```

### 2. Gumawa ng Virtual Environment

```bash
# Para sa Windows
python -m venv venv
.\venv\Scripts\Activate
```

### 3. I-install ang mga Dependencies

```bash
pip install -r requirements.txt
```

### 4. Patakbuhin ang App

```bash
python main.py
``` 