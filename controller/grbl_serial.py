import serial
import serial.tools.list_ports
import time
import threading
import logging

class GRBLController:
    def __init__(self, on_status_change=None, on_position_update=None, on_log=None):
        self.ser = None
        self.on_status_change = on_status_change
        self.on_position_update = on_position_update
        self.on_log = on_log
        self.is_connected = False
        self.thread = None
        self.stop_thread = False
        self.logger = logging.getLogger(__name__)
        if not self.logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)
            self.logger.setLevel(logging.INFO)

    @staticmethod
    def list_ports():
        ports = serial.tools.list_ports.comports()
        return [port.device for port in ports]

    def connect(self, port, baudrate=115200):
        try:
            self.ser = serial.Serial(port, baudrate, timeout=1)
            time.sleep(2)
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
        if not self.is_connected:
            self.logger.warning("Attempted to send command while not connected")
            if self.on_log:
                self.on_log("[Not connected] Cannot send: " + command)
            return "Not connected"
        try:
            self.ser.write((command + '\n').encode())
            self.logger.debug(f"Sent command: {command}")
            if self.on_log:
                self.on_log(f"Sent: {command}")
            return "Sent"
        except serial.SerialException as e:
            self.logger.error(f"Serial error while sending command '{command}': {e}")
            if self.on_log:
                self.on_log(f"Serial error while sending '{command}': {e}")
            if self.on_status_change:
                self.on_status_change("Error", f"Serial error: {e}")
            self.disconnect()
            return f"Serial error: {e}"
        except Exception as e:
            self.logger.error(f"Unexpected error while sending command '{command}': {e}")
            if self.on_log:
                self.on_log(f"Unexpected error while sending '{command}': {e}")
            if self.on_status_change:
                self.on_status_change("Error", f"Communication error: {e}")
            return f"Communication error: {e}"

    def _read_from_port(self):
        while not self.stop_thread and self.is_connected:
            try:
                line = self.ser.readline().decode('utf-8').strip()
                if line:
                    if self.on_log:
                        self.on_log(f"GRBL: {line}")
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
            except serial.SerialException as e:
                self.logger.error(f"Serial error in reader thread: {e}")
                if self.on_log:
                    self.on_log(f"Serial error in reader thread: {e}")
                if self.on_status_change:
                    self.on_status_change("Error", f"Serial error: {e}")
                self.disconnect()
            except UnicodeDecodeError as e:
                self.logger.warning(f"Unicode decode error in reader thread: {e}")
                if self.on_log:
                    self.on_log(f"Unicode decode error in reader thread: {e}")
                # Continue reading, this might be a temporary issue
            except Exception as e:
                self.logger.error(f"Unexpected error in reader thread: {e}")
                if self.on_log:
                    self.on_log(f"Unexpected error in reader thread: {e}")
                # For unexpected errors, we'll log and continue
                # This prevents the thread from dying on unexpected issues

    def __del__(self):
        self.disconnect() 