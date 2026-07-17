import tkinter as tk
from tkinter import scrolledtext, messagebox
import serial
import threading
import time

class SerialControllerUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Serial Port 3 Controller")
        self.root.geometry("450x450")
        
        # Serial connection variables
        self.ser = None
        self.is_reading = False
        
        # Port Settings
        self.port_name = 'COM3'  # Change to /dev/ttyS2 or /dev/ttyUSB2 for Linux
        self.baud_rate = 9600
        
        self.build_ui()

    def build_ui(self):
        # --- Connection Control ---
        conn_frame = tk.Frame(self.root)
        conn_frame.pack(pady=10)
        
        tk.Label(conn_frame, text=f"Target: {self.port_name} @ {self.baud_rate} baud").pack()
        
        self.btn_connect = tk.Button(conn_frame, text="Connect", command=self.connect_port, width=15)
        self.btn_connect.pack(side=tk.LEFT, padx=5)
        
        self.btn_disconnect = tk.Button(conn_frame, text="Disconnect", command=self.disconnect_port, width=15, state=tk.DISABLED)
        self.btn_disconnect.pack(side=tk.LEFT, padx=5)

        # --- Event Log Area ---
        tk.Label(self.root, text="Event Log / Incoming Data:").pack(anchor=tk.W, padx=10)
        
        self.log_area = scrolledtext.ScrolledText(self.root, width=50, height=15, state=tk.DISABLED)
        self.log_area.pack(padx=10, pady=5)

        # --- Command Sending Area ---
        cmd_frame = tk.Frame(self.root)
        cmd_frame.pack(pady=10, fill=tk.X, padx=10)
        
        tk.Label(cmd_frame, text="Command:").pack(side=tk.LEFT)
        
        self.cmd_entry = tk.Entry(cmd_frame, width=30, state=tk.DISABLED)
        self.cmd_entry.pack(side=tk.LEFT, padx=5)
        
        # Bind the Enter key to send commands as well
        self.cmd_entry.bind("<Return>", lambda event: self.send_command())
        
        self.btn_send = tk.Button(cmd_frame, text="Send", command=self.send_command, state=tk.DISABLED)
        self.btn_send.pack(side=tk.LEFT)

    def write_to_log(self, text):
        """Helper to safely write text to the scrolled text widget."""
        self.log_area.config(state=tk.NORMAL)
        self.log_area.insert(tk.END, text + "\n")
        self.log_area.see(tk.END)  # Auto-scroll to the bottom
        self.log_area.config(state=tk.DISABLED)

    def connect_port(self):
        try:
            self.ser = serial.Serial(port=self.port_name, baudrate=self.baud_rate, timeout=1)
            self.is_reading = True
            
            # Start the background thread for reading logs
            self.read_thread = threading.Thread(target=self.read_serial_logs, daemon=True)
            self.read_thread.start()
            
            # Update UI states
            self.btn_connect.config(state=tk.DISABLED)
            self.btn_disconnect.config(state=tk.NORMAL)
            self.cmd_entry.config(state=tk.NORMAL)
            self.btn_send.config(state=tk.NORMAL)
            
            self.write_to_log(f"--- Connected to {self.port_name} ---")
            
        except serial.SerialException as e:
            messagebox.showerror("Connection Error", f"Could not open {self.port_name}:\n{e}")

    def disconnect_port(self):
        self.is_reading = False # Signals the thread to stop
        time.sleep(0.1)         # Give the thread a moment to finish
        
        if self.ser and self.ser.is_open:
            self.ser.close()
            
        # Update UI states
        self.btn_connect.config(state=tk.NORMAL)
        self.btn_disconnect.config(state=tk.DISABLED)
        self.cmd_entry.config(state=tk.DISABLED)
        self.btn_send.config(state=tk.DISABLED)
        
        self.write_to_log("--- Disconnected ---")

    def send_command(self):
        if self.ser and self.ser.is_open:
            command = self.cmd_entry.get()
            if command:
                # Add carriage return and line feed, then encode to bytes
                full_command = f"{command}\r\n"
                self.ser.write(full_command.encode('utf-8'))
                self.write_to_log(f"Sent: {command}")
                self.cmd_entry.delete(0, tk.END) # Clear entry field

    def read_serial_logs(self):
        """Runs in a separate thread to constantly monitor for incoming logs."""
        while self.is_reading and self.ser and self.ser.is_open:
            try:
                if self.ser.in_waiting > 0:
                    # Read, decode, and strip incoming bytes
                    incoming_data = self.ser.readline().decode('utf-8', errors='ignore').strip()
                    if incoming_data:
                        # Use root.after to safely update the UI from this background thread
                        self.root.after(0, self.write_to_log, f"Log: {incoming_data}")
            except Exception as e:
                self.root.after(0, self.write_to_log, f"Read Error: {e}")
                break
            time.sleep(0.05) # Small sleep to prevent high CPU usage

if __name__ == "__main__":
    root = tk.Tk()
    app = SerialControllerUI(root)
    
    # Ensure a clean exit when clicking the "X" button
    root.protocol("WM_DELETE_WINDOW", lambda: (app.disconnect_port(), root.destroy()))
    root.mainloop()
