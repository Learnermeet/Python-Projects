import tkinter as tk
from tkinter import messagebox
import time
import threading
import pygame

pygame.mixer.init()

AUDIO_PATH = r"D:\Projects\Python-Projects\Alarm_Clock\audio.mp3"

class AlarmApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Alarm Clock")
        self.root.geometry("300x220")
        self.root.resizable(False, False)

        self.running = False

        tk.Label(root, text="Alarm Clock", font=("Arial", 16, "bold")).pack(pady=10)

        frame = tk.Frame(root)
        frame.pack(pady=10)

        tk.Label(frame, text="Minutes").grid(row=0, column=0, padx=5)
        tk.Label(frame, text="Seconds").grid(row=0, column=1, padx=5)

        self.minutes_entry = tk.Entry(frame, width=8)
        self.seconds_entry = tk.Entry(frame, width=8)
        self.minutes_entry.grid(row=1, column=0, padx=5)
        self.seconds_entry.grid(row=1, column=1, padx=5)

        self.status = tk.Label(root, text="Set time and start", fg="blue")
        self.status.pack(pady=5)

        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Start", width=10, command=self.start_alarm).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Stop", width=10, command=self.stop_alarm).grid(row=0, column=1, padx=5)

    def start_alarm(self):
        if self.running:
            return

        try:
            minutes = int(self.minutes_entry.get() or 0)
            seconds = int(self.seconds_entry.get() or 0)

            if minutes < 0 or seconds < 0:
                raise ValueError

        except ValueError:
            messagebox.showerror("Invalid Input", "Enter valid non-negative numbers")
            return

        total_seconds = minutes * 60 + seconds

        if total_seconds == 0:
            messagebox.showwarning("No Time Set", "Please set a time greater than 0")
            return

        self.running = True
        threading.Thread(target=self.run_timer, args=(total_seconds,), daemon=True).start()

    def run_timer(self, total_seconds):
        remaining = total_seconds

        while remaining > 0 and self.running:
            mins = remaining // 60
            secs = remaining % 60
            self.status.config(text=f"Ringing in {mins:02d}:{secs:02d}")
            time.sleep(1)
            remaining -= 1

        if self.running:
            self.play_sound()

    def play_sound(self):
        self.status.config(text="ALARM RINGING!", fg="red")
        pygame.mixer.music.load(AUDIO_PATH)
        pygame.mixer.music.set_volume(1.0)
        pygame.mixer.music.play(-1)  # Loop

    def stop_alarm(self):
        self.running = False
        pygame.mixer.music.stop()
        self.status.config(text="Alarm stopped", fg="green")


if __name__ == "__main__":
    root = tk.Tk()
    app = AlarmApp(root)
    root.mainloop()