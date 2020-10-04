import threading
import time

import PySimpleGUI as sg
import random
version = "alpha 10"
sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.

import pyautogui
from pynput.keyboard import *

resume_key = Key.home
pause_key = Key.end
exit_key = Key.f12

pause = True
running = True

def on_press(key): #loosely based on https://github.com/isaychris/python-autoclicker
    global running, pause

    if key == resume_key:
        pause = False
        print("[Resumed]")
    elif key == pause_key:
        pause = True
        print("[Paused]")
    elif key == exit_key:
        running = False
        print("[Exit]")


a = 1




layout = [  [sg.Text('Python Random Clicker '+version)],
            [sg.Text('Wait time in milliseconds or seconds?')],
            [sg.Radio('milliseconds', "RADIO1", default=True)],
            [sg.Radio('seconds', "RADIO1")],
            [sg.Text('Press HOME to start, END to end')],
            [sg.Text('Min wait time  '), sg.InputText(size=(10,5))],
            [sg.Text('Max wait time '), sg.InputText(size=(10,5))],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
#window = sg.Window('PRC '+ version, layout)
window = sg.Window(title='PRC '+ version, layout=layout, margins=(0, 0))
threads = []

def main():
    lis = Listener(on_press=on_press)
    lis.start()
    if values[0] == True:
        time_value = "milliseconds"
    if values[1] == True:
        time_value = "seconds"
    if time_value == "milliseconds":
        x = 1000
    if time_value == "seconds":
        x = 1
    while running:
        if not pause:
            pyautogui.click(pyautogui.position())
            pyautogui.PAUSE = random.uniform(float(values[2])/x, float(values[3])/x)
            print(random.uniform(float(values[2])/x, float(values[3])/x))
    lis.stop()

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    if a == 1:
        # Event Loop to process "events" and get the "values" of the inputs
        t = threading.Thread(target=main)
        threads.append(t)
        t.start()
        a=0

window.close()


