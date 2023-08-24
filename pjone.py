import pyautogui as p
import time
img = ['./img/chrome.png','./img/chrome_l.png']
img2= './img/photo_l.png'
web = 'facebook.com'
keyword = [
    "Why do programmers hate nature?\nIt has too many bugs.",
    "Why do Java developers wear glasses?\nBecause they don't see sharp.",
    "Why do C# and Java developers keep breaking their keyboards?\nBecause they use a strongly typed language.",
    "Why did the programmer quit his job?\nHe didn't get arrays.",
    "Why do programmers prefer dogs over cats?\nBecause dogs have a \"fetch\" function.",
    "Why did the programmer go to therapy?\nHe had too many issues.",
    "Why did the SQL query go to therapy?\nIt had too many relationship problems.",
    "Why do programmers always mix up Christmas and Halloween?\nBecause Oct 31 == Dec 25.",
    "Why don't programmers like nature documentaries?\nToo many bugs.",
    "Why did the programmer get thrown out of school?\nHe couldn't keep his classes together."
]
def _doubleCick(image): #func double click
    klick = p.locateOnScreen(image)#If the file is not a png file it will not work
    print(klick)
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
    time.sleep(10)
# Start auto

_doubleCick(img[0])
_wp(web)
time.sleep(2)
for i in keyword:
    _Cick(img2)
    _post(i)
#close
p.click(1910,10,button='left')