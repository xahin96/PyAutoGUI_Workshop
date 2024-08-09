import pyautogui
import time
import os

time.sleep(5)

# Adjust for potential scaling factor (e.g., 2x for Retina displays)
scaling_factor = 2

# Locate the image
position = pyautogui.locateOnScreen('copy.png')

if position:
    # Adjust coordinates
    adjusted_position = (position[0] / scaling_factor + 10, position[1] / scaling_factor + 10)
    pyautogui.moveTo(adjusted_position)
    pyautogui.click()
else:
    print("Image not found.")

