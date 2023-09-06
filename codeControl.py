import pyautogui as p
import time
img = './img/chrome_44.png'
img2= './img/pp.png'
web = 'facebook.com'
keyword = []
file_path = "svtable.txt"

with open(file_path, 'r') as file:
    
    for line in file:
        keyword.append(line.strip()+' Truong dai hoc Quang binh ') 
# print(keyword)

def _doubleCick(image): #func double clic
    klick = p.locateOnScreen(image)#If the file is not a png file it will not work
    print(p.click(klick))
    if klick != None:
        p.doubleClick(klick)

def _Cick(image):#func click
    klick = p.locateOnScreen(image)#If the file is not a png file it will not work
    print(klick)
    p.click(klick)
def _wp(url): #func open webpage
    time.sleep(1)
    p.write(url,interval=0.15)
    p.press('enter')
def _post(content): # func content post
    time.sleep(1)
    p.write(content,interval=0.15)
    p.hotkey('ctrl','enter')
    time.sleep(5)
# Start auto

_doubleCick(img)
_wp(web)
time.sleep(2)
for i in keyword:
    _Cick(img2)
    _post(i)
    
#close
p.click(1910,10,button='left')