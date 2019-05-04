import psutil
import ctypes
from win10toast import ToastNotifier

battery = psutil.sensors_battery()
toaster = ToastNotifier()
discharging = True
ICON_EXLAIM= 0x30
ICON_STOP = 0x10
x = 1

if not hasattr(psutil, "sensors_battery"):
    ctypes.windll.user32.MessageBoxW(0,"Sorry, but this platform is currently not supported.","Unsupported",ICON_EXLAIM)

if battery is None:
    ctypes.windll.user32.MessageBoxW(0, "This program has detected that there is no battery installed on this computer. Click OK to close this window.","No Battery Detected",ICON_STOP)

if battery.percent == 60 and discharging == True:
        toaster.show_toast("Battery Reminder","Your battery is at 60%, please charge to keep a healthy battery!", icon_path="batteryhalf.png")

if battery.percent == 50 and discharging == True:
        toaster.show_toast("Battery Reminder","Your battery is at 50%, please charge to keep a healthy battery!", icon_path="batteryhalf.png")

if battery.percent == 40 and discharging == True:
        toaster.show_toast("Battery Reminder","Your battery is at 40%, please charge to keep a healthy battery!", icon_path="batteryhalf.png")

if battery.percent == 30 and discharging == True:
        toaster.show_toast("Battery Reminder","Your battery is at 30%, please charge immediately.", icon_path="batteryhalf.png")

if battery.power_plugged == True:
    discharging = False
    if battery.percent < 100:
        x = 2
    else: 
        toaster.show_toast("Fully Charged!","Your battery is fully charged! Feel free to unplug the charger.", icon_path='batteryfull.png')

if battery.power_plugged == False:
    discharging = True  