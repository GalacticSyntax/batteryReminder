import psutil
import ctypes
from win10toast import ToastNotifier

toaster = ToastNotifier()

ICON_EXLAIM=0x30
ICON_STOP = 0x10

battery = psutil.sensors_battery()

while battery.power_plugged == False:
    for i in range(4):
                if battery.percent == 60:
                    if battery.percent == 50:
                        if battery.percent == 40:
                            if battery.percent == 30:
                                toaster.show_toast("Battery Reminder","Your battery is at 30%, please charge immediately.", icon_path="batteryhalf.png")
                            else:
                                toaster.show_toast("Battery Reminder","Your battery is at 40%, please charge.", icon_path="batteryhalf.png")
                        else:
                            toaster.show_toast("Battery Reminder","Your battery is at 50%, please charge.", icon_path="batteryhalf.png")
                    else:
                        toaster.show_toast("Battery Reminder","Your battery is at 60%, please charge.", icon_path="batteryhalf.png")

while battery.power_plugged == True:
    for i in range(1):
        if battery.percent < 100:
            pass
        else:
            toaster.show_toast("Your battery fully charged! Feel free to unplug anytime!", icon_path="batteryfull.png")

if not hasattr(psutil, "sensors_battery"):
    ctypes.windll.user32.MessageBoxW(0, "Sorry, but this platform is currently not supported.", "Unsupported", ICON_STOP)

if battery is None:
    ctypes.windll.user32.MessageBoxW(0, "This program has detected that there is no battery installed on this computer. Click OK to close this window.", "No Battery", ICON_EXLAIM)