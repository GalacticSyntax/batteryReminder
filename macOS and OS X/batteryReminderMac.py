import psutil
import pync
import subprocess as s

battery = psutil.sensors_battery()
discharging = True
x = 1

if not hasattr(psutil, "sensors_battery"):
    s.run("osascript -e 'Tell application ""System Events"" to display dialog 'Sorry, but this platform is currently not supported.' with title ""Unsupported")

if battery is None:
    s.run("osascript -e 'Tell application ""System Events"" to display dialog 'This program has detected that there is no battery installed on this computer. Click OK to close this window.' with title ""No Battery Detected")

if battery.percent == 60 and discharging == True:
    pync.notify(title="Battery Reminder","Your battery is at 60%, please charge.", title="Battery Reminder", app_icon="batteryhalf.png")

if battery.percent == 50 and discharging == True:
    pync.notify(title="Battery Reminder","Your battery is at 50%, please charge.", title="Battery Reminder", app_icon="batteryhalf.png")

if battery.percent == 40 and discharging == True:
    pync.notify(title="Battery Reminder","Your battery is at 40%, please charge.", title="Battery Reminder", app_icon="batteryhalf.png")

if battery.percent == 30 and discharging == True:
    pync.notify(title="Battery Reminder","Your battery is at 30%, please charge immediately.", title="Battery Reminder", app_icon="batteryhalf.png")

if battery.power_plugged == True:
    discharging = False
    if battery.percent < 100:
        x = 2
    else: 
        pync.notify("Your battery is fully charged! Feel free to unplug the charger.", title="Fully Charged!", app_icon='batteryfull.png')

if battery.power_plugged == False:
    discharging = True
