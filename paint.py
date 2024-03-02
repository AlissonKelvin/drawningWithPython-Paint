import pyautogui
import time

distance = 300

print(pyautogui.size())
print(pyautogui.position())

pyautogui.moveTo(667,1051)
pyautogui.click(667,1051)
pyautogui.write("paint")

time.sleep(2)

pyautogui.press("enter")

time.sleep(2)

pyautogui.moveTo(675,395)

while distance > 0:
    pyautogui.dragRel(distance,0,1,button="left")
    distance = distance -20
    pyautogui.dragRel(0,distance,1,button="left")
    pyautogui.dragRel(-distance,0,1,button="left")
    distance = distance -20
    pyautogui.dragRel(0,-distance,1,button="left")

    