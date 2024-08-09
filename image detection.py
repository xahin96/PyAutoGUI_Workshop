import pyautogui
import time
import subprocess

# Brief pause to give you time to switch to the desired screen/window
time.sleep(5)

image_path = 'copy5.png'
position = pyautogui.locateOnScreen(image_path)
if position:
    adjusted_position = ((position[0] / 2) + 10, (position[1] / 2) + 10)
    pyautogui.moveTo(adjusted_position)
    pyautogui.click()
else:
    print("Image not found on the screen.")