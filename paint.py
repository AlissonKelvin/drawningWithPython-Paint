import pyautogui
import time

distance = 300

print(pyautogui.size()) #To know the size screen
print(pyautogui.position())#To know the position of the mouse

pyautogui.moveTo(667,1051)
pyautogui.click(667,1051)
pyautogui.write("paint") #Typing the word "Paint"

time.sleep(2)

pyautogui.press("enter")# Pressing the key

time.sleep(2)

pyautogui.moveTo(675,395)

while distance > 0: #Drawning in the paint
    pyautogui.dragRel(distance,0,1,button="left")
    distance = distance -20
    pyautogui.dragRel(0,distance,1,button="left")
    pyautogui.dragRel(-distance,0,1,button="left")
    distance = distance -20
    pyautogui.dragRel(0,-distance,1,button="left")

    