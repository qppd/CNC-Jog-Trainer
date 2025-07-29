import customtkinter as ctk

class ConnectionPanel(ctk.CTkFrame):
    def __init__(self, master, refresh_callback, connect_callback, disconnect_callback, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_columnconfigure(1, weight=1)

        self.connect_callback = connect_callback
        self.disconnect_callback = disconnect_callback
        self.refresh_callback = refresh_callback

        self.connect_btn = ctk.CTkButton(self, text="Connect", command=self.on_connect_click)
        self.connect_btn.grid(row=0, column=0, padx=5, pady=5)
        
        self.port_menu = ctk.CTkOptionMenu(self, values=["-"], dynamic_resizing=False)
        self.port_menu.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        self.refresh_btn = ctk.CTkButton(self, text="Refresh", command=self.refresh_callback, width=80)
        self.refresh_btn.grid(row=0, column=2, padx=5, pady=5)
        
    def on_connect_click(self):
        self.connect_callback(self.port_menu.get())

    def set_ports(self, ports):
        if not ports:
            ports = ["-"]
        self.port_menu.configure(values=ports)
        if ports:
            self.port_menu.set(ports[0])

    def set_connection_state(self, is_connected):
        if is_connected:
            self.connect_btn.configure(text="Disconnect", command=self.disconnect_callback)
            self.port_menu.configure(state="disabled")
            self.refresh_btn.configure(state="disabled")
        else:
            self.connect_btn.configure(text="Connect", command=self.on_connect_click)
            self.port_menu.configure(state="normal")
            self.refresh_btn.configure(state="normal")
            self.refresh_callback()