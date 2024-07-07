import tkinter as tk
from tkinter import messagebox
import winreg
import os


#Function for the Restart Check
def check_restart_needed():
    # Open the Windows Update registry key
    key_path = r"SOFTWARE\Microsoft\Windows\CurrentVersion\WindowsUpdate\Auto Update\RebootRequired"
    try:
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path) as key:
            # Check if the "RebootRequired" value exists
            return True
    except FileNotFoundError:
        # If the key doesn't exist, no restart is needed
        return False

#Fucntion for the Button
def restart_clicked():
    restart_label = tk.Label(root, text="Computer will Restart in 30 seconds, please save unsave works! ")
    restart_label.pack()
    os.system("shutdown /r /t 30 /f")


def button2_clicked():
   exit()

def button3_clicked():
    exit()


#Funtion to stop the main loop if run at specific time
def stop_mainloop():
    root.quit()  # This will stop the mainloop
    os.system("shutdown /r /t 30 /f")



#Function when Window is being force close
def on_closing():
    if messagebox.askokcancel("Quit and Restart", "Do you want to quit and Restart?"):
        root.destroy()
        os.system("shutdown /r /t 30 /f")


if __name__ == "__main__":
    restart_needed = check_restart_needed()
    if restart_needed is True:
        # Main application window for the Button
        root = tk.Tk()
        root.title("Restart Window")

        # Button to open Popup 1
        popup1_button = tk.Button(root, text="Restart Computer!", command=restart_clicked)
        popup1_button.grid(pady=20, padx=200)

        label = tk.Label(root, text="If left untouched, Computer will restart in 2 minutes!")
        label.pack()

        # Button to open Popup 2
        popup2_button = tk.Button(root, text="Open Popup 2", command=button2_clicked)
        popup2_button.pack(pady=20, padx=100)

        # Configure a callback for when the window is closed when pressed the X in pop up
        root.protocol("WM_DELETE_WINDOW", on_closing)

        #Instantiate of tk and will stop and restart the PC if disregard the pop up for 2 mins.
        root.after(12000, stop_mainloop)


        root.mainloop()




    else:
        print("No restart needed.")
        root = tk.Tk()
        root.title("Main Window")
        popup3_button = tk.Button(root, text="Update Run, No Restart needed", command=button3_clicked)
        popup3_button.pack(pady=20, padx=100)

        # Configure a callback for when the window is closed
        root.protocol("WM_DELETE_WINDOW", on_closing)

        # Will run the root TK
        root.mainloop()

        exit()


