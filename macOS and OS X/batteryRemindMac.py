import psutil
import pync
import os
import tkinter as tk
from tkinter import messagebox

battery = psutil.sensors_battery()

root = tk.Tk()
root.withdraw()

def nohup():
    dirpath = os.path.realpath(__file__)
    os.system(f"nohup python3 {dirpath}")

while battery.power_plugged == False:
    for i in range(4):
                if battery.percent == 60:
                    if battery.percent == 50:
                        if battery.percent == 40:
                            if battery.percent == 30:
                                pync.notify("Your battery is at 30%, please charge immediately.", appIcon="batteryhalf.png")
                            else:
                                pync.notify("Your battery is at 40%, please charge.", appIcon="batteryhalf.png")
                        else:
                            pync.notify("Your battery is at 50%, please charge.", appIcon="batteryhalf.png")
                    else:
                        pync.notify("Your battery is at 60%, please charge.", appIcon="batteryhalf.png")

while battery.power_plugged == True:
    for i in range(1):
        if battery.percent < 100:
            pass
        else:
            pync.notify("Your battery fully charged! Feel free to unplug anytime!", appIcon="batteryfull.png")

if not hasattr(psutil, "sensors_battery"):
    messagebox.showwarning('Sorry, but this platform is currently not supported.','Unsupported')

if battery is None:
    messagebox.showerror('This program has detected that there is no battery installed on this computer. Click OK to close this window.','No Battery')