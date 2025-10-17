import customtkinter as ctk
from tkinter import filedialog, PhotoImage, messagebox
import os

from ui_components.jog_panel import JogPanel
from ui_components.file_upload import FileUploadFrame
from ui_components.status_bar import StatusBar
from ui_components.connection_panel import ConnectionPanel
from controller.grbl_serial import GRBLController
from controller.gcode_sender import GcodeSender

# Set theme and appearance
ctk.set_appearance_mode("System")  # Options: "Light", "Dark", "System"
ctk.set_default_color_theme("blue")  # You can use "green", "dark-blue", etc.


class JogTrainerApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # --- Log Area ---
        self.log_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.log_frame.grid(row=4, column=0, columnspan=4, sticky="ew", padx=10, pady=(0, 10))
        self.log_textbox = ctk.CTkTextbox(self.log_frame, height=80, width=780, state="disabled")
        self.log_textbox.pack(fill="both", expand=True)

        # GRBL Controller
        self.controller = GRBLController(
            on_status_change=self.update_status,
            on_position_update=self.update_position,
            on_log=self.append_log
        )
        self.gcode_sender = GcodeSender(self.controller, on_progress=self.update_progress)

        # Window setup
        self.title("CNC Jog Trainer")
        self.geometry("800x480")
        self.resizable(False, False)
        
        # Get the directory of the script
        self.script_dir = os.path.dirname(os.path.abspath(__file__))

        # Configure main grid
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # Header
        self.status_bar = StatusBar(self, fg_color="transparent")
        self.status_bar.grid(row=0, column=0, sticky="ew", padx=10, pady=10)

        # Main content frame
        self.main_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.main_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
        self.main_frame.grid_columnconfigure((0, 1, 2, 3), weight=1)
        self.main_frame.grid_rowconfigure((0, 1, 2), weight=1)

        # --- Button Creation ---
        button_font = ctk.CTkFont(size=18, weight="bold")
        button_size = (120, 80)

        # --- Jog Panel (Manual Jog for Arduino) ---
        jog_commands = {
            "x+": self.jog_x_plus_manual,
            "x-": self.jog_x_minus_manual,
            "y+": self.jog_y_plus_manual,
            "y-": self.jog_y_minus_manual
        }
        self.jog_panel = JogPanel(self.main_frame, jog_commands, fg_color="transparent")
        self.jog_panel.grid(row=0, column=0, rowspan=3, columnspan=2, sticky="nsew", padx=5, pady=5)
        
        # Machine Controls
        self.feed_hold_btn = ctk.CTkButton(self.main_frame, text="Feed Hold", font=button_font, width=button_size[0], height=button_size[1], fg_color="#F0F0F0", text_color="black", hover_color="#D0D0D0", command=self.feed_hold)
        self.feed_hold_btn.grid(row=0, column=2, padx=5, pady=5)
        
        self.home_btn = ctk.CTkButton(self.main_frame, text="HOME", font=button_font, width=button_size[0], height=button_size[1], fg_color="green", hover_color="darkgreen", command=self.go_home)
        self.home_btn.grid(row=0, column=3, padx=5, pady=5)

        # Note: The original image shows "Cycle Start" twice. I'm labeling the pause button as "Pause"
        self.pause_btn = ctk.CTkButton(self.main_frame, text="Pause", font=button_font, width=button_size[0], height=button_size[1], fg_color="#F0F0F0", text_color="black", hover_color="#D0D0D0", command=self.pause_job)
        self.pause_btn.grid(row=1, column=2, padx=5, pady=5)
        
        self.cycle_start_btn = ctk.CTkButton(self.main_frame, text="Cycle Start", font=button_font, width=button_size[0], height=button_size[1], command=self.start_job)
        self.cycle_start_btn.grid(row=1, column=3, padx=5, pady=5)

        self.reset_btn = ctk.CTkButton(self.main_frame, text="RESET", font=button_font, width=button_size[0], height=button_size[1], fg_color="red", hover_color="darkred", command=self.reset_job)
        self.reset_btn.grid(row=2, column=3, padx=5, pady=5)

        # Footer
        self.connection_panel = ConnectionPanel(self, self.refresh_ports, self.connect_controller, self.disconnect_controller, fg_color="transparent")
        self.connection_panel.grid(row=2, column=0, columnspan=4, sticky="ew", padx=10, pady=5)
        
        self.file_upload_frame = FileUploadFrame(self, self.upload_file, self.start_gcode_job, fg_color="transparent")
        self.file_upload_frame.grid(row=3, column=0, columnspan=4, sticky="ew", padx=10, pady=5)
        

        self.refresh_ports()
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
    def append_log(self, message):
        self.log_textbox.configure(state="normal")
        self.log_textbox.insert("end", message + "\n")
        self.log_textbox.see("end")
        self.log_textbox.configure(state="disabled")

    def on_closing(self):
        self.controller.disconnect()
        self.destroy()

    # --- Controller Methods ---
    def refresh_ports(self):
        ports = self.controller.list_ports()
        self.connection_panel.set_ports(ports)

    def connect_controller(self, port):
        if port and port != "-":
            is_connected = self.controller.connect(port)
            self.connection_panel.set_connection_state(is_connected)

    def disconnect_controller(self):
        self.controller.disconnect()
        self.connection_panel.set_connection_state(False)

    def update_status(self, status, line):
        self.status_bar.set_status(status)
        self.append_log(f"STATUS: {status}, LINE: {line}")
        # Show message box for error messages
        if status == "Error":
            messagebox.showerror("Connection Error", line)

    def update_position(self, pos_str):
        try:
            # pos_str is like "0.000,0.000,0.000"
            x, y, z = map(float, pos_str.split(','))
            self.status_bar.set_position(x, y, z)
        except ValueError as e:
            print(f"Could not parse position: {pos_str}, error: {e}")

    def update_progress(self, progress, lines_sent, total_lines):
        self.file_upload_frame.update_progress(progress)
        self.append_log(f"Progress: {progress*100:.1f}% ({lines_sent}/{total_lines})")
        if progress == 1:
            self.file_upload_frame.set_running_state(False)


    # --- Command Methods (Placeholders) ---
    def jog_x_plus(self):
        self.controller.send_command("$J=G91 X1 F500")
    def jog_y_plus(self):
        self.controller.send_command("$J=G91 Y1 F500")
    def jog_y_minus(self):
        self.controller.send_command("$J=G91 Y-1 F500")
    def jog_x_minus(self):
        self.controller.send_command("$J=G91 X-1 F500")

    # --- Manual Jog Methods for Arduino Protocol ---
    def jog_x_plus_manual(self):
        self.controller.send_command("X+")

    def jog_x_minus_manual(self):
        self.controller.send_command("X-")

    def jog_y_plus_manual(self):
        self.controller.send_command("Y+")

    def jog_y_minus_manual(self):
        self.controller.send_command("Y-")
        
    def feed_hold(self):
        self.controller.send_command("!")
        
    def go_home(self):
        self.controller.send_command("$H")

    def pause_job(self):
        self.controller.send_command("!")
        
    def start_job(self):
        self.controller.send_command("~")

    def reset_job(self):
        # Sending a soft-reset command
        self.controller.send_command("\x18")

    def upload_file(self):
        filepath = filedialog.askopenfilename(
            title="Open G-code File",
            filetypes=(("G-code files", "*.nc *.gcode"), ("All files", "*.*"))
        )
        self.file_upload_frame.set_file_name(filepath)
        if filepath:
            self.gcode_sender.load_file(filepath)
            print(f"Selected file: {filepath}")

    def start_gcode_job(self):
        if self.gcode_sender.is_running:
            if self.gcode_sender.is_paused:
                self.gcode_sender.resume()
                self.file_upload_frame.start_btn.configure(text="Pause")
            else:
                self.gcode_sender.pause()
                self.file_upload_frame.start_btn.configure(text="Resume")
        else:
            self.gcode_sender.start()
            self.file_upload_frame.set_running_state(True)
            self.file_upload_frame.start_btn.configure(text="Pause")


if __name__ == "__main__":
    app = JogTrainerApp()
    app.mainloop() 