import pyautogui
import time
import subprocess

# Brief pause to give you time to switch to the desired screen/window
time.sleep(5)

# Move the mouse to the first position and click
pyautogui.moveTo(680, 808)
pyautogui.click()

time.sleep(1)
pyautogui.typewrite("Please write a short python Hello world code")

time.sleep(1)
pyautogui.moveTo(1216, 809)
pyautogui.click()

time.sleep(5)
image_path = 'copy.png'
position = pyautogui.locateOnScreen(image_path)
if position:
    adjusted_position = ((position[0] / 2) + 10, (position[1] / 2) + 10)
    pyautogui.moveTo(adjusted_position)
    pyautogui.click()
else:
    print("Image not found on the screen.")

time.sleep(3)
subprocess.Popen(["open", "-a", "PyCharm"])

time.sleep(1)
pyautogui.hotkey('command', 'shift', 'j')

time.sleep(1)
pyautogui.press('enter')

time.sleep(1)
pyautogui.typewrite("testing.py")

time.sleep(1)
pyautogui.press('enter')

time.sleep(1)
pyautogui.press('enter')

time.sleep(1)
pyautogui.hotkey('command', 'v')

time.sleep(1)
pyautogui.hotkey('ctrl', 'shift', 'r')