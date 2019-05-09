import psutil
import pync
import os
from threading import Event
import calendar
import tkinter as tk
from tkinter import messagebox

battery = psutil.sensors_battery()
discharging = True
battpercent = battery.percent

root = tk.Tk()
root.withdraw()

def nohup():
    dirpath = os.path.realpath(__file__)
    os.system(f"nohup python3 {dirpath}")

if battpercent == 60 and discharging == True:
    pync.notify('Your battery is at 60%, please charge!',title="Battery Reminder")
    Event().wait(timeout=60)

elif battpercent == 50 and discharging == True:
    pync.notify('Your battery is at 50%, please charge!',title="Battery Reminder")
    Event().wait(timeout=60)

elif battpercent == 40 and discharging == True:
    pync.notify('Your battery is at 40%, please charge!',title="Battery Reminder")
    Event().wait(timeout=60)

elif battpercent == 30 and discharging == True:
    pync.notify('Your battery is at 30%, please charge!',title="Battery Reminder")
    Event().wait(timeout=60)

if not hasattr(psutil, "sensors_battery"):
    messagebox.showwarning('Sorry, but this platform is currently not supported.','Unsupported')

if battery is None:
    messagebox.showerror('This program has detected that there is no battery installed on this computer. Click OK to close this window.','No Battery')