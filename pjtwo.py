import pyautogui as p
file_path = "svtable.txt"
lines_list = []
with open(file_path, 'r' ,encoding='utf-8') as file:
    
    for line in file:
        lines_list.append(line.strip()+' Truong dai hoc Quang binh ') 

print(lines_list)
print(p.locateOnScreen('chrome_44.png'))
b = p.locateOnScreen('chrome_44.png')
print(b)

