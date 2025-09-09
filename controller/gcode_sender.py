import threading
import time
import logging

class GcodeSender:
    def __init__(self, controller, on_progress=None, on_error=None):
        self.controller = controller
        self.on_progress = on_progress
        self.filepath = None
        self.gcode_lines = []
        self.is_running = False
        self.is_paused = False
        self.thread = None

    def load_file(self, filepath):
        self.filepath = filepath
        with open(filepath, 'r') as f:
            self.gcode_lines = [line.strip() for line in f if line.strip() and not line.strip().startswith(';')]
        print(f"Loaded {len(self.gcode_lines)} lines of G-code from {filepath}")

    def start(self):
        if not self.gcode_lines or not self.controller.is_connected:
            print("Cannot start: No file loaded or not connected.")
            return

        self.is_running = True
        self.is_paused = False
        self.thread = threading.Thread(target=self._send_gcode)
        self.thread.daemon = True
        self.thread.start()

    def stop(self):
        self.is_running = False
        if self.thread and self.thread.is_alive():
            self.thread.join()

    def pause(self):
        self.is_paused = True

    def resume(self):
        self.is_paused = False

    def _send_gcode(self):
        total_lines = len(self.gcode_lines)
        for i, line in enumerate(self.gcode_lines):
            while self.is_paused and self.is_running:
                time.sleep(0.1)

            if not self.is_running:
                print("G-code sending stopped.")
                break
            
            # Simple flow control: wait for 'ok'
            response = self.controller.send_command(line)
            print(f"Sent: {line} -> Got: {response}")
            if 'ok' not in response:
                print(f"Error sending line {i+1}: {line}. Halting.")
                self.is_running = False
                break

            if self.on_progress:
                progress = (i + 1) / total_lines
                self.on_progress(progress, i + 1, total_lines)
        
        self.is_running = False
        print("G-code sending finished.") 