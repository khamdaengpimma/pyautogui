import pyautogui as pui
import time
url = 'facebook.com'
img = ['./img/chrome_l.png','./img/photo_l.png']
local = pui.locateOnScreen(img[0])
pui.doubleClick(local)
time.sleep(0.5)
pui.write(url,interval=0.15)
pui.press('enter')
time.sleep(2)
local2 = pui.locateOnScreen(img[1])
pui.click(local2)