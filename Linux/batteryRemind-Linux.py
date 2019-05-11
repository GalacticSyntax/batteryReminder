import psutil
import notify2
import os
import time
import sys
import tkinter as tk
from tkinter import messagebox

battery = psutil.sensors_battery()
discharging = True
battpercent = battery.percent

root = tk.Tk()
root.withdraw()

notify2.init('batteryReminder')

def nohup():
    dirpath = os.path.realpath(__file__)
    os.system(f"nohup python3 {dirpath}")

if not hasattr(psutil, "sensors_battery"):
    messagebox.showwarning('Sorry, but this platform is currently not supported.','Unsupported')
    sys.exit()

if battery is None:
    messagebox.showerror('This program has detected that there is no battery installed on this computer. Click OK to close this window.','No Battery')
    sys.exit()

if battpercent == 60 and discharging == True:
    sxp = notify2.Notification('Battery Reminder',"Your battery is at 60%, please charge!")
    sxp.show()
    time.sleep(60)

elif battpercent == 50 and discharging == True:
    fip = notify2.Notification('Battery Reminder',"Your battery is at 50%, please charge!")
    fip.show()
    time.sleep(60)

elif battpercent == 40 and discharging == True:
    fop = notify2.Notification('Battery Reminder',"Your battery is at 40%, please charge!")
    fop.show()
    time.sleep(60)

elif battpercent == 30 and discharging == True:
    thp = notify2.Notification('Battery Reminder',"Your battery is at 30%, please charge!")
    thp.show()
    time.sleep(60)
    
elif battery.power_plugged == True:
    if battpercent < 100:
        pass
    else:
        fc = notify2.Notification('Battery Reminder',"Your battery is fully charged! Please unplug the charger!")
        fc.show()
        time.sleep(60)
    discharging = False
    
elif battery.power_plugged == False:
    discharging = True