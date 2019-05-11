### Things to note

The python file contains ```os.system(f"nohup python3 {dirpath}")```. This allows the program to run in the background. Adding an ampersand (&) to the end of the command makes it unkillable until the user shuts down the computer. This line of code doesn't contain an ampersand, which means the program can be killed using System Monitor.
