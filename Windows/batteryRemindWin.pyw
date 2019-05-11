import psutil
import ctypes
import time
import sys
from win10toast import ToastNotifier

toaster = ToastNotifier()

ICON_EXLAIM=0x30
ICON_STOP = 0x10

battery = psutil.sensors_battery()
discharging = True

if not hasattr(psutil, "sensors_battery"):
    ctypes.windll.user32.MessageBoxW(0, "Sorry, but this platform is currently not supported.", "Unsupported", ICON_STOP)
    sys.exit()

if battery is None:
    ctypes.windll.user32.MessageBoxW(0, "This program has detected that there is no battery installed on this computer. Click OK to close this window.", "No Battery", ICON_EXLAIM)
    sys.exit()

if battery.percent == 60 and discharging == True:
    toaster.show_toast('Battery Reminder',"Your battery is at 60%, please charge!")
    time.sleep(60)

elif battery.percent == 50 and discharging == True:
    toaster.show_toast('Battery Reminder',"Your battery is at 50%, please charge!")
    time.sleep(60)

elif battery.percent == 40 and discharging == True:
    toaster.show_toast('Battery Reminder',"Your battery is at 40%, please charge!")
    time.sleep(60)

elif battery.percent == 30 and discharging == True:
    toaster.show_toast("Battery Reminder","Your battery is at 30%, please charge immediately.")
    time.sleep(60)
    
elif battery.power_plugged == True:
    if battery.percent < 100:
        pass
    else:
        toaster.show_toast('Your battery is fully charged! Please unplug the charger!',"Battery Reminder")
        time.sleep(60)
    discharging = False
    
elif battery.power_plugged == False:
    discharging = True