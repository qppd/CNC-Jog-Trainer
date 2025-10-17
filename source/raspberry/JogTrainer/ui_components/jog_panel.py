import customtkinter as ctk

class JogPanel(ctk.CTkFrame):
    def __init__(self, master, jog_commands, **kwargs):
        super().__init__(master, **kwargs)

        button_font = ctk.CTkFont(size=18, weight="bold")
        button_size = (120, 80)

        # Jog Controls (X and Y only)
        self.x_plus_btn = ctk.CTkButton(self, text="X+", font=button_font, width=button_size[0], height=button_size[1], command=jog_commands["x+"])
        self.x_plus_btn.grid(row=0, column=0, padx=5, pady=5)

        self.y_plus_btn = ctk.CTkButton(self, text="Y+", font=button_font, width=button_size[0], height=button_size[1], command=jog_commands["y+"])
        self.y_plus_btn.grid(row=0, column=1, padx=5, pady=5)

        self.x_minus_btn = ctk.CTkButton(self, text="X-", font=button_font, width=button_size[0], height=button_size[1], command=jog_commands["x-"])
        self.x_minus_btn.grid(row=1, column=0, padx=5, pady=5)

        self.y_minus_btn = ctk.CTkButton(self, text="Y-", font=button_font, width=button_size[0], height=button_size[1], command=jog_commands["y-"])
        self.y_minus_btn.grid(row=1, column=1, padx=5, pady=5)