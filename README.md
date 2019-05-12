# Usage and Installation Instructions

Thank you for your interest in my program! Read the instructions below to get everything up and running!

## Windows
*Note: Windows XP and lower are NOT supported.*\
\
Requirements:
* Python 3.7.3 or above\
\
This application requires Python to be installed. If you don't have it already, <a href="https://www.python.org/downloads/release/python-373/" target="_blank">Download</a> it.
Once Python is installed, go to the <a href="https://github.com/coolkiwiii/batteryreminder/releases" target="_blank">Releases</a> page and download *BatteryReminder-Windows.exe*. Next, hold Win+R to open Run. In Run type in ```shell:startup```. Then, copy *BatteryReminder-Windows.exe*  to that location. This makes the program start up everytime your computer boots into Windows.

## macOS/Mac OS X
*Note: Mac OS X 10.7 and lower are NOT supported.*\
\
Requirements:
* Python 3.7.3 or above
* brew\
\
First, if you don't have it already, install Python. Click <a href="https://www.python.org/downloads/release/python-373/" target="_blank">here</a> to download it. Run the installer. After Python is installed, you must install brew, if you don't have it already. Open up a terminal window (*If you can't find it, use Spotlight to search for "Terminal"*). Once you are in the terminal, copy and paste ```/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"```. This will install brew. Next, type ```brew install terminal-notifier``` in the terminal. After that, in the terminal type in ```pip3 install psutil pync```. Once that is done, head over to the <a href="https://github.com/coolkiwiii/batteryreminder/releases" target="_blank">Releases</a> page and download *BatteryReminder-Mac.zip*. Extract the .zip file and run the program.

## Linux
*Note: Many distros like Ubuntu already come with a compatible version of Python. Please check by entering ```python3``` in the terminal.*\
\
Requirements:
* Python 3.7.3 or above
* python3-tk
* pip
* psutil and notify2\
\
First, if you don't have it already, install Python. Click <a href="https://www.python.org/downloads/release/python-373/" target="_blank">here</a> to download it. Install the tar.gz. If you don't know how, look it up on Google. Open up a new terminal window and type in ```sudo apt install python3-pip``` or use the package manager your system has. Still in the terminal, type in ```pip3 install psutil notify2```. After it is installed, type ```sudo apt install pyhton3-tk``` or use the package manager your system has. Then, head over to the <a href="https://github.com/coolkiwiii/batteryreminder/releases" target="_blank">Releases</a> page and download *batteryRemind-Linux*. Execute it to start the program.
