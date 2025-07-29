import serial
import serial.tools.list_ports
import time
import threading

class GRBLController:
    def __init__(self, on_status_change=None, on_position_update=None):
        self.ser = None
        self.on_status_change = on_status_change
        self.on_position_update = on_position_update
        self.is_connected = False
        self.thread = None
        self.stop_thread = False

    @staticmethod
    def list_ports():
        ports = serial.tools.list_ports.comports()
        return [port.device for port in ports]

    def connect(self, port, baudrate=115200):
        try:
            self.ser = serial.Serial(port, baudrate, timeout=1)
            time.sleep(2) # Wait for GRBL to initialize
            self.ser.flushInput()
            self.is_connected = True
            if self.on_status_change:
                self.on_status_change("Connected", f"Connected to {port}")
            
            self.stop_thread = False
            self.thread = threading.Thread(target=self._read_from_port)
            self.thread.daemon = True
            self.thread.start()

            return True
        except serial.SerialException as e:
            if self.on_status_change:
                self.on_status_change("Error", f"Failed to connect: {e}")
            self.is_connected = False
            return False

    def disconnect(self):
        self.stop_thread = True
        if self.thread and self.thread.is_alive():
            self.thread.join()
        if self.ser and self.ser.isOpen():
            self.ser.close()
            self.is_connected = False
            if self.on_status_change:
                self.on_status_change("Disconnected", "Disconnected from port")

    def send_command(self, command):
        if self.is_connected:
            self.ser.write((command + '\\n').encode())
            response = self.ser.readline().decode().strip()
            return response
        return "Not connected"

    def _read_from_port(self):
        while not self.stop_thread and self.is_connected:
            try:
                line = self.ser.readline().decode('utf-8').strip()
                if line:
                    if line.startswith('<') and line.endswith('>'):
                        # Status report like <Idle|WPos:0.000,0.000,0.000|FS:0,0>
                        parts = line[1:-1].split('|')
                        status = parts[0]
                        if self.on_status_change:
                            self.on_status_change(status, line)
                        
                        for part in parts:
                            if part.startswith('WPos:'):
                                pos_str = part[5:]
                                if self.on_position_update:
                                    self.on_position_update(pos_str)
                    else:
                        # Other messages from GRBL (ok, error, etc.)
                        print(f"GRBL: {line}")

            except serial.SerialException as e:
                if self.on_status_change:
                    self.on_status_change("Error", f"Serial error: {e}")
                self.disconnect()
            except Exception as e:
                print(f"Error reading from serial: {e}")

    def __del__(self):
        self.disconnect() 