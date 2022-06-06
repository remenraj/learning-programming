# draw a square spiral in ms paint program
# switch to ms paint program when you run this program

import pyautogui

pyautogui.click()   # click to put drawing program in focus

distance = 250

while distance > 0:
    print(distance, 0)
    pyautogui.dragRel(distance, 0, duration=0)   # move right
    distance = distance - 25
    print(0, distance)
    pyautogui.dragRel(0, distance, duration=0)   # move down
    print(-distance, 0)
    pyautogui.dragRel(-distance, 0, duration=0)  # move left
    distance = distance - 25
    print(0, -distance)
    pyautogui.dragRel(0, -distance, duration=0)  # move up