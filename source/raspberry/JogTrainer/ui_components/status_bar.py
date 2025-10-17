import customtkinter as ctk
from tkinter import PhotoImage
import os

class StatusBar(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_columnconfigure(2, weight=1) # Give weight to the position frame

        self.status_label = ctk.CTkLabel(self, text="Not Connected", font=ctk.CTkFont(size=16, weight="bold"))
        self.status_label.grid(row=0, column=0, sticky="w", padx=10)
        
        # Position Frame
        self.position_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.position_frame.grid(row=0, column=1, sticky="w")
        self.x_pos_label = ctk.CTkLabel(self.position_frame, text="X: 0.000", font=ctk.CTkFont(size=14))
        self.x_pos_label.pack(side="left", padx=10)
        self.y_pos_label = ctk.CTkLabel(self.position_frame, text="Y: 0.000", font=ctk.CTkFont(size=14))
        self.y_pos_label.pack(side="left", padx=10)
        self.z_pos_label = ctk.CTkLabel(self.position_frame, text="Z: 0.000", font=ctk.CTkFont(size=14))
        self.z_pos_label.pack(side="left", padx=10)

        self.title_label = ctk.CTkLabel(self, text="CNC CONTROL PANEL", font=ctk.CTkFont(size=20, weight="bold"))
        self.title_label.grid(row=0, column=2, sticky="w", padx=20)
        
        # Get the directory of the script
        script_dir = os.path.dirname(os.path.abspath(__file__))
        logo_path = os.path.join(script_dir, "..", "assets", "raspberry_pi_logo.png")

        try:
            self.logo_image = PhotoImage(file=logo_path)
            self.logo_label = ctk.CTkLabel(self, image=self.logo_image, text="")
            self.logo_label.grid(row=0, column=3, sticky="e")
        except Exception as e:
            print(f"Could not load logo: {e}")
            # Fallback to text if image fails
            self.logo_label = ctk.CTkLabel(self, text="RPI", font=ctk.CTkFont(size=20, weight="bold"))
            self.logo_label.grid(row=0, column=3, sticky="e")

    def set_status(self, status_text):
        self.status_label.configure(text=status_text)

    def set_position(self, x, y, z):
        self.x_pos_label.configure(text=f"X: {x:.3f}")
        self.y_pos_label.configure(text=f"Y: {y:.3f}")
        self.z_pos_label.configure(text=f"Z: {z:.3f}") 