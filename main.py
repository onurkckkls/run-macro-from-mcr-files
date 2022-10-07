from fromMcr import FromMcr
import time
import win32gui
import win32con
from os.path import exists
import argparse
import re



def main():
    parser = argparse.ArgumentParser(description="from MCR")
    parser.add_argument("-m", default="", help="This is macro path, you can give relative or full path without extension", type=str)
    args = parser.parse_args()
    
    # When run program, if it has arg, take it as macro name
    path = re.sub(".mcr$", "", (args.m if args.m else input("Macro: ")))

    # File exists check and take input while found file
    file_exists = exists(path + ".mcr")
    while not file_exists:
        path = input("File Not Exists, Macro: ")
        file_exists = exists(path + ".mcr")

    # Sleep for looking like working
    time.sleep(2)

    # Minimize console window and focus second window before run the macro
    try:
        Minimize = win32gui.GetForegroundWindow()
        win32gui.ShowWindow(Minimize, win32con.SW_MINIMIZE)
        Foreground = win32gui.GetForegroundWindow()
        win32gui.SetForegroundWindow(Foreground)
    except:
        pass

    # Create object and run program
    macro = FromMcr(path)
    macro.run()


if __name__ == "__main__":
    main()
