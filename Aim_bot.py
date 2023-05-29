from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api
import win32con


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
# Color of center: (255, 219, 195)


while not keyboard.is_pressed('q'):

    pic = pyautogui.screenshot(region=(570, 450, 760, 550))

    width, height = pic.size

    for x in range(0, 760, 5):
        print("x=", x)
        for y in range(0, 550, 5):
            print("y=", y)
            r, g, b = pic.getpixel((x, y))
            if b == 195:
                click(x+570, y+450)
                break
