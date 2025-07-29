import customtkinter as ctk
from tkinter import filedialog
import os

class FileUploadFrame(ctk.CTkFrame):
    def __init__(self, master, upload_command, start_command, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_columnconfigure(1, weight=1)
        
        self.upload_command = upload_command
        self.start_command = start_command

        self.upload_btn = ctk.CTkButton(self, text="Upload G-code", command=self.upload_command)
        self.upload_btn.grid(row=0, column=0, padx=5, pady=5)

        self.file_label = ctk.CTkLabel(self, text="No file selected.", anchor="w")
        self.file_label.grid(row=0, column=1, padx=10, sticky="ew")

        self.start_btn = ctk.CTkButton(self, text="Start Job", command=self.start_command, state="disabled")
        self.start_btn.grid(row=0, column=2, padx=5, pady=5)
        
        self.progress_bar = ctk.CTkProgressBar(self)
        self.progress_bar.grid(row=1, column=0, columnspan=3, sticky="ew", padx=5, pady=5)
        self.progress_bar.set(0)

    def set_file_name(self, filepath):
        if filepath:
            filename = os.path.basename(filepath)
            self.file_label.configure(text=filename)
            self.start_btn.configure(state="normal")
        else:
            self.file_label.configure(text="No file selected.")
            self.start_btn.configure(state="disabled")

    def update_progress(self, progress_value):
        self.progress_bar.set(progress_value)

    def set_running_state(self, is_running):
        if is_running:
            self.upload_btn.configure(state="disabled")
            self.start_btn.configure(text="Pause") # Or Stop/Cancel
        else:
            self.upload_btn.configure(state="normal")
            self.start_btn.configure(text="Start Job") 