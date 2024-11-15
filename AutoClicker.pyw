""" This version launches without a console (no logging included)"""

import time
import threading
import keyboard
import pyautogui  # For mouse clicking
import tkinter as tk
from tkinter import ttk, messagebox


__version__ = "1.1.0"
__build__ = "2024.11.14.1" # format: yyyy.mm.dd.patch-number
__author__ = "Team12Runners LLC & Blinky"


class AutoPresserGUI(tk.Tk):

    def __init__(self, presser):
        super().__init__()
        self.presser = presser
        self.title("AutoClicker v1.0")
        self.geometry("300x380")  # set window size to show title
        self.focus_force()  # Force-focus window

        # Version Label
        self.version_label = ttk.Label(self, text=f"AutoClicker Version: {__version__}\nBuild: {__build__}")
        self.version_label.pack(pady=10)

        # Author Label
        self.author_label = ttk.Label(self, text=f"Developed by: {__author__}")
        self.author_label.pack(pady=5)

        # Click Frequency Input
        self.click_frequency_label = ttk.Label(self, text="Click Frequency (0 For Default Frequency):")
        self.click_frequency_label.pack(pady=5)

        self.click_frequency_entry = ttk.Entry(self)
        self.click_frequency_entry.pack(pady=5)
        self.click_frequency_entry.insert(0, "0")

        # Update Frequency Button
        self.update_button = ttk.Button(self, text="Update Frequency", command=self.update_frequency)
        self.update_button.pack(pady=5)

        # Toggle Button
        self.toggle_button = ttk.Button(self, text="Toggle", command=self.toggle_pressing)
        self.toggle_button.pack(pady=20)

        # State Toggle Button (Mouse/Keyboard)
        self.state_button = ttk.Button(self, text="Mouse", command=self.toggle_state)
        self.state_button.pack(pady=20)

        # Exit Button
        self.exit_button = ttk.Button(self, text="Exit", command=self.quit)
        self.exit_button.pack(pady=20)

        # Add hotkey to toggle
        keyboard.add_hotkey('right shift', self.toggle_pressing)

    def update_frequency(self):
        try:
            frequency = int(self.click_frequency_entry.get())
            if frequency < 0:
                raise ValueError("The frequency must be a positive integer or zero.")
            self.presser.click_frequency = frequency if frequency > 0 else 1
        except ValueError as e:
            tk.messagebox.showerror("Invalid input", str(e))

    def toggle_pressing(self):
        if self.presser.is_pressing:
            self.presser.stop_pressing()
            self.toggle_button.config(text="Start")
        else:
            self.presser.start_pressing()
            self.toggle_button.config(text="Stop")

    def toggle_state(self):
        self.presser.toggle_state()
        if self.presser.state == 'keyboard':
            self.state_button.config(text="Mouse")
        else:
            self.state_button.config(text="Keyboard")


class AutoPresser:

    def __init__(self):
        self.is_pressing = False
        self.key = 'e'
        self.state = 'mouse'  # default state
        self.click_frequency = 1

    def start_pressing(self):
        if not self.is_pressing:
            self.is_pressing = True
            threading.Thread(target=self.auto_press).start()

    def stop_pressing(self):
        self.is_pressing = False

    def auto_press(self):
        while self.is_pressing:
            if self.state == 'keyboard':
                keyboard.press(self.key)
                keyboard.release(self.key)
            elif self.state == 'mouse':
                pyautogui.click(clicks=self.click_frequency,
                                interval=0.001 / self.click_frequency)  # Adjust interval for speed
            time.sleep(0.00000001)  # Minimal sleep to prevent thread locking

    def toggle_state(self):
        if self.state == 'keyboard':
            self.state = 'mouse'
        else:
            self.state = 'keyboard'


if __name__ == "__main__":
    presser = AutoPresser()
    app = AutoPresserGUI(presser)
    app.mainloop()