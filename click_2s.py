import pyautogui as p
import time as t
import sys as s
import keyboard as k
while True:
    if k.is_pressed('Esc'):
        s.exit(0)
    t.sleep(3)
    p.click(button='left')    